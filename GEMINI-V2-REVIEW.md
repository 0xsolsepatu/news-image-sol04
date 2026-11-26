# GEMINI REVIEWS — news-image-20261125 REBUILD v2 (26 Nov 2026)

Three review passes, per solsepatu's order (26 Nov 08:20 WIB): "lakukan
pengecekan berulang bersama Gemini sebelum di-submit". Model:
gemini-3.5-flash-lite. Every Gemini factual claim was verified against
the source before applying — its factual judgment has proven unreliable.

## Pass 1 — design review, pre-build (~09:00 WIB, 1,567 tokens)
Prompt: 40–50 story denser-layout plan vs the top-10 pattern.
Verdict: denser layout (40–50 stories + 12-card grid + 20-item tail +
motifs) would FAIL readability/craft at 300px; 40–50 stories in
1024×1024 unrealistic (sub-6pt type / clipping); recommends ABOLISH the
20-item tail, use a 15-story grid/column structure, 3-tier vertical flow
(masthead+stats top 15%, 3 leads + dense 2-col briefs middle 50%, UTC
timeline + map + DATE CHECK bottom 35%), remove flat motifs from grid
cards (typographic tags instead), aim for 32–35 stories maximum.
- ADOPTED: 32–35 target (revised to 32 in the draft), no 20-item tail,
  3-tier flow, motifs removed from grid cards (kept only 2 small
  top-right motifs: oil chart, Giza flame).
- REJECTED (with evidence): Gemini's claim that top entries "likely use
  much larger canvases" is factually wrong — the competition caps images
  at 1024×1024, so the top-10 entries fit 32–55 stories in the same
  canvas. The legibility concern stands; the canvas claim does not.
- Gemini made no news claims in this review (design only).

## Pass 2 — revised-plan design review (~09:10 WIB, 1,443 tokens)
Prompt: revised 32-story plan (3 leads + 12 grid + 17 tail, headline-only
tail at 22px rows, grid cards 71px, bottom row 62px).
Verdict: GO WITH CHANGES. (1) 17-item headline-only tail at 22px rows =
"risky noise" at 300px; (2) 71px grid cards with headline + 2-line deck
+ tags = "extremely cramped; text collision imminent"; (3) 62px bottom
row for map + DATE CHECK + 4-entry timeline = "severe overflow risk",
needs 100–120px; (4) cut the tail to 8–10 items, expand the bottom zone
to ~110px, drop the 2-line deck from grid cards, tail rows ≥26px.
- ADOPTED (geometry): bottom zone expanded to 98px, tail rows 28px
  (headline + 1-line deck), grid cards 74px (not 71px), leads 172px.
- NOT ADOPTED (story cut): cutting the tail to 8–10 would drop the
  total to ~27–29 stories and undo the main improvement (story count is
  the top-10 entries' clearest differentiator: 32–55 vs our 24). The
  geometry warnings were addressed by REDESIGN, not by cutting stories.
  Final total: 29 stories (3 leads + 12 grid + 14 tail) — the clean
  maximum this layout holds at legible sizes, per the v1 render evidence
  (82px cards with headline + 2-line deck + tags render cleanly).
- Gemini made no news claims in this review (design only).

## Pass 3 — post-build review (~09:40 WIB, 1,593 tokens)
Prompt: the built entry (full story list, stat strip, map, DATE CHECK,
timeline, and the two fixes already made).
Verdict: GO WITH CHANGES, single point — the West Java mine flood date
flag. Gemini claimed it is "Flagged as [24 Nov] in the build" and should
be [25 Nov] PURE if the toll was reported Wed 25 Nov.
- VERIFIED AGAINST THE SOURCE (render.py): the claim is WRONG. The card
  is `("ASIA", "West Java mine flood kills 9", ..., "AP", False, None)` —
  `late24=False`, i.e. already PURE with no [24 NOV] tag. The scripted
  cross-check confirms it (story #7 pure=True; pure count 17, not 16).
  The research appendix already records it as PURE 25 Nov (first report
  of the deaths/rescue; the flood itself was Mon 23 Nov). No change
  needed; Gemini misread the prompt's grid list.
- Headline accuracy: no overstatements found. Design: 29-story density
  "well-balanced and appropriately restrained"; 300px legibility "solid"
  after the two fixes.
- EFFECTIVE VERDICT: GO. No changes applied from pass 3.

## Summary
- Pass 1: design GO with the 32–35 target (adopted in revised form).
- Pass 2: geometry fixes adopted; story-cut rejected with evidence.
- Pass 3: GO (the one flagged item is a Gemini misread, verified false).
- Build proceeds to push + submit.
