# Render metro Word originals to PDF with a fresh hidden Word instance (macros disabled,
# links not updated, read-only). Usage: render_word.ps1 <targets.json>
# targets.json: [{ "id": "...", "source": "research/metro/raw/....docx" }]
param([Parameter(Mandatory=$true)][string]$Targets)
$ErrorActionPreference = 'Stop'
$project = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$outDir = Join-Path $PSScriptRoot 'render'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
$items = Get-Content -LiteralPath $Targets -Raw -Encoding UTF8 | ConvertFrom-Json
$manifestPath = Join-Path $PSScriptRoot 'render-manifest.json'
$rows = @()
if (Test-Path $manifestPath) { $rows = @(Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json) }
$word = New-Object -ComObject Word.Application
try {
  $word.Visible = $false
  $word.DisplayAlerts = 0
  $word.AutomationSecurity = 3
  $word.Options.UpdateLinksAtOpen = $false
  foreach ($item in $items) {
    $source = Join-Path $project ($item.source -replace '/', '\')
    $pdf = Join-Path $outDir ($item.id + '.pdf')
    $row = [ordered]@{ id=$item.id; sourcePath=$item.source; sourceSha256=(Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLower(); renderPath=('research/metro/render/' + $item.id + '.pdf'); method='Hidden Microsoft Word; macros disabled; links not updated; read-only; ExportAsFixedFormat PDF'; status='pending' }
    $doc = $null
    try {
      $doc = $word.Documents.Open($source, $false, $true, $false)
      $doc.ExportAsFixedFormat($pdf, 17)
      $row.renderSha256 = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()
      $row.status = 'rendered'
    } catch { $row.status = 'failed'; $row.error = $_.Exception.Message }
    finally { if ($null -ne $doc) { $doc.Close(0); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc) } }
    $rows = @($rows | Where-Object { $_.id -ne $item.id }) + @([pscustomobject]$row)
    Write-Output ("{0} {1}" -f $item.id, $row.status)
  }
} finally {
  $word.Quit(0); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($word)
}
$rows | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $manifestPath -Encoding utf8
