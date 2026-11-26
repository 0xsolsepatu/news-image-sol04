# BUILD — news-image-20261125: "Sum up 25 November's world news in one image"

Entry for make.fun `news-image-20261125` ($100, 50 paid places; entries
close Thu 27 Nov 2026 07:00 WIB; results due 11 Dec 2026 15:00 WIB).
Built 25 Nov 2026 ~10:00–10:15 WIB by the builder subagent; Gemini
review (design placement) done by the parent before the build — see
`GEMINI-DESIGN.md`. The parent does the Gemini code/content review,
GitHub push and submit.

## Design

Same proven format as the 23 Nov entry (round 3 rank 219/13,031, top
1.7%): a "THE WORLD IN ONE DAY" newspaper front page, 1024×1024 PNG,
cream paper #F7F1E3, serif masthead "WEDNESDAY 25 NOVEMBER 2026", a
5-number stat strip, 3 illustrated lead panels (simple drawn scenes,
basic shapes only), a 9-card grid, a 12-item 2-column tail list, a DATE
CHECK box, a small world map + UTC timeline, and the footer
"MAKE.FUN // 25 NOVEMBER 2026 // 24-HOUR GLOBAL SUMMARY".

Layout (1024 tall): masthead 8–140, stat strip 146–198, leads 206–394,
grid 402–660, tail 668–912, bottom row (map | DATE CHECK | timeline)
914–984, footer rule 992, footer text 996–1015. `render.py` prints an
OK/OVERFLOW line per section and counts issues; this build reports
0 issues. Fonts: DejaVu Serif (bold) / DejaVu Sans (bold), all local.

- 3 LEADS (all PURE 25 Nov): (1) China launches first Pakistani to
  orbit — rocket lifting off a desert pad into a starry night sky;
  (2) Asia stocks tumble on tariff threat — falling red bar chart with
  a descending line and %; (3) Gaza death toll reaches 74,746 —
  crumbling-building outline + relief cross, restrained, no graphic
  detail.
