---
title: Water Is the Install: Specifying Treatment for a High-End Espresso Bar
date: 2026-07-27
tag: Installations
description: Why alkalinity matters more than TDS, why a softener and straight RO are both the wrong answer, and the treatment I actually specify on a build.
---

When a three-group machine comes into the shop with a split heat exchanger or a heating element burned open, the invoice says *element* or *exchanger*. The cause was decided years earlier, on the day someone plumbed the machine into whatever came out of the wall through a $40 carbon block.

Treatment is the cheapest line item on a high-end bar build and the one that determines whether the machine reaches year ten. It deserves more than an afterthought at the end of the plumbing walkthrough.

## The TDS meter is the most over-trusted tool in the industry

Everyone owns a TDS pen. It gives one number, instantly, and that number feels like an answer. It isn't. A conductivity meter estimates the *total* dissolved solids and tells you nothing about *which* solids.

Two waters can both read 150 ppm and behave like completely different liquids. One is mostly calcium bicarbonate: it will scale your boiler and flatten every espresso you pull. The other is mostly sodium chloride: it will not scale at all, and it will quietly pit your stainless steel. Same reading on the pen. Opposite problems.

> **The number that actually matters is alkalinity**, and a TDS pen cannot measure it. You need a titration — a drop-count carbonate hardness kit is fine and costs about the price of a bag of beans.

## The four numbers I test for

### Total alkalinity (as CaCO₃)

This is the bicarbonate content, and it does double duty as the villain. Bicarbonate is what actually precipitates when you heat water: calcium bicarbonate breaks down into calcium carbonate, CO₂ and water, and the carbonate plates out onto the hottest surface it can find. That is your element or exchanger wall. This is why "temporary" hardness, not total hardness, drives scale.

Alkalinity also buffers acid. Coffee is acidic, and that acidity is most of what you taste as brightness, sweetness and fruit. High alkalinity neutralises it in the cup: the espresso goes flat, dull and slightly chalky, and no amount of recipe work rescues it. Baristas chase that fault around the grinder for weeks. It is in the water line.

### Calcium hardness

You need some. Calcium and magnesium bind to flavour compounds during extraction and are part of how the cup gets body. Strip hardness to zero and you get thin, hollow, papery espresso. Hardness is a target to hit, not a number to minimise.

### Chloride

The one nobody tests and the one that ends warranties. Chloride attacks the passive layer on stainless steel and causes pitting corrosion — small, deep, localised holes rather than general rusting. Keep it under 30 mg/L. Treat anything over 50 mg/L as an active threat, and note that it is not removed by a softener or a carbon block.

### Chlorine and chloramine

Both must reach the machine at zero, for taste and for elastomer life. These are not interchangeable problems. Free chlorine comes out on standard granular carbon easily. Chloramine does not — it needs *catalytic* carbon and meaningfully longer contact time. Plenty of bars have a carbon filter fitted, a chloraminated municipal supply, and a persistent swimming-pool note nobody can place.

## Targets

The SCA brewing standard is the reference point. For espresso I pull alkalinity and hardness toward the low end of acceptable, because a pressurised boiler running above 120 °C is far less forgiving of scale than a batch brewer.

| Parameter | SCA target | What I specify for espresso |
| --- | --- | --- |
| Total alkalinity | 40 mg/L | 30–50 mg/L as CaCO₃ |
| Calcium hardness | 68 mg/L (4 gr) | 50–75 mg/L as CaCO₃ |
| TDS | 150 mg/L | 110–160 mg/L |
| pH | 7.0 | 6.8–7.5 |
| Chloride | — | ≤ 30 mg/L |
| Total chlorine | 0 mg/L | 0 mg/L |
| Sodium | 10 mg/L | ≤ 30 mg/L |

Useful conversion when you are reading a plumber's report or an American filter datasheet: one grain per gallon is 17.1 mg/L as CaCO₃.

## The two common fixes, and why both are wrong

### A water softener

