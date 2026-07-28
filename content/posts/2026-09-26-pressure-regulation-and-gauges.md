---
title: Pressure Regulation and Gauges
date: 2026-09-26
tag: Water
description: Machines specify an inlet pressure range for good reasons. Static and dynamic pressure differ, mains pressure rises overnight, and a wrong gauge invalidates every judgement you make.
---

Inlet pressure is a specification, not a characteristic of the building. Most manufacturers want something in the region of 2–4 bar at the machine and cap it around 6, and both ends of that range matter.

## Both ends have consequences

**Too low** starves the pump. A rotary pump that cannot get water in as fast as it is pushing it out cavitates, and cavitation destroys pumps from the inside. Low inlet pressure also slows autofill, so the boiler struggles to recover during a rush.

**Too high** stresses every fitting and joint continuously, accelerates weeping at unions, and can interfere with how the pump's bypass behaves. It also makes water hammer worse, which is tomorrow's post.

## Static and dynamic are different numbers

Measure both. They can differ substantially and they tell you different things.

**Static pressure** is with nothing flowing. It is the highest pressure the system sees, and it is what fittings and the expansion vessel precharge relate to.

**Dynamic pressure** is measured while water is flowing at a realistic rate. It is lower — sometimes much lower — because of losses through the supply, the meter, the isolation valves and the filter train.

The failure mode this exposes: a supply with perfectly good static pressure that collapses under flow because of an undersized service pipe or a loaded prefilter. Static reads 4 bar, and at peak draw the machine is seeing 1.2 bar and the pump is starving.

**So the number that matters is dynamic pressure at the machine inlet, at peak flow.** A static reading alone can look fine on a supply that cannot deliver.

## Overnight pressure rise

The detail that explains a specific and puzzling category of fault.

Mains pressure is a function of network demand. When demand falls overnight, **pressure often rises significantly** — sometimes by a couple of bar. A system comfortable at 4 bar at ten in the morning can be at 6 bar at three in the morning.

Consequences:

- **Leaks that only appear overnight**, found as a wet floor at open with everything dry by mid-morning.
- **Fittings weeping intermittently** and never when you are there.
- **Expansion vessel precharge set to daytime static** being wrong at night.

If a client reports finding water in the morning and nothing during the day, measure overnight pressure — a gauge with a maximum-reading pointer, left in place, answers it. Then regulate.

This is also the case for fitting a regulator even where daytime pressure looks acceptable.

## Regulators

A pressure reducing valve, direct-acting, fitted after the isolation valve and before the treatment train.

- **Set it to the middle of the machine's specified range**, not the top. Mid-range gives headroom in both directions.
- **Set it under flow**, then confirm static afterwards. A regulator adjusted with no flow will read differently in service.
- **Check it holds** — regulators drift and their seats wear. A regulator that has stopped regulating is invisible without a gauge.
- **Size it for the flow**, not just the pressure. An undersized regulator becomes a restriction at peak draw and creates the dynamic pressure problem it was meant to prevent.
- Combined regulator-and-gauge units are convenient and reduce fittings.

## Gauges

The instruments everything else depends on. A wrong gauge means every judgement made from it is wrong.

**Where to fit:**

- **Before the filter train** — supply pressure.
- **After the filter train**, at the machine inlet — what the machine actually receives. The differential between these two is your cartridge-loading indicator.
- Optionally one with a **maximum-reading pointer**, to capture overnight peaks.

**Choosing:** a range with normal operating pressure around mid-scale, glycerine-filled if the location vibrates, and a size and position you can read without a torch or dismantling a panel. A gauge nobody can read gets ignored.

**Checking:**

- **Zero when depressurised.** A gauge that does not return to zero is reading offset across its whole range. This is the single most useful gauge check and it takes seconds.
- **Cross-check against a known gauge** — the portafilter gauge you use for brew pressure works.
- **Replace** anything fogged, sticking, or with a bent pointer. They cost very little.

> A gauge that does not read zero at rest is reading wrong everywhere. Check it at every service — it is a five-second test that validates every pressure number in the log.

## At commissioning

Record all of these in the baseline:

1. Static pressure at the machine inlet.
2. Dynamic pressure at the machine inlet, at peak simultaneous draw.
3. Regulator setting.
4. Differential across the filter train, clean, at peak flow.
5. Overnight static, if the site history suggests it matters.

Then re-measure at every service. A dynamic pressure that has fallen since commissioning is a loading filter or a failing regulator, and it is the earliest available warning of a pump about to be starved.