- 9 GRID: Solomons pact (Reuters), CIA/ODNI breach (CNN, "sources
  say" attribution kept), Australia inflation (Reuters), oil slides
  (Reuters, mini falling-chart motif), Russia 490,334 dead (BBC), WHO
  Congo Ebola (WHO), Huawei guilty (DOJ/AFP, [24 NOV] tag), Houthis
  hit Riyadh tower (Reuters, [24 NOV] tag), Senegal AFCON crown
  (BBC/CAS, [24 NOV] tag).
- 12 TAIL, in Gemini's accepted order, each with a visible date tag:
  [25 Nov] Spain polls, [25 Nov] India food prices, [24 Nov] Citi
  Venezuela, [24 Nov] 266m hunger, [24 Nov] England T20I, [24 Nov]
  Banten fire toll 26, [24 Nov] Kyiv ship-hit confirmation,
  [24 Nov] Korean air alert, [24 Nov] Punjab alliance, [24 Nov]
  Hormuz tanker mines ("Iran says"), [24 Nov] Microsoft Code Red,
  [25 Nov] US tariffs. CORRECTION APPLIED (see GEMINI-DESIGN.md):
  Gemini mislabeled the US-tariffs item [24 Nov]; it is PURE 25 Nov
  (BBC/Reuters, 25 Nov) and is tagged [25 Nov] here. Tail item 8 uses
  the research headline "Russian jets trigger Korean air alert", not
  Gemini's "Russian Jets Scrambled On".
- STAT STRIP: GAZA TOLL 74,746 • RUSSIA DEAD 490,334 • CONGO EBOLA
  TOLL 5,775 • S. KOREA MARKET −5.3% • GLOBAL HUNGER 266M. (The 266M
  figure is the WFP warning of 24 Nov; it is flagged [24 Nov] in the
  tail list and covered by the DATE CHECK note.)
- DATE CHECK box: masthead date + "12 of the 24 stories stem from Tue
  24 Nov (or earlier). Each is flagged [24 Nov] in the tail list
  above."
- MAP pins: 1 Jiuquan, 2 Seoul, 3 Gaza, 4 Riyadh, 5 Banten,
  6 Canberra. TIMELINE: one verified timestamp only — 00:18 GMT
  Shenzhou-24 lifts off (Reuters, 25 Nov); no other time is printed.

## Story list (24, all verbatim from RESEARCH.md)

PURE 25 Nov (12): China launches first Pakistani to orbit; Asia stocks
tumble on tariff threat; Australia signs Solomons defence pact; CIA and
spy chief hit by cyber breach; Australia inflation beats forecasts; Oil
slides as glut fears trump war risk; Gaza death toll reaches 74,746;
Russia's own data: 490,334 war dead; India's food prices climb again;
Spain heads to polls on Sunday; WHO flees Congo Ebola hospital; US
readies new tariffs on trade partners.

LATE-24 (12): Citi weighs return to Venezuela; 266m face acute hunger,
WFP warns; Houthis hit Riyadh's tallest tower; Huawei guilty of
stealing trade secrets; England crush Australia in 2nd T20I; Senegal
keep AFCON crown after appeal; Indonesia factory fire toll hits 26;
Kyiv confirms Gulf of Finland ship hit; Russian jets trigger Korean air
alert; BJP, Akali Dal reunite for Punjab 2027; Tankers hit by mines in
Hormuz Strait; Microsoft declares 'Code Red' outage.

Sources: Reuters, BBC, CNN, AP, WHO, WAFA, DoJ/AFP, CAS, Bloomberg
(via Reuters), WFP, IRGC/UKMTO — see RESEARCH.md per story. No number,
name or claim was invented, embellished or merged; attributions
("sources say", "Iran says") are kept verbatim in the decks.

## Files

- `render.py` — build tool only (NOT for commit). Adapted from the
  23 Nov renderer: same helpers, palette and section logic; new
  content, re-balanced geometry (taller grid cards for 2-line titles
  + 2-line decks; 6-row tail list; compressed 70px bottom row).
- `entry.png` — the rendered entry (1024×1024).
- `main.py` — entry program (stdlib only): copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`),
  byte for byte, with PNG-magic and sha256 copy verification.
- `README.md` — entry description + make.fun badges. Badge lines
  taken from the LIVE requirements fetch
  (GET https://make.fun/api/competitions/news-image-20261125/requirements,
  25 Nov ~09:47 WIB), not from the 23 Nov README. Repo name assumed
  `news-image-sol04` (follows sol02 → sol03); the parent must correct
  it if the created repo is named differently. Referral code
  `r4c0y56z` reused from the 23 Nov README.
- `LICENSE` — MIT, copied from the 23 Nov workdir.

## Verification (25 Nov 2026 ~10:15 WIB)

- `entry.png`: 1024×1024, RGB, **188,387 bytes** (limit 1,048,576).
- **sha256: 2ae4de6bf8d0533e30c791018ff7bb7c334993053d60fffda04a106330ddb4d2**
- `render.py` run: 0 issues — no overflow, no truncation, no
  too-long tail/date-check line, no grid title dropped.
- `main.py` run twice (to `/tmp/mf-out1` and `/tmp/mf-out2`): both
  outputs byte-identical to `entry.png` — same sha256
  `2ae4de6b…ddb4d2` on all three.
- Parent fix after the builder's report: DATE CHECK line changed from
  "Each is flagged [24 Nov] in the tail list above." to "Each is
  flagged [24 Nov] where it appears." — the old wording was inaccurate
  (3 of the 12 late-24 stories sit in the grid, not the tail list).
  Re-rendered by the parent, 0 issues, byte-identical runs re-verified,
  DATE CHECK box re-read visually: new wording fits, no truncation.
- Scripted cross-check against RESEARCH.md: all 24 headlines and all
  24 decks present verbatim in `render.py` (the one apparent miss,
  the Sánchez deck, is present as the `\u00e1` escape and renders as
  "Sánchez"); 12 PURE / 12 LATE-24 counts match; every tail tag
  matches the research date flag (no mismatches); the three LATE-24
  grid cards (Huawei, Houthis, Senegal) carry `late24=True` and show
  a red [24 NOV] tag; all five stat numbers, the footer and the
  masthead date are present.
- Visual read at full size (1024×1024): every headline, deck, header,
  stat, date tag and the footer is legible, with no overlap and no
  text running under the footer. Two fixes applied after the first
  render: the rocket nose was redrawn inside the night-sky box, and
  the tail list was reordered to Gemini's accepted placement.
- Visual read at 300×300: masthead, date, stat numbers, lead
  headlines and grid headlines stay legible; the page structure
  (masthead → stats → 3 leads → 9 grid → tail → map/DATE CHECK/
  timeline → footer) is clear at thumbnail size.

---

## REBUILD v2 — 26 Nov 2026 ~09:00–09:45 WIB (rank review, solsepatu's 08:20 order)

Why: the v1 entry ranked 6,907/10,309 (judge 949,581; prize line 987,839;
gap 38,258 micro). Top-10 entries carry 32–55 stories, 15–21 drawn
fields, full UTC timelines, 10 regions. v2 closes the gap: **29 stories
(17 pure 25 Nov, 12 late-24)**, 6-stat strip (all pure), 10 map pins,
4-entry UTC timeline. 21 stories kept from v1; 8 new (Giza tanker, US
GDP/PCE, UK energy cap, West Java mine, UCL Wed night — all pure 25 Nov;
Dell, US confidence, Sooryavanshi — late-24). Dropped for space (still
verified): Citi Venezuela, Microsoft Code Red, Senegal AFCON, Giuliani
Medal of Freedom, Real Madrid 5-1 PSV. See RESEARCH.md "REBUILD v2".

### Design changes vs v1
- Stat strip: 5 → 6 boxes (74,746 Gaza; 490,334 Russia; 5,775 Congo;
  −5.3% S. Korea; 31 Giza; 4.3% US GDP). The 266M hunger figure moved to
  the tail (it is a 24 Nov warning).
- Grid: 9 → 12 cards (3 cols × 4 rows, 74px each; fonts 13pt/10pt).
  Two small top-right motifs kept (oil falling-chart, Giza flame);
  the other 10 cards use typographic tags only (per Gemini pass 1).
- Tail: 12 → 14 items (2 cols × 7 rows, 28px each; headline 12pt +
  1-line deck 9.5pt). US tariffs deck corrected per the Reuters wire
  of 25 Nov: 14 partners (not 16), China 20% on top of existing ~25%,
  Mexico and Norway spared.
- Bottom row: 70px → 98px (per Gemini pass 2): map with 10 pins
  (Jiuquan, Seoul, Gaza, Riyadh, Banten, Canberra, Giza, London,
  Washington, Bogor; 2-line legend) + DATE CHECK box (6 lines, incl. the
  6 rejected items) + UTC timeline with 4 verified entries (00:18 GMT
  Shenzhou-24 lifts off; 13:30 GMT BEA GDP 4.3%; 21:45 GMT UCL night
  ends — PSG held 2-2, Bayern beaten; 23:14 GMT AP reports Giza toll 31).
- No separate footer (bottom row ends 1014, 10px margin).
- Layout (1024 tall): masthead 8–132, stat strip 138–182, leads
  190–362 (illustrations rescaled to h=46), grid 370–684, tail 692–914,
  bottom row 916–1014.

### Gemini reviews (3 passes — see GEMINI-V2-REVIEW.md)
- Pass 1 (design, pre-build): 40–50 stories too dense; aim 32–35, no
  20-item tail, 3-tier flow, remove grid motifs. Adopted in revised form.
  Gemini's "larger canvases" claim is factually wrong (cap is 1024×1024).
- Pass 2 (revised 32-story plan): GO WITH CHANGES — 71px grid cards and
  62px bottom row would clip; expand bottom to ~110px, tail rows ≥26px,
  cut tail to 8–10. Geometry adopted (bottom 98px, tail 28px, cards
  74px); the story cut NOT adopted — 29 stories is the clean maximum,
  and cutting stories would undo the main improvement.
- Pass 3 (post-build): GO WITH CHANGES on one point — West Java mine
  date flag. Verified false against render.py: the card is already PURE
  (`late24=False`, no tag; cross-check pure=17). Gemini misread the
  prompt. Effective verdict: GO. No changes applied.

### Verification (26 Nov 2026 ~09:40 WIB)
- `render.py` run: **0 issues** — no overflow, no truncation, no
  too-long tail/date-check line, no grid title/deck over 2 lines.
- `entry.png`: 1024×1024, RGB, **206,369 bytes** (limit 1,048,576).
- **sha256: af3facf2ad1850c8a8d833b5093435a702aee0e6cb8a31eadb10e6da52fd350e**
- Two render runs byte-identical (same sha256).
- Scripted cross-check (`/tmp/check-v2.py`): all 29 headlines + decks
  verbatim vs RESEARCH.md v2; counts 3 leads / 12 grid / 14 tail;
  17 pure / 12 late; stat numbers match; DATE CHECK says 12 of 29;
  dropped items (Citi, Microsoft, Senegal, Giuliani, Real Madrid) absent.
  **0 failures.**
- Visual read at full size: every headline, deck, header, stat, date tag
  and the bottom row is legible, no overlap. Two fixes applied after the
  first v2 render: (1) timeline above-axis labels merged ("off3:30") —
  shortened the 13:30 label to "13:30 GDP 4.3%" (PCE stays in the grid
  card deck); (2) oil-card mini-chart motif struck through the word
  "risk" — motif cards now wrap titles to a narrower width (code fix in
  render.py). Both verified fixed by crop inspection (timeline + oil +
  Giza cards).
- Visual read at 300×300: masthead, date, stat numbers, lead headlines
  and grid headlines stay legible; the page structure (masthead → stats
  → 3 leads → 12 grid → tail → map/DATE CHECK/timeline) is clear at
  thumbnail size.
- `main.py` run twice (to two output dirs): both outputs byte-identical
  to `entry.png` — same sha256 `af3facf2…d350e` on all three.

---

## REBUILD v3 — 27 Nov 2026 ~00:15–01:30 WIB (rank review)

Why: the v2 entry ranked 8,042/21,134 (judge 975,976; prize line rank 50
at 989,109; rank 10 at 990,801). Top-10 entries carry 35–50 stories,
11–15 drawn scenes, a map, a full UTC timeline, a date check. v3: **45
stories (34 PURE 25 Nov, 11 LATE-24)** — 29 kept from v2 + 16 new
(13 pure, 3 late; a 14th pure and 4th late were researched and cut for
space — see RESEARCH.md). Dropped from v2 (still verified): England
T20I, Punjab alliance, Korean air alert, Kyiv ship confirmation, US
confidence. Research: coordinator (10 pure + 3 late, all verified
against Reuters/AP/BBC/CNN/White House) + research subagent (20 pure +
4 late, merged; overlaps confirmed the coordinator's findings).

### Design changes vs v2
- Grid: 12 → 15 cards (3 cols × 5 rows, 64px each per Gemini pass 1;
  fonts 12pt title max 2 lines / 8.5pt deck ONE line ≤70 chars; two
  decks shortened after the first render flagged 2-line wraps: Giza,
  Savasleyka). Small geometric motifs on all 15 cards (flame, bars,
  bolt, pick, jet, gavel, balloon, plane, lightning, flag, chip,
  satellite, chart-down, scales, waves) + 3 lead illustrations + map +
  timeline = 17 drawn elements.
- Tail: 14 → 27 items, 2 cols × 14 rows, SINGLE-LINE rows (18px):
  "[tag] Headline — deck" at 10pt bold headline / 9pt deck (Gemini
  pass 1: stacked 22px rows would overlap; the 30px-row alternative
  would have forced cutting the tail to 21 items). Decks shortened to
  terse supporting facts; the renderer measures every line and flags
  anything over 478px (11 lines trimmed in two passes).
- Leads: same 3 (illustration h=28, title 18pt, deck 11pt, 132px panels).
- Stat strip: unchanged (6 boxes, all pure 25 Nov).
- Bottom row: 98px → 92px: map with 12 pins (Jiuquan, Seoul, Gaza,
  Riyadh, Banten, Canberra, Giza, London, Washington, Bogor, Pyongyang,
  Madrid; closest pair London/Madrid 11.3px apart, r=5 circles do not
  touch) + 2-line legend + DATE CHECK box (11 of 45 from 24 Nov +
  6 rejected items incl. Villavicencio date-unclear, Niger State
  unverified) + UTC timeline with 6 verified entries (00:18 Shenzhou;
  12:01 White House children announcement; 13:30 BEA GDP; 15:00 Iowa
  blast 09:00 CST; 21:45 UCL ends; 23:14 AP Giza toll) in 4 staggered
  label rows (2 above, 2 below the axis). One fix after the first
  render: 13:30 and 23:14 labels collided ("13:30 GDP3:14 Giza 31") —
  13:30 moved to the second above-axis row; crop inspection confirms
  all 6 labels distinct.
- Layout (1024 tall): masthead 6–110, stat strip 114–152, leads
  158–290, grid 296–640, tail 646–920, bottom row 922–1014.

### Gemini reviews (2 passes — see GEMINI-V2-REVIEW.md)
- Pass 1 (design, pre-build): GO WITH CHANGES — grid cards 60→64px
  (adopted); tail rows single-line (adopted); bottom row to 130px by
  cutting tail to 21 (NOT adopted — 94px proven by v2, 6-entry timeline
  fits with staggered labels, verified by render + crop inspection).
  Fact flags: Nvidia Wednesday session confirmed; SpaceX "Starmind"
  proven real (AP/Reuters/WSJ) — Gemini's doubt was wrong; Iowa blast
  9,500 lb / 09:00 CST confirmed (Des Moines Register); Andy Taylor
  "announces" present tense kept (headline style; deck states died Monday).
- Pass 3 (post-build): GO. One flag — Andy Taylor "died 24 Nov 2023":
  VERIFIED FALSE (Reuters/BBC/CNN/AP 25 Nov 2026; died Mon 23 Nov 2026).
  Honest assessment: density alone unlikely to bridge the 13k gap to the
  prize line; expects high 970ks. Top 50 remains a stretch, not a promise.

### Verification (27 Nov 2026 ~01:20 WIB)
- `render3.py` run: **0 issues** — no overflow, no truncation, no
  2-line grid deck, no tail line over 478px, no grid title over 2 lines.
- `entry.png`: 1024×1024, RGB, **226,322 bytes** (limit 1,048,576).
- **sha256: 36a2fff395f6375e481e99d41b806e17472cf42ffdcb7975f1746cb7014fb40b**
- Two render runs byte-identical (same sha256); `main.py` run twice (to
  two output dirs): both outputs byte-identical to `entry.png`.
- Scripted cross-check (`/tmp/check-v3.py`, AST-based): all 45 headlines
  present in RESEARCH.md (4 documented shortenings: tariffs, Solomons,
  Andy Taylor, Putin); every deck number appears in RESEARCH.md; counts
  3 leads / 15 grid / 27 tail; 34 pure / 11 late; stat numbers match;
  DATE CHECK says 11 of 45; dropped items absent as stories
  (Villavicencio/Niger State appear only as DATE CHECK rejections).
  **0 failures.**
- Visual read at full size: every headline, deck, header, stat, date tag,
  map pin, timeline label and the bottom row is legible, no overlap.
  Crop-inspected: timeline (all 6 labels distinct), tail, grid rows 4–5.
- Visual read at 300×300: masthead, date, stat numbers, lead headlines
  and grid headlines stay legible; page structure (masthead → stats →
  3 leads → 15 grid → tail → map/DATE CHECK/timeline) is clear.
- Nvidia deck uses the Reuters CLOSE figure −3.9% (not the −4.6%
  intraday figure); the Russia-grid deck avoids the "five killed" figure
  seen only in social summaries (Reuters: one killed in Kyiv region).