Standard ion-exchange softening trades calcium and magnesium for sodium. It does stop scale, which is why plumbers reach for it. But it leaves alkalinity completely untouched — you have swapped a scale problem for high-sodium, high-alkalinity water. The buffering that flattens your espresso is still there, now with a salty edge and no calcium to give the cup body. It is the worst-tasting water in professional coffee.

### Straight reverse osmosis

The overcorrection. RO permeate is close to pure, and pure water is *aggressive*. With almost no dissolved mineral it has nothing to be in equilibrium with, so it leaches metal from brass fittings and copper pipe, and with no alkalinity it has no buffer, so pH wanders. It also makes hollow, lifeless espresso.

> Never plumb a machine to unblended RO. If RO is the right tool, the deliverable is **RO plus a controlled blend or remineralisation stage** — and a blend valve someone will actually verify with a test kit, not set once and forget.

## What I actually specify

Test the water first, then choose. Roughly:

- **Moderate alkalinity, decent source water.** Catalytic carbon plus a weak-acid cation cartridge — the BWT bestmax, Everpure Claris and Brita Purity families are all this. Unlike a softener, WAC resin genuinely removes alkalinity: it releases H⁺, which converts bicarbonate to CO₂. Set the bypass to land on target, then confirm by titration.
- **High alkalinity, high chloride, or anything unpleasant.** RO with a blend or remineralisation stage. More capital, more servicing, total control over the final water. On coastal or heavily treated supplies this is the only honest answer.
- **Already near target.** Catalytic carbon for chlorine, sediment protection, and leave the chemistry alone. Do not treat water that does not need treating.

## The install details people skip

- **Size the filter on peak flow, not just capacity.** A cartridge rated for the right volume can still starve a busy bar during a morning rush if its flow rating is below your simultaneous draw. Add the espresso machine, the brewer and the hot tap together.
- **Check static line pressure and regulate it.** Most manufacturers want roughly 2–4 bar at the inlet and cap it around 6. Fit a regulator and a gauge you can read without pulling a panel.
- **Give thermal expansion somewhere to go.** A check valve or backflow preventer on the inlet turns the machine into a closed system, and heating a closed system spikes pressure hard enough to weep valves and fatigue fittings. A small expansion vessel on the treated line solves it permanently.
- **Backflow prevention to local code.** Not optional, and an inspector will find it.
- **Isolation valve and cartridge clearance.** Whoever changes the filter should not need to move the machine. If the change is awkward it will be skipped, and a spent cartridge is worse than none.
- **Label the install and log the numbers.** Source reading, treated reading, cartridge model, date, and the volume the cartridge is rated for, on a tag at the filter head.

## Commissioning checklist

1. Test at the tap the machine will actually connect to — not the municipal annual report, which is an average taken well upstream of the building's plumbing.
2. Flush the new cartridge for the full volume in its instructions.
3. Titrate the treated water at the machine inlet. Alkalinity, hardness, chlorine. Confirm you hit the target rather than assuming the bypass setting was right.
4. Verify static and flowing pressure at the inlet.
5. Set a cartridge change interval from measured volume, and put it in a calendar with an owner's name on it.
6. Book a hardness re-test in six months. Municipal supplies drift seasonally, and blended sources can shift a long way.

## Prevention is the whole strategy

Once carbonate has plated onto an element or an exchanger wall, there is no clean recovery. Chemically descaling a modern machine in place tends to loosen scale into valves and gicleurs where it jams things, and the acid is hard on gaskets and any aluminium in the circuit. On a high-end machine, descaling is a salvage operation, not maintenance.

Worth saying plainly to owners: scale damage is obvious to anyone who opens the machine, and manufacturers routinely decline warranty claims on it. A treatment package is a fraction of one heat exchanger. That is usually the argument that lands.

Get the water right and the rest of the bar — grinder, workflow, routine — is a conversation about craft. Get it wrong and you spend the next five years troubleshooting a cup that was never going to taste good.
