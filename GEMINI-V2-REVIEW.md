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

---

## REBUILD v3 — Gemini reviews (27 Nov 2026)

### Pass 1 — design review, pre-build (~00:35 WIB, 2,145 tokens)
Prompt: 45-story plan (3 leads + 15 grid + 27 tail), geometry budget,
6-entry timeline, 12 map pins, 17 drawn elements.
Verdict: GO WITH CHANGES.
- (1) Grid cards 60px -> 64px (3 lines of text need ~51-55px + padding).
  ADOPTED: cards 64px, grid 296-640.
- (2) Tail rows 22px stacked headline+deck = overlap risk; use 30px rows
  or single-line lead-in rows. ADOPTED in the single-line form: tail items
  become one-liners ("[tag] Headline — deck" at 9.5pt, 18px rows, 27 items
  in 2 cols x 14 rows). The 30px-row alternative would have forced cutting
  the tail to 21 items; the single-line form keeps all 45 stories.
- (3) Bottom row 100px too small for 12 pins + legend + DATE CHECK +
  6-entry timeline; cut tail to 21 and expand to 130px. NOT ADOPTED as
  stated: the bottom row stays ~94px (v2's 98px row already held 10 pins +
  DATE CHECK + 4-entry timeline cleanly); the 6-entry timeline uses 4
  staggered label rows (2 above, 2 below the axis) to avoid collisions,
  and the map legend stays 2 lines at 7.5pt. Verified by render + visual
  read instead of by cutting stories.
- Thumbnail legibility: masthead + stats legible at 300px; lead headlines
  marginal; grid headlines unreadable as text at 300px but fine as
  structural blocks (judge reads hierarchy, not raw text, at thumbnail).
- Fact flags — ALL VERIFIED against sources before acting:
  * Nvidia date/market: CONFIRMED. S&P action "on Wednesday" (Reuters,
    25 Nov); Wed 25 Nov was a normal session, Nasdaq fell 2% Wednesday
    (Reuters wrap); markets closed Thu for Thanksgiving. No change.
  * SpaceX "Starmind": Gemini doubted the name. PROVEN REAL — AP
    (NPR Illinois, 26 Nov 00:53 CST): "a data center constellation called
    'Starmind'"; Reuters 25 Nov: FCC "approving the SpaceX 'Starmind'
    constellation"; WSJ/CNN confirm. Gemini's doubt was wrong. No change.
  * US Army Iowa blast: CONFIRMED — Des Moines Register: "roughly 9,500
    pounds", "9 a.m. blast on Wednesday, Nov. 25"; Wikipedia entry:
    9:00 AM CST (15:00 UTC), 68 drums, Iowa Army Ammunition Plant.
    "9,500 lb" is the Army's stated figure (some sources say 9,700 lb net
    explosive weight; the deck uses the Army's 9,500). No change.
  * Andy Taylor tense: Gemini wants "announced Wed" (past) instead of
    "announces". NOT ADOPTED: "announces" is standard headline present
    tense for a Wednesday-dated paper, and the deck states he died Monday.
    No change.

### Pass 3 — post-build review (~01:00 WIB, 1,800 tokens)
Prompt: the built v3 entry (full 45-story list, stat strip, DATE CHECK,
6-entry timeline, 12 pins, the two fixes already made, 300px legibility).
Verdict: GO. No remaining concrete problems. Layout verified clean
(0 issues, byte-identical renders, timeline collision resolved, no
multi-line grid decks).
- Fact flag — Andy Taylor: Gemini claimed he "actually passed away on
  November 24, 2023". VERIFIED FALSE against the sources: Reuters
  25 Nov 2026 ("died at age 65 on Monday", joint statement released
  Wednesday), BBC/CNN/AP all 25 Nov 2026, died Mon 23 Nov 2026 of
  metastatic prostate cancer. Gemini hallucinated the 2023 date. No change.
- All other stories: no flags.
- Honest assessment: density alone is unlikely to bridge the 13k gap to
  the prize line; expects high 970ks; top 50 would need qualitative
  polish, not just more stories. Kept as the honest note (same as v2:
  top 50 is a stretch, not a promise). Effective verdict: GO.
