---
title: Commissioning: First Fill to Sign-Off
date: 2026-08-10
tag: Installations
description: The sequence for bringing a machine up safely, the numbers to set, and the baseline document that makes every future service call answerable.
---

Commissioning is not "switch it on and pull a shot". It is a sequence with a safety-critical order, a set of numbers to establish, and a document to leave behind.

That document is the part most often skipped, and it is the part that pays off for the next ten years. Without a recorded baseline, every future diagnostic question — has the pump always been at 8.5 bar? was the flow rate always this slow? — is unanswerable.

## The order matters

Water before power. Always.

1. **Water on, machine cold, no power.** Open the supply and check every joint for leaks at static pressure. Cold and unpowered is when a leak is harmless.
2. **Fill the boilers.** Manual fill valve where fitted; otherwise let the autofill run. On the steam boiler, open a steam valve during filling so displaced air can escape — a boiler filled against trapped air will not fill properly and the level reading lies.
3. **Confirm water is actually in the boiler.** Sight glass, or run the hot water tap until it flows steadily. Do not accept the level probe's word for it yet.
4. **Now energise the heating.** Not before.
5. **Bring up to pressure and watch it.** Stay with the machine through the first heat cycle.
6. **Re-check every joint hot.** Fittings move with thermal expansion, and joints that were dry cold will weep at temperature. This second check catches most first-week leaks.

## The numbers to set

Work to the manufacturer's figures where they specify them; the ranges below are typical starting points.

| Parameter | Typical target | How to verify |
| --- | --- | --- |
| Steam boiler pressure | 1.0–1.3 bar | Machine gauge, cross-checked if possible |
| Brew temperature | 92–95 °C | Machine readout, ideally confirmed at the group |
| Pump pressure | ~9 bar | Portafilter gauge, **while water is flowing** |
| Group flow rate | Per manufacturer | Timed volume with no basket |
| Volumetric doses | Per recipe | Scales, at the cup |

Two details that cause most of the errors here.

**Pump pressure must be set under flow.** A static reading with the group blocked and no flow is not the pressure the puck sees. Use a portafilter gauge and set it with water moving.

**Brew temperature on the readout is not brew temperature at the puck.** The displayed figure is wherever the probe sits, and the offset between that and the water hitting the coffee is machine-specific and sometimes several degrees. If you have the means to measure at the group, do it and record the offset — that single number saves hours of future argument about whether the machine is running hot.

## Verify the safety systems, do not assume them

These are the checks that separate a commissioning from a switch-on. Each one is testing a device whose entire purpose is to prevent an expensive or dangerous failure, and none of them has ever been tested on this machine on this site.

- **Autofill cut-off.** Watch a full fill cycle and confirm it stops at the correct level rather than continuing to fill.
- **Autofill timeout.** Most machines cut the fill after a set period to protect against a failed probe or lost water supply. Confirm the machine has one and, where it can be tested safely, that it works.
- **Pressure relief valve.** Free, not seized, correctly rated, and discharging somewhere safe.
- **Element protection.** Confirm the machine's low-water or thermal protection exists and is connected — not bypassed by a previous installer, which happens more often than it should.
- **Electrical protection.** Confirm the machine sits on its own RCBO and that it holds through a full warm-up with elements cycling.

## Confirm the water, at the machine

The treatment was specified from a source-water test. Now verify the output, at the machine inlet, after flushing the cartridge for its full run-in volume.

Titrate alkalinity and hardness, check chlorine reads zero, and confirm the numbers land in the target range. A blend valve set by eye is not a treatment specification — it is a guess that happens to be adjustable.

Record the readings. This is the baseline against which a future scale problem gets diagnosed.

## The baseline document

Leave this with the client and keep a copy. It is the single most useful artefact from the whole installation.

- Machine model, serial, build date; same for each grinder.
- Supply voltage measured at the machine, under load.
- Static and flowing water pressure at the inlet.
- Source water and treated water test results, with the date.
- Filter model, cartridge model, install date, and rated volume.
- Steam pressure, brew temperature setting, and the measured group offset if taken.
- Pump pressure under flow.
- Group flow rates, per group.
- Volumetric dose settings, per group.
- Grinder dose consistency: ten weighed doses and the spread.
- Ambient temperature behind the bar and at the grinder intake.
- Photographs: data plates, the under-counter void, the filter head, the air gap.

Ten minutes of writing. It converts every future service visit from archaeology into comparison.

## Hand over to humans

The machine is commissioned when the staff can run it, not when it makes coffee.

Walk the team through the daily open and close routine, and do the first backflush *with* them rather than describing it. Show them the filter cartridge and when it is due. Show them the isolation valves for water and power, and be explicit about what to do in a leak.

Then be clear about escalation. The three things that mean "stop and call", not "keep going and mention it later":

1. A breaker or RCD that trips.
2. Any steam or water escaping from somewhere it should not.
3. A pressure gauge reading outside its normal band.

Everything else can wait for a scheduled visit. Those three cannot, and a team that knows the difference will call you at the right time instead of after the damage.

## Then come back

Book a two-week follow-up as part of the installation, not as a separate sale. Thermal cycling settles fittings, the team's habits become visible, and the first genuine faults surface in the first fortnight.

It is also when the baseline gets its first comparison, which is when it starts earning its keep.
