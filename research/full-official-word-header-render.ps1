$ErrorActionPreference='Stop'
$project=Split-Path -Parent $PSScriptRoot
$outDir=Join-Path $PSScriptRoot 'bulk-render-headers'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
$papers=Get-Content -Raw -LiteralPath (Join-Path $project 'public\data\papers.json') | ConvertFrom-Json
$targets=@($papers | Where-Object { $_.format -in @('doc','docx') })
$priority=Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot 'bulk-render-manifest.json') | ConvertFrom-Json
$known=@{}
foreach($r in $priority){$known[$r.id]=$r}
$byHash=@{};$rows=@();$word=$null;$owned=$false
try {
 $word=New-Object -ComObject Word.Application
 if($word.Documents.Count -ne 0){throw 'Fresh Word instance unexpectedly has documents; no existing document will be touched.'}
 $owned=$true;$word.Visible=$false;$word.DisplayAlerts=0;$word.AutomationSecurity=3;$word.Options.UpdateLinksAtOpen=$false
 foreach($p in $targets){
  $relative=if($p.originalFile){$p.originalFile}else{$p.file}
  $source=[IO.Path]::GetFullPath((Join-Path (Join-Path $project 'public') $relative))
  $sha=(Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLower()
  $row=[ordered]@{id=$p.id;school=$p.school;year=$p.year;semester=$p.semester;exam=$p.exam;grade=$p.grade;sourcePath=('public/'+$relative.TrimStart('.','/'));sourceSha256=$sha;status='pending'}
  $doc=$null
  try {
   if($sha -ne $p.sha256){throw 'Original source SHA mismatch before read-only conversion.'}
   if($known.ContainsKey($p.id)){
    $render=[IO.Path]::GetFullPath((Join-Path $project $known[$p.id].renderPath))
    $row.renderPath=$known[$p.id].renderPath;$row.method='Reused the four-file priority read-only Word conversion with matching original SHA.';$row.status='existing-render-verified'
   } elseif($p.file.EndsWith('.pdf')){
    $render=[IO.Path]::GetFullPath((Join-Path (Join-Path $project 'public') $p.file))
    $row.renderPath=('public/'+$p.file.TrimStart('.','/'));$row.method='Reused existing derived PDF from matching original Word source.';$row.status='existing-render-verified'
   } elseif($byHash.ContainsKey($sha)) {
    $render=$byHash[$sha];$row.renderPath=$render.Substring($project.Length+1).Replace('\','/');$row.method='Reused the new PDF for an identical original Word SHA; source identity remains separate.';$row.status='identical-original-render-reused'
   } else {
    $render=Join-Path $outDir ($p.id+'.pdf')
    $doc=$word.Documents.Open($source,$false,$true,$false)
    $doc.ExportAsFixedFormat($render,17)
    $row.renderPath=('research/bulk-render-headers/'+$p.id+'.pdf');$row.method='Fresh hidden Word instance; force-disable macros; do not update links; read-only; no recent-file entry; ExportAsFixedFormat PDF.';$row.status='rendered-now'
   }
   $row.renderSha256=(Get-FileHash -LiteralPath $render -Algorithm SHA256).Hash.ToLower();$row.bytes=(Get-Item -LiteralPath $render).Length;$byHash[$sha]=$render
  } catch {$row.status='failed';$row.error=$_.Exception.Message}
  finally {if($null -ne $doc){$doc.Close(0);[void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc)}}
  $rows+=$row
  $rows | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'full-official-word-header-render-progress.json') -Encoding utf8
  Write-Output ($p.id+': '+$row.status)
 }
} finally {
 if($null -ne $word -and $owned){$word.Quit(0)}
 if($null -ne $word){[void][Runtime.InteropServices.Marshal]::ReleaseComObject($word)}
}
$rows | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'full-official-word-header-render-manifest.json') -Encoding utf8
