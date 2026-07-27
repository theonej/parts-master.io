---
title: Autofill, Level Probes and Boiler Faults
date: 2026-08-21
tag: Diagnostics
description: The circuit that stops an element burning out. How conductivity probes actually fail, why over-filling produces wet steam, and the timeout that saves a boiler.
---

The autofill system is a small circuit with one critical job: keep water over the element. When it fails in the unhelpful direction, you lose an element and possibly more.

It is also the system most often "fixed" by bypassing something, which is why I check for previous interference on any machine I have not seen before.

## How level sensing works

Most commercial machines use a **conductivity probe**: a metal rod, insulated from the boiler, hanging down to the target water level. Water conducts, so when the water touches the probe tip a tiny current flows between probe and boiler body, and the controller reads "level reached". When the water drops below the tip, the circuit opens and the fill valve energises.

This is elegant and reliable, and it has three failure modes that follow directly from how it works.

**Scale on the probe tip — insulation.** Scale does not conduct. A scaled probe stops seeing water that is genuinely there, so the controller keeps filling. The boiler over-fills.

**A conductive bridge — false full.** Scale, corrosion product or a wet mineral deposit tracking across the probe's insulator gives the controller a permanent "water present" signal even when the boiler is empty. **This is the dangerous one:** the machine believes it is full, never calls for water, and the element runs dry.

**Water conductivity too low.** Overly pure water conducts poorly, so the probe reads unreliably. Which is one more reason unblended RO does not belong on an espresso machine — it interferes with the level sensing as well as corroding the plumbing.

Some machines use float switches or capacitive sensors instead. Floats stick, and their pivots scale up. The diagnostic logic below still applies.

## Reading the symptoms

**Boiler over-fills; wet, spitting steam.** Water level has risen above the steam take-off, so you are drawing water with the steam. Suspect a scaled probe, or a fill valve passing when de-energised. This is the most common presentation.

**Machine fills continuously, or fills and never stops.** Probe not registering (scale), probe wiring open circuit, controller input failed, or a fill solenoid stuck open. If water is running to the drain, isolate the machine.

**Machine never fills; low water alarm; element protection trips.** False-full from a conductive bridge, or a failed fill solenoid, or no water supply. Do not keep resetting it — the reason it stopped is the reason the element still exists.

**Level hunts, fill valve chatters.** Probe fouling, turbulence at the probe, or a marginal signal. Often an early indication of the scale problem before it becomes a hard fault.

**Slow to fill, especially during a rush.** Not the autofill. Look at the filter cartridge, line pressure, and inlet strainer — the same starved-inlet chain from the pump post.

## Diagnosis

1. **Establish the true water level.** Sight glass where fitted; otherwise the hot water tap. Do not start from what the display claims.
2. **Pull and inspect the probe.** Isolate, depressurise, remove it. You are looking at the tip for scale and at the insulator for tracking, deposit or cracking. A visual inspection answers most of these faults immediately.
3. **Clean or replace.** Descale the probe tip carefully, clean the insulator thoroughly, and inspect the insulator for damage. Probes are inexpensive — if the insulator is at all suspect, replace rather than clean. This is not a part worth nursing.
4. **Test the fill solenoid** both ways: does it open when energised, and does it fully close when not? A valve passing slightly when closed slowly over-fills a boiler overnight and produces a machine that is wet-steaming first thing and fine by ten o'clock.
5. **Check the wiring and earth.** The probe circuit relies on the boiler body as its return path. A poor earth bond gives erratic level readings, and it is a genuine safety item in its own right.
6. **Confirm the protective functions still work,** below.

## The timeout, and never bypassing it

Most machines have a fill timeout: if the level is not satisfied within a set period, the fill stops and the machine alarms. It exists so that a probe failure or a lost water supply does not become a flooded floor or a dry-fired element.

Machines also have low-water element protection, and many have a thermal fuse or cutout as a last resort.

Check all of these exist and are connected. On a machine with a service history you do not know, **look for evidence that someone has bypassed one** — a jumpered terminal, a disconnected probe lead, a defeated cutout. It happens, usually as a Saturday-morning expedient that was never undone.

> If you find protection bypassed, restore it and put it in writing. That bypass is the difference between a probe fault and a destroyed boiler, and the person who fitted it is not the person who will be blamed.

## Over-filling is a quality problem too

Wet steam is not only a nuisance. Steam carrying water condenses into the milk, so texturing takes longer, the milk ends up thinner and more dilute, and the barista compensates by steaming longer and hotter.

Bars live with this for months, blaming milk supply or technique. Ten minutes with the sight glass and the probe fixes it.

## It is a water problem, again

Every failure mode above except a genuinely faulty solenoid is driven by deposit — scale on the tip, tracking across the insulator, deposit in a float pivot.

Which means autofill reliability is decided by water treatment, like element life, valve life and gicleur condition. A machine on correctly specified water has a probe that gets cleaned at annual service and otherwise works. A machine on untreated hard water has a probe that becomes a recurring callout, and eventually an element.

## Service routine

- Inspect and clean the probe annually; replace on any doubt about the insulator.
- Confirm fill cut-off level against the sight glass.
- Test that the fill solenoid closes fully.
- Confirm timeout and low-water protection are present, connected and not bypassed.
- Record the fill cycle time in the baseline; a lengthening cycle is an early inlet restriction.
