import json,pathlib,collections
R=pathlib.Path(__file__).resolve().parent
ap=R/'full-official-crawl-audit.json';a=json.loads(ap.read_text(encoding='utf8'));over=json.loads((R/'paper-metadata-overrides.json').read_text(encoding='utf8'));visual=json.loads((R/'full-official-header-visual-review.json').read_text(encoding='utf8'));screen=json.loads((R/'full-official-header-screen.json').read_text(encoding='utf8'));word=json.loads((R/'full-official-word-header-render-manifest.json').read_text(encoding='utf-8-sig'))
for row in a['allMathFiles']:
    if row['id'] not in over:continue
    o=over[row['id']];row['resolvedMetadataOverride']=o;row['confirmedHeaderSlot']={k:o.get(k,row.get(k)) for k in ['year','semester','exam','grade']}
    if any(row.get(k)!=row['confirmedHeaderSlot'][k] for k in ['year','semester','exam','grade']):
        row['eligibleAsDeclaredYearQuestion']=False;row['identityStatus']='confirmed-header-conflict'
        row['headerVerification']=o['metadataBasis']
    if o.get('contentDuplicateOf'):row['canonicalContentSourceId']=o['contentDuplicateOf']
ids={r['id']:r for r in a['allMathFiles']}
for schoolkey in ['zhonghua','luodong']:a[schoolkey]['mathFiles']=[ids[r['id']] for r in a[schoolkey]['mathFiles']]
for cell in a['coverage']:
    cell['nonConflictingDeclaredQuestionIds']=[i for i in cell['questionFileIds'] if ids[i].get('eligibleAsDeclaredYearQuestion',True)]
    if cell['questionFileIds'] and not cell['nonConflictingDeclaredQuestionIds']:cell['status']='listed-question-header-conflict'
a['criticalFindings']['additionalVisualHeaderCorrections']=visual
a['headerScreenSummary']={'questionFiles':screen['originalQuestionFiles'],'statuses':screen['statuses'],'remainingTextMismatchCandidates':len(screen['potentialConflicts']),'policy':screen['policy'],'fullReport':'research/full-official-header-screen.json','manualVisualFindings':'research/full-official-header-visual-review.json','scanWarning':'83 scanned/header-unresolved files still require visual/OCR identity review; no automated year override was applied to them.'}
a['wordHeaderConversionSummary']={'originalWordFiles':len(word),'statuses':dict(collections.Counter(r['status'] for r in word)),'manifest':'research/full-official-word-header-render-manifest.json','scope':'All33 Word originals can now supply PDF first-page text for identity screening; only the original4 priority files were inspected across all pages. This is not a claim that all other Word question bodies were fully visually accepted.'}
ap.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'headerScreen':a['headerScreenSummary']['statuses'],'wordOriginals':len(word),'canonicalDuplicateAliases':{r['id']:r['canonicalContentSourceId'] for r in a['allMathFiles'] if r.get('canonicalContentSourceId')}},ensure_ascii=False))
