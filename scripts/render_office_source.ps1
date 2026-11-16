param([Parameter(Mandatory=$true)][string]$PaperId)
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path $PSScriptRoot -Parent
$inventory = Get-Content -LiteralPath (Join-Path $repoRoot 'research/metro/metro-inventory.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$sourceRow = @($inventory.sources.PSObject.Properties.Value.files | Where-Object { $_.id -eq $PaperId }) | Select-Object -First 1
if (-not $sourceRow -or $sourceRow.format -notin @('doc','docx','odt')) { throw 'Expected an inventoried Office question source.' }
$sourcePath = [IO.Path]::GetFullPath((Join-Path $repoRoot $sourceRow.localPath))
if ((Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash.ToLower() -ne $sourceRow.sha256) { throw 'Source checksum mismatch.' }
$renderDirectory = Join-Path $repoRoot 'research/metro/rendered'
New-Item -ItemType Directory -Path $renderDirectory -Force | Out-Null
$renderPath = Join-Path $renderDirectory ($PaperId + '.pdf')
$wordInstance = $null
$sourceDocument = $null
try {
    $wordInstance = New-Object -ComObject Word.Application
    $wordInstance.Visible = $false
    $wordInstance.DisplayAlerts = 0
    $wordInstance.AutomationSecurity = 3
    $sourceDocument = $wordInstance.Documents.Open($sourcePath, $false, $true, $false)
    $sourceDocument.ExportAsFixedFormat($renderPath, 17)
} finally {
    if ($sourceDocument) { $sourceDocument.Close(0); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($sourceDocument) }
    if ($wordInstance) { $wordInstance.Quit(0); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($wordInstance) }
}
python -X utf8 (Join-Path $PSScriptRoot 'register_office_render.py') $PaperId
if ($LASTEXITCODE -ne 0) { throw 'Failed to register source rendering.' }
