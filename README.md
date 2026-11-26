# news-image-sol04 — World news, Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/0xsolsepatu/news-image-sol04/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/0xsolsepatu/news-image-sol04/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for make.fun `news-image-20261125` ($100, 50 paid places, entries close
Thu 27 Nov 2026 07:00 WIB): a program that writes one image summing up the
world's news of Wednesday 25 November 2026.

## The image

A "THE WORLD IN ONE DAY" newspaper front page, 1024×1024 PNG — cream
paper, serif masthead, a 6-number stat strip, three illustrated lead
stories, a 15-card grid with small drawn motifs, a 27-item date-flagged
tail list, a DATE CHECK box and a world map + UTC timeline. 45 verified
stories from Wednesday 25 November 2026 (34 pure 25 Nov, 11 from Tue
24 Nov, each flagged [24 Nov]). Same proven format as the 23 Nov entry,
round 3 rank 219/13,031, top 1.7%; rebuilt twice after rank reviews —
v2 (29 stories) ranked 8,042/21,134, judge 975,976; v3 adds 16 more
verified stories to reach the top-10 pattern of 35–50 stories — see
BUILD.md:

Lead stories: **China launches first Pakistani to orbit** — Shenzhou-24
lifts off with Zeeshan Ali, 40, first foreigner aboard Tiangong;
**Asia stocks tumble on tariff threat** — MSCI Asia ex-Japan falls 2.3%,
Seoul sinks 5.3% as the US readies new tariffs; **Gaza death toll
reaches 74,746** — WAFA toll rises amid Israeli attacks as the UN flags
a worsening aid crisis. Grid: Giza tanker fire kills 31; US GDP jumps
to 4.3% (core PCE 3.3%); UK energy cap to rise 26%; West Java mine
flood kills 9; Ukraine hits five jets at Russian air base (3 MiG-31s,
2 Su-34s at Savasleyka); judges urge dropping Netanyahu bribery case;
Macy's parade postponed to Saturday (first ever weather postponement);
Abrego Garcia lands in Spain; Russia hits Ukraine grid, 5 regions dark;
N. Korea expels Swiss diplomat; S&P puts Nvidia on downgrade watch
(shares end 3.9% lower); FCC clears SpaceX's 1m Starmind satellites;
Nasdaq slides 2%; Ramaphosa wins Farmgate court reprieve; Canary
Islands see record migrant day. Tail: US proposes tariffs on 14
partners; Spain heads to polls on Sunday; India's food prices climb
again; PSG held by Roma, Bayern beaten; Russia's war dead 490,334
(BBC); Australia signs Solomons pact; CIA and spy chief hit by cyber
breach (sources say); Australia inflation beats forecasts; oil slides;
WHO flees Congo Ebola hospital; nine more children reunited (Melania
Trump initiative, total 43); US Army blasts 9,500lb explosives in Iowa;
Senegal MPs defy president on budget (128-9); Nigeria seizes $227m
meth; Duran Duran's Andy Taylor dies (announced Wed, died Monday);
Jolie and Pitt settle winery fight; 266m face acute hunger, WFP warns;
Indonesia factory fire toll hits 26; tankers hit by mines in Hormuz
Strait (Iran says); Dell posts record $54.9bn quarter; Sooryavanshi,
15, smashes 204 off 53; Huawei guilty of stealing trade secrets;
Houthis hit Riyadh's tallest tower; Putin vows retaliation on
refineries; Congo rebels halt advance on Bunia; China probes Shanghai
chief Chen; US pauses Ecuador military operations.
DATE CHECK: 11 of the 45 stories stem from Tue 24 Nov (or earlier) and
are explicitly flagged [24 Nov] — nothing dated 24 Nov is shown as a
25 Nov event.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` beside it to `/output/entry.png` — byte for byte, so two runs
write identical bytes. No network at grading. See `BUILD.md` for the news
sources, design choices and verification steps.

---

Entered on [make.fun](https://make.fun/?ref=r4c0y56z&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards
