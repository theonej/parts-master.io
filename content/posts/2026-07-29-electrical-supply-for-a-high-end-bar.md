---
title: Electrical: Sizing Supply for a Three-Group Bar
date: 2026-07-29
tag: Installations
description: Phase selection, circuit sizing, voltage drop and the nuisance-tripping problem nobody diagnoses correctly. Get this wrong at order time and it cannot be fixed later.
---

Water damage takes years to kill a machine. Bad electrical provision ruins an opening week.

The reason electrical deserves attention before anything else is that some of it is irreversible. Element voltage configuration is often set when the machine is built. If you order a three-phase machine for a single-phase site, you do not adjust it on installation day — you send it back.

## Establish the supply before you specify the machine

Not after. The order of operations matters, and it is routinely reversed because the machine is the exciting decision.

- **Phase and voltage at the panel**, confirmed by measurement and photograph, not by what the landlord remembers.
- **Main breaker rating and actual spare capacity.** Empty breaker ways are not the same as available load. Add up what is already connected.
- **Whether the machine's element configuration is factory-set.** Ask the distributor explicitly, in writing.

> The single most expensive electrical mistake in this trade is ordering the wrong element configuration, because it is discovered on installation day and the fix is a shipping delay.

## Rough loads

Nameplate figures vary a lot between manufacturers, but for planning:

| Machine | Typical total load |
| --- | --- |
| One group | 1.5–2.5 kW |
| Two group | 3–5 kW |
| Three group | 5–9 kW |
| Add a grinder | 0.5–1.5 kW each, low duty |

Those are heating loads and they are close to continuous during warm-up. Size the circuit for the nameplate, not for an average.

## Circuit sizing, worked

A 6 kW three-group machine:

- **230 V single phase:** roughly 26 A, so a 32 A dedicated circuit.
- **208 V single phase:** roughly 29 A, so a 40 A dedicated circuit.
- **208 V three phase:** roughly 17 A per leg, so a 20–25 A three-pole circuit.

The three-phase version needs materially less copper and puts a balanced load on the supply. On any bar with three-phase available and a machine of three groups or more, take it.

Always follow local code for derating, grouping and installation method. The numbers above are for sanity-checking a quote, not for sizing a cable.

## Dedicated means dedicated

The espresso machine gets its own circuit, with nothing else on it. So does each grinder, ideally.

This is not fussiness. The machine draws several kilowatts in hard on/off cycles as the element switches. Every cycle produces a small voltage dip on that circuit. Share it with grinder motors — which have their own inrush on start — and you get a supply that sags at exactly the moment the electronics are trying to hold a stable reading.

The symptom is a machine that occasionally resets, throws an implausible sensor fault, or drifts in temperature during a rush and behaves perfectly at 9 a.m. Everyone blames the control board. It is the circuit.

## Voltage drop is a real constraint

Fixed appliances want to see close to nominal voltage. Aim to keep drop within about 3% at full load over the whole run.

An undersized cable on a long run costs you element performance permanently: a machine at 5% low voltage heats measurably slower and never quite recovers during a rush, because heating power falls with the square of voltage. A 5% voltage drop is roughly a 10% power loss. Baristas experience that as "the machine can't keep up" and nobody thinks to measure voltage under load.

Measure at the machine terminals with the elements drawing, not at the panel at rest.

## Nuisance tripping, diagnosed properly

This is the fault I get called about most, and it is almost always misdiagnosed as a faulty machine.

Heating elements have a small standing insulation leakage to earth, and it rises as the element ages and absorbs moisture. A single machine might sit at a few milliamps. That is normal and harmless.

Now put the machine, two grinders, a fridge and a dishwasher behind one 30 mA RCD. Their leakage currents add. The device trips at 60–70% of its rating, so you are tripping at around 20 mA of combined leakage, and it happens on the morning everything switches on together.

The fix is not a bigger RCD. It is **separate protection per appliance**, so the machine's leakage is measured on its own. An individual RCBO per circuit solves it and also stops one appliance taking the whole bar down. Where regulations specify a device type sensitive to DC components, use it — inverter-driven equipment on the same board is a common complication.

If a machine trips its own dedicated device repeatedly, then you have a genuine fault: test the elements to earth cold and hot, because some only fail when hot and expanded.

## The details that get skipped

- **A local isolator the barista can reach.** Service work needs a lockable disconnect that does not involve a trip to the panel behind a locked door.
- **Earth bonding and continuity, verified and recorded.** On a plumbed metal-bodied appliance this is a safety item, not paperwork.
- **Labelled circuits.** "Coffee machine" on the panel schedule. It takes thirty seconds and saves a shift.
- **Certification handed over.** Test results, in writing, to the client.
- **Headroom for what comes next.** Bars add a second grinder, a batch brewer, a hot tap. Leave capacity.

## The handover conversation

Tell the client two things and their machine will outlive its warranty.

First, that the circuit is dedicated and must stay that way — the day someone plugs a heat gun into it, the problems start. Second, that if the machine starts tripping a breaker, the answer is a phone call, not resetting it repeatedly. A machine that trips is telling you something specific about an element, and the information is more useful before it fails completely.
