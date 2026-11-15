$ErrorActionPreference = 'Stop'
$project = Split-Path -Parent $PSScriptRoot
$outDir = Join-Path $PSScriptRoot 'bulk-render'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
$targets = @(
  @{ id='1n9YoleDH0qAnQI2e-kctebYBYMlXIUc6'; file='1n9YoleDH0qAnQI2e-kctebYBYMlXIUc6.doc'; school='中華國中';year=107;semester=1;exam=2;grade=8 },
  @{ id='16EeKUo1TFlipf950nPiry7mpCxdq6Cp-'; file='16EeKUo1TFlipf950nPiry7mpCxdq6Cp-.docx';school='中華國中';year=108;semester=1;exam=2;grade=8 },
  @{ id='ld-106-1-2-8'; file='ld-106-1-2-8.doc';school='羅東國中';year=106;semester=1;exam=2;grade=8 },
  @{ id='ld-108-1-2-8'; file='ld-108-1-2-8.doc';school='羅東國中';year=108;semester=1;exam=2;grade=8 }
)
$rows = @()
$word = $null
$ownedInstance = $false
try {
  $word = New-Object -ComObject Word.Application
  if ($word.Documents.Count -ne 0) { throw 'The new Word instance contains existing documents; stopped without closing it.' }
  $ownedInstance = $true
  $word.Visible = $false
  $word.DisplayAlerts = 0
  $word.AutomationSecurity = 3
  $word.Options.UpdateLinksAtOpen = $false
  foreach ($item in $targets) {
    $source = Join-Path (Join-Path $project 'public\papers') $item.file
    $pdf = Join-Path $outDir ($item.id + '.pdf')
    $row = [ordered]@{ id=$item.id;school=$item.school;year=$item.year;semester=$item.semester;exam=$item.exam;grade=$item.grade;sourcePath=('public/papers/'+$item.file);sourceSha256=(Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLower();renderPath=('research/bulk-render/'+$item.id+'.pdf');method='Fresh hidden Microsoft Word instance; macros forced disabled; links not updated; open read-only and not added to recent files; ExportAsFixedFormat PDF';status='pending' }
    $doc = $null
    try {
      $doc = $word.Documents.Open($source, $false, $true, $false)
      $doc.ExportAsFixedFormat($pdf, 17)
      $row.renderSha256 = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()
      $row.bytes = (Get-Item -LiteralPath $pdf).Length
      $row.status = 'rendered'
    } catch {
      $row.status = 'failed'
      $row.error = $_.Exception.Message
    } finally {
      if ($null -ne $doc) { $doc.Close(0); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc) }
    }
    $rows += $row
    $rows | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'bulk-render-manifest.json') -Encoding utf8
    Write-Output ($item.id + ': ' + $row.status)
  }
} finally {
  if ($null -ne $word -and $ownedInstance) { $word.Quit(0) }
  if ($null -ne $word) { [void][Runtime.InteropServices.Marshal]::ReleaseComObject($word) }
}
