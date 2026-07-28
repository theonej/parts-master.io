---
title: Sizing a Filter for Peak Flow
date: 2026-09-18
tag: Water
description: Capacity and flow rate are two independent specifications. Getting the second one wrong gives you a system that works at 10 a.m. and fails at 8:30.
---

Filter datasheets give two numbers that get treated as one. Capacity, in litres, tells you how often to change the cartridge. Flow rate, in litres per minute, tells you whether it works at all when the bar is busy.

Bars are sized on capacity almost universally, because that is the number salespeople lead with.

## What undersized flow actually does

Three consequences, all of which present as something else.

**Pressure drop, and a starved pump.** Pressure drop across a cartridge rises steeply with flow. At peak draw an undersized filter can pull the machine's inlet pressure below its specification, so brew pressure falls. Worse, a starved rotary pump cavitates, and cavitation destroys pumps from the inside.

The signature is unmistakable once you know it: **brew pressure fine when the bar is quiet, low during the rush.** That gets diagnosed as a failing pump, and a new pump behaves identically.

**Reduced contact time, and chlorine breakthrough.** Chlorine and especially chloramine removal depends on time in the media. Halve the contact time and removal falls. A bar whose water tastes clean mid-afternoon and faintly of chlorine at 8:30 a.m. has a flow problem, not a media problem.

**Reduced dealkalisation.** Ion exchange is also rate-dependent. At high flow, treated output alkalinity rises.

All three appear only at peak. That is why they are hard to diagnose on a quiet-morning service visit, and why the number needs to be right at design time.

## Calculating peak simultaneous demand

Add everything that can draw at once, not average consumption. The morning rush is the design case.

| Draw | Typical rate |
| --- | --- |
| Espresso group, extracting | 0.15–0.25 L/min each |
| Steam boiler autofill, refilling | 0.5–1.5 L/min |
| Hot water tap, running | 2–4 L/min |
| Batch brewer, filling | 1–3 L/min |
| Ice machine, filling | 0.5–1.5 L/min |

The hot water tap dominates, and it is the one people forget. A three-group bar with two shots running, an autofill cycle and someone drawing 2 litres for an Americano is well over 3 L/min instantaneously.

Worked example for a three-group bar with a batch brewer:

- Two groups extracting: 0.4 L/min
- Autofill: 1.0 L/min
- Hot water tap: 3.0 L/min
- Batch brewer filling: 2.0 L/min

**Peak simultaneous: 6.4 L/min.** A cartridge rated 4 L/min is undersized, whatever its capacity.

Judgement applies — not everything peaks together every minute. But the batch brewer filling while someone draws hot water during a rush is an ordinary Tuesday, not a worst case.

> Cartridge capacity sets the change interval. Cartridge flow rating sets whether the system works at 8:30 a.m. Size on flow, then check capacity.

## Pressure drop stacks

Each stage in the train contributes. Sediment, carbon and dealkalisation cartridges each drop pressure, and it adds up — then rises further as the sediment stage loads.

So the check is: **static line pressure, minus total pressure drop across the loaded train, at peak flow, must still exceed the machine's minimum inlet pressure.**

Carbon block filters drop noticeably more than granular beds. Fit three block stages in series on a marginal supply and you can be below the machine's requirement before anything is dirty.

Datasheets usually quote flow at a specified pressure drop. Read the conditions, not just the number.

## The fix is parallel, not bigger

When flow is the constraint, the instinct is a larger cartridge. Often the right answer is **two cartridges in parallel** on a twin manifold.

Parallel gives you:

- **Double the flow capability**, because each cartridge sees half the flow.
- **Double the volumetric capacity**, so a longer change interval.
- **Better contact time at peak**, because the flow through each is halved — which directly addresses chlorine breakthrough and dealkalisation performance.
- **A degree of redundancy**, and the ability to change one at a time on some manifolds.

The cost is a manifold and a second cartridge, which is modest against the alternative of chronic peak-time problems. Parallel manifolds are standard on any bar with a hot water tap and a brewer, and they are under-specified constantly.

Note also that if the **filter head** is the restriction rather than the media, a bigger cartridge in the same head changes nothing. Check the head's rated flow too.

## Measure it at commissioning

Do not leave this as a calculation.

1. Record static inlet pressure at the machine.
2. Open the largest draws you can simultaneously — hot water tap plus a group plus the brewer.
3. Record inlet pressure **under that load**. Compare against the machine's minimum.
4. Record the differential across the filter train while flowing.
5. Titrate the treated water at peak flow, not at a trickle. Same discipline as remineralisation.
6. Put all of it in the baseline.

Step five catches the contact-time problem that a quiet-tap sample hides completely.

## The retrofit case

On an existing bar reporting rush-only pressure problems, work in this order before touching the pump:

1. Age and volume of the sediment cartridge.
2. Age and volume of the carbon and dealkalisation cartridges.
3. Differential pressure across the train at peak flow.
4. Rated flow of the cartridges and the head against calculated peak demand.
5. Static and flowing line pressure at the inlet.

Most of the time the answer is a loaded cartridge, and the fix is a change plus a schedule. Sometimes the answer is that the system was never sized for the flow, and the fix is a parallel manifold.
