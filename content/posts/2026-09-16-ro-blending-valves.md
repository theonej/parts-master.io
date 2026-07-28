---
title: "RO Blending Valves: Setting and Verifying"
date: 2026-09-16
tag: Water
description: The arithmetic for setting a blend, why blending defeats the purpose on high-chloride water, and why a valve set once at commissioning drifts off target.
---

RO permeate needs mineral put back. The cheap way is to blend a controlled proportion of untreated feed water back into it. It works well, and it fails in one specific case that people miss.

## The arithmetic

Permeate is close to zero for practical purposes, so the blended output is essentially the feed water diluted by the blend fraction:

**output ≈ feed concentration × blend fraction**

Rearranged, the fraction you need is:

**blend fraction ≈ target ÷ feed**

Worked: feed alkalinity 200 mg/L, target 40 mg/L.

**40 ÷ 200 = 0.2** — so roughly 20% feed water blended into 80% permeate.

Check the other parameter with the same fraction. If feed calcium hardness is 250 mg/L, then 20% blend gives 50 mg/L — comfortably in the 50–75 target. Both land, so a single blend setting works.

Sometimes they do not both land. If the feed's hardness-to-alkalinity ratio is wrong for your two targets, no single blend fraction satisfies both, and you have to choose. Prioritise **alkalinity**, because it drives scale and buffering, then add hardness separately by remineralisation if the cup needs it.

## The failure case: chloride

This is the point worth taking away.

Blending brings back **everything** in the feed water proportionally — including the chloride and silica the membrane just removed.

Feed at 120 mg/L chloride, blended at 20%, gives 24 mg/L chloride in the output. That happens to be under the 30 mg/L target, so it works. But feed at 250 mg/L chloride blended at 20% gives 50 mg/L, which is squarely in pitting-risk territory — and you have installed an RO plant and still have a chloride problem.

> If you specified RO **because** of chloride or silica, do not blend. Blending reintroduces the exact parameter you bought the membrane to remove. Remineralise instead.

That is the decision rule. Blend when RO was chosen for high alkalinity or general poor quality. Remineralise when it was chosen for chloride or silica.

Always run the chloride number through the blend fraction before settling on a design. It takes ten seconds and it catches a design error that would otherwise be discovered by a pitted boiler.

## Valve types

**Needle valve.** Adjustable, infinitely variable, and prone to being nudged. Mark the position.

**Calibrated orifice or fixed restrictor.** Set at design, not field-adjustable. More stable, less flexible when feed water changes seasonally.

**Motorised or automatic blending.** Found on larger systems, sometimes with conductivity feedback. Self-correcting, more to fail.

For a café, a needle valve with a marked and recorded position is normal. The discipline is in the verification, not the hardware.

## Setting it properly

1. **Measure the feed** — alkalinity, hardness, and know the chloride from the lab analysis.
2. **Measure the permeate** so you are not assuming it is zero. A declining membrane raises permeate concentration and shifts the whole calculation.
3. **Calculate the fraction** from the target and the feed.
4. **Set the valve** approximately, and run water for long enough that the output is genuinely mixed.
5. **Titrate the blended output at the machine inlet.** Not at the valve, not at the tank — at the point the machine draws from, downstream of every tee and length of pipe.
6. **Adjust and re-titrate.** Two or three iterations is normal.
7. **Mark the valve position** physically and **record it** in the water log with the readings that produced it.

Step five is where most installations go wrong. A sample taken at the blend tee has not fully mixed, and reads differently from what the machine receives.

## Why it drifts

A blend set correctly at commissioning does not stay correct, for four reasons:

**Feed water changes seasonally.** The fraction was calculated from one feed measurement. When feed alkalinity rises in late summer, the same valve position delivers higher output alkalinity.

**Membrane performance declines.** As rejection falls, permeate carries more dissolved solids, so the blended output rises even with the valve untouched.

**The valve moves.** Vibration, someone working in the cabinet, a cleaner. Needle valves are not locked.

**Prefilter loading changes the pressure balance.** In some plumbing arrangements the blend fraction is pressure-dependent, so a loading prefilter shifts the ratio.

All four are invisible without measurement. A machine can be scaling steadily on a system that was perfectly set two summers ago.

## Put it in the service routine

At every service visit:

- Titrate the blended output at the machine inlet. Alkalinity and hardness.
- Compare against the recorded commissioning figures.
- Check the valve is still on its mark.
- Measure feed and permeate conductivity for the rejection rate.
- Re-set and re-record if it has moved.

Five minutes. It is the difference between an RO plant that protects a machine and an expensive installation quietly delivering the wrong water.

## The honest summary

Blending is the simple, cheap, reliable way to bring permeate back to target — provided the feed water's problem was quantity rather than a specific ion. Run the chloride arithmetic first, verify by titration at the machine, and re-check it every visit because it moves on its own.
