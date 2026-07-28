---
title: Sediment Prefiltration and Micron Ratings
date: 2026-09-11
tag: Water
description: Nominal ratings are marketing, absolute ratings are a specification. Sizing the first stage to protect everything behind it without starving the pump.
---

The cheapest stage in the treatment train, protecting the most expensive components behind it. It is also the stage most likely to be forgotten in a service schedule, because nothing dramatic happens when it loads up — brew pressure just quietly falls.

## What it is protecting

- **Carbon media**, from being blinded by particulates that occupy the surface without being adsorbed.
- **Ion exchange resin**, from fouling.
- **RO membranes**, which are the expensive case — particulate fouling shortens membrane life directly.
- **Small orifices** in the machine: gicleurs, solenoid seats, flowmeters.
- **The pump.** A blocked prefilter starves the inlet, and a starved rotary pump cavitates, which destroys it from the inside.

That last one is worth emphasising because the causal chain is long enough that people miss it. A neglected sediment cartridge eventually costs a pump.

## Nominal versus absolute

The single most misleading number in filtration.

**Nominal rating** means the filter removes some percentage of particles at that size — often 60–85%. A "5 micron nominal" filter passes a significant fraction of 5 micron particles.

**Absolute rating** means it removes essentially all of them, conventionally around 99.9%.

Marketing uses nominal, because the number looks better. A nominal 1 micron and an absolute 1 micron filter are not comparable products.

For most café applications nominal is adequate and cheaper. Where it matters — ahead of an RO membrane — specify absolute, and ask which is quoted if the datasheet does not say.

## Depth versus surface

**Depth filters** — spun or melt-blown polypropylene — trap particles throughout their thickness. They hold far more dirt before blinding, and they are the usual choice for a first stage. Graded-density versions are coarser on the outside and finer inside, which spreads loading through the depth and extends life further.

**Pleated (surface) filters** capture on the surface. Larger surface area for a given housing, lower pressure drop when clean, and some are washable. They blind faster on dirty water because everything accumulates in one plane.

For a coffee bar on municipal supply, a graded-density depth cartridge is the sensible default.

## Sizing

**Do not over-filter.** A 1 micron prefilter on clean municipal water gives you frequent changes, unnecessary pressure drop and no benefit. Over-filtering is a real and common error.

Typical arrangements:

| Situation | Prefiltration |
| --- | --- |
| Clean municipal supply, cartridge system | Single 5 micron depth, or rely on the carbon block's own rating |
| Visible particulate, older mains, well water | 20 micron then 5 micron |
| Ahead of an RO membrane | 5 micron then 1 micron absolute |

Size the housing on **flow rate** first. Pressure drop rises steeply as a cartridge loads, so a stage that is marginal when clean becomes a restriction within weeks.

## Monitor it with pressure, not a calendar

The best indicator of a loading prefilter is differential pressure across it.

Fit gauges before and after — or at minimum before the filter and at the machine inlet — and record the clean differential at commissioning. When the differential has roughly doubled, the cartridge is due regardless of what the calendar says.

Without gauges you are guessing, and the guess is always optimistic. The symptom you will get instead is **brew pressure falling during the rush only**, because that is when flow is highest and pressure drop worst. That symptom gets blamed on the pump.

> A pressure gauge either side of the prefilter costs very little and converts sediment changes from a calendar guess into a measurement. On any site with an RO plant, treat it as mandatory.

## Housings

- **Clear housings** let you see the cartridge, which is genuinely useful. They also admit light, which grows algae — so keep them out of direct light or accept the trade.
- **Opaque housings** avoid that and require you to rely on differential pressure.
- **Pressure rating** must exceed maximum line pressure, including any overnight rise.
- **A housing spanner**, kept with the machine. Housings tighten in service and the spanner is always somewhere else.
- **Clearance below** to drop the sump without dismantling anything — the same serviceability point as the filter head.

Fit an isolation valve upstream and a drain or flush point so a cartridge change does not flood the counter void.

## In the routine

- Record clean differential pressure at commissioning.
- Read the differential monthly, on the same sheet as the water meter.
- Change on differential, with a calendar backstop of six to twelve months.
- Flush after changing, to drain, before water reaches the machine.
- Log it: date, cartridge type, differential before and after.

Sediment filtration is unglamorous and nobody notices it working. The measure of a good first stage is that the carbon behind it reaches its rated volume and the pump reaches its tenth year.
