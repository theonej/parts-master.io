---
title: Chloride and Pitting Corrosion
date: 2026-09-07
tag: Water
description: The ion nobody tests, which no cartridge removes, and which drills holes through stainless steel from the inside. Where it comes from and what to do about it.
---

Everyone testing water for a coffee bar measures hardness. Most measure alkalinity. Almost nobody measures chloride, and it is the one that produces a hole in a boiler.

It is also the parameter you cannot fix with the cartridge you were going to fit anyway, which is why it needs to be established before the treatment decision rather than after.

## Why stainless steel is vulnerable

Stainless steel does not resist corrosion by being inert. It resists corrosion because chromium in the alloy forms an extremely thin, self-repairing oxide layer on the surface — the passive layer. That film is what makes stainless stainless.

Chloride ions attack that film locally. They break it down at small discrete points, and once the film is broken at a point, that point corrodes while the surrounding passivated metal does not.

The result is **pitting**: small, deep, localised penetrations rather than general surface rusting. And pitting is far more dangerous than general corrosion, because:

- It concentrates all the damage in a tiny area, so it penetrates fast.
- It is nearly invisible. A pit can be a fraction of a millimetre across and go most of the way through the wall.
- Once started, a pit is self-sustaining. The chemistry inside it becomes more aggressive than the bulk water, so it accelerates.

You do not get a warning. You get a machine that was fine and is now weeping from somewhere that cannot be repaired.

## Heat and concentration make it worse

Two things in an espresso machine make chloride attack more aggressive than the same water would be in a cold pipe.

**Temperature.** Pitting susceptibility rises sharply with temperature. A chloride level that is harmless in a cold water main is meaningfully aggressive at 125 °C.

**Concentration by evaporation.** In a steam boiler, water leaves as steam and dissolved solids stay behind. Over time chloride concentrates in the boiler water above the level in the supply. A boiler that is topped up and drawn off continuously reaches a steady state above the inlet concentration, and one that is rarely drained concentrates further.

That second mechanism is why a supply at a "moderate" chloride level can still produce trouble in a machine that is never drained.

> Chloride in the supply is not chloride in the boiler. Evaporation concentrates it. This is a reason to drain and refresh steam boilers periodically on high-chloride supplies, and a reason to treat borderline readings as worse than they look.

## Where it comes from

- **Coastal supplies** and any aquifer with saline intrusion.
- **Road salt** in winter, affecting shallow groundwater and surface sources. This is seasonal, which means a single test in July can miss it.
- **Ion exchange softeners.** They regenerate with sodium chloride brine, and an incompletely rinsed regeneration cycle puts chloride into the treated water. A building softener can therefore *raise* chloride while lowering hardness.
- **Some disinfection by-products** and treatment chemicals.
- **Water treatment using hydrochloric acid** for pH correction.

The softener case deserves emphasis, because it is the one where treatment causes the problem. A bar in a hard-water area on a building softener can have near-zero hardness, high sodium and elevated chloride — the worst combination available for both taste and boiler life.

## The numbers

- **Keep chloride below 30 mg/L.** This is the working target.
- **Above 50 mg/L, treat as an active threat** to a stainless boiler at temperature.
- **Check the manufacturer's specification**, because many state their own chloride limit, and that figure is a warranty condition.

## Nothing simple removes it

This is the crux. Chloride is a small, highly soluble anion and it passes straight through the treatment most bars fit:

- **Carbon filtration** — no effect. Carbon adsorbs organics and chlorine, not chloride.
- **Sediment filtration** — no effect.
- **Ion exchange softening** — no effect on chloride, and may add it.
- **Weak acid cation dealkalisation** — no effect. It addresses bicarbonate.

What does work:

- **Reverse osmosis.** The membrane rejects chloride effectively. Then blend or remineralise to bring hardness and alkalinity back to target. On a high-chloride supply this is the answer, and it is the main reason RO gets specified on a coffee bar.
- **Anion exchange**, in specialist applications. Rarely the practical choice for a café.

## What this means for specification order

Chloride has to be established *first*, because it determines the whole architecture:

1. Get chloride from a lab analysis at specification time. It cannot be measured with a field kit.
2. **If chloride is low**, you are choosing between carbon plus a dealkalising cartridge and doing nothing much. A straightforward decision.
3. **If chloride is high**, cartridge treatment cannot solve it regardless of how good the cartridge is. You are specifying RO with a blend, at a different capital cost and with a different service regime.

Discovering that after you have quoted a cartridge system is an awkward conversation. Discovering it after a boiler has pitted is a much worse one — and because pitting damage is diagnosable, it is a warranty claim that will be declined on water quality grounds.

## On existing machines

If you inherit a machine on a coastal or high-chloride supply with no RO, two things are worth doing: get the chloride figure, and drain the steam boiler periodically to stop concentration building. Neither fixes the specification, but both buy time while the client decides whether to fund the plant that will.
