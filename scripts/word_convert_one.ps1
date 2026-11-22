param(
    [Parameter(Mandatory = $true)][string]$InputPath,
    [Parameter(Mandatory = $true)][string]$OutputPath,
    [Parameter(Mandatory = $true)][string]$LogPath
)
# Convert ONE legacy Word file (.doc / .odt / .rtf) to .docx with the installed Word, unattended.
# Run it through scripts/word_convert.py (separate process + timeout); it logs each step so a hang shows where.
$ErrorActionPreference = 'Stop'
function Log($m) { Add-Content -LiteralPath $LogPath -Value ((Get-Date -Format 'HH:mm:ss.fff') + ' ' + $m) -Encoding UTF8 }
Remove-Item -LiteralPath $LogPath -ErrorAction SilentlyContinue
$word = $null
$doc = $null
try {
    Log 'start'
    $tmpDir = Join-Path ([IO.Path]::GetTempPath()) ('wordconv_' + [guid]::NewGuid().ToString('N').Substring(0, 8))
    New-Item -ItemType Directory -Path $tmpDir | Out-Null
    $copy = Join-Path $tmpDir ('src' + [IO.Path]::GetExtension($InputPath))
    Copy-Item -LiteralPath $InputPath -Destination $copy
    Unblock-File -LiteralPath $copy -ErrorAction SilentlyContinue
    Log 'copied+unblocked'
    $word = New-Object -ComObject Word.Application
    Log ('word created')
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.AutomationSecurity = 3
    try { $word.Options.ConfirmConversions = $false } catch { Log ('ConfirmConversions: ' + $_.Exception.Message) }
    try { $word.Options.UpdateLinksAtOpen = $false } catch { }
    try { $word.Options.CheckSpellingAsYouType = $false; $word.Options.CheckGrammarAsYouType = $false } catch { }
    Log 'options set'
    $m = [Type]::Missing
    $doc = $word.Documents.Open($copy, $false, $true, $false, 'x', 'x', $false, 'x', 'x', 0, $m, $false, $false, $m, $true)
    Log ('opened, paragraphs=' + $doc.Paragraphs.Count)
    $outDir = Split-Path -Parent $OutputPath
    if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }
    $fmt = 16
    if ($OutputPath -like "*.pdf") { $fmt = 17 }
    $doc.SaveAs2($OutputPath, $fmt)
    Log 'saved'
    $zero = 0
    $doc.Close([ref]$zero)
    $doc = $null
    $word.Quit([ref]$zero)
    $word = $null
    Log 'done'
    exit 0
} catch {
    Log ('ERROR: ' + $_.Exception.Message)
    exit 2
} finally {
    $zero2 = 0
    if ($doc) { try { $doc.Close([ref]$zero2) } catch { } }
    if ($word) { try { $word.Quit([ref]$zero2) } catch { } }
}
