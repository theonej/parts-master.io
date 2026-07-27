---
title: Temperature Stability: PID, Probes and Offsets
date: 2026-08-18
tag: Diagnostics
description: The number on the display is not the water hitting the coffee. How to find the offset, how to tell control problems from thermal ones, and why PID tuning is the last thing to touch.
---

Temperature complaints arrive as "the machine is running hot" or "it can't hold temperature". Both statements are about the display, and the display is measuring a spot inside the machine that is not the puck.

Before adjusting anything, the useful question is which of three different faults you are looking at, because they have different causes and only one of them involves the controller.

## Establish the offset first

The probe sits wherever the manufacturer put it — in the boiler, in the group, in a thermosyphon line. The water that reaches the coffee has travelled further and lost or gained heat on the way. The difference between the two is the **offset**, it is specific to the machine and its installation, and it can be several degrees.

Measure it with a group thermometer — a Scace-type device or a thermofilter — and compare against the display under normal working conditions. Write the number down.

That single figure resolves an enormous number of arguments. A machine displaying 93 °C and delivering 90.5 °C is not faulty; it has an offset, and the recipe should be set from the measured value. Without it, one bar's "93" and another's "93" are not the same temperature and their notes are not comparable.

> Take the offset at commissioning and record it in the baseline. Retake it when anything in the brew path changes.

## Three different faults

**Drift over the session or the day.** Readings slowly climb or fall. This is thermal, not control — ambient temperature, cabinet ventilation, warm-up state, or heat soaking into the group mass. Look at the environment and the warm-up regime.

**Oscillation cycle to cycle.** The reading hunts above and below setpoint repeatedly. This is a control or sensing problem — controller tuning, or a probe that is responding late.

**Step changes or implausible values.** The reading jumps, or reads something impossible. Electrical: probe, wiring, connection, or the controller input. Not a tuning issue.

Identifying which pattern you have takes ten minutes of watching the display and saves an afternoon.

## Check the mechanical and thermal causes before the controller

This is the discipline that matters, because PID parameters are easy to change and changing them hides symptoms rather than fixing causes.

- **Scale on the element or the probe.** Scale is an insulator. On the element, the controller sees the boiler responding sluggishly and overshoots. On the probe, the reading lags reality, which produces oscillation that looks exactly like bad tuning. **This is the most common real cause of a machine that has "developed" a temperature problem.** A machine that was stable for three years and is now hunting has a deposit, not a tuning error.
- **Water level.** A low steam boiler level changes the thermal mass and can expose the probe or the element.
- **Insufficient warm-up.** Group heads are large lumps of brass with a lot of thermal mass. A machine needs 20–40 minutes from cold for the groups to reach equilibrium, and bars that switch on ten minutes before opening have an unstable first hour by design. Fit a timer or use the machine's scheduled-on function.
- **Thermosyphon restriction.** On HX and thermosyphon machines, circulation to the group depends on clear passages. Scale or debris slows the loop and the group runs cool while the boiler reads correct.
- **Ambient and cabinet ventilation** — the heat-load post applies directly here.
- **A failing probe.** PT100 and thermocouple elements drift as they age. A drifting probe reads *steadily wrong*, which produces a machine that is stable but at the wrong temperature — often diagnosed as needing recalibration when it needs a probe.

## Compare groups against each other

On a multi-group machine this is the highest-value diagnostic available, and it is free.

Measure brew temperature and flow at every group under the same conditions. They should be close. If one group runs consistently cooler:

- Thermosyphon restriction to that group.
- A partially blocked gicleur or dispersion block on that group.
- On a multi-boiler machine, that group's own element, probe or control loop.

A single cold group is why one barista's shots taste different from their colleague's, and it is invisible to a team where each person works one side of the machine.

## Test recovery, not idle

Idle stability is easy and largely meaningless. What matters is behaviour under load.

The test: pull four doubles back to back while steaming continuously, and watch brew temperature and steam pressure through it and for two minutes afterwards. Record the sag and the recovery time.

That number belongs in the baseline too. When a bar says the machine cannot keep up any more, the recovery test compared against the commissioning figure answers whether anything has actually changed.

## PID, last

Only after the above. Most machines ship with sensible parameters, and the factory knows the thermal system better than you do on a first visit.

Read the symptoms:

- **Oscillating around setpoint** — proportional action too aggressive, or integral winding up. But check probe lag and scale first, because both produce this.
- **Slow to recover, sits below setpoint under load** — control too conservative, or the element simply lacks the power for the demand, which is a specification problem rather than a tuning one.
- **Overshoots badly on warm-up, then settles** — often normal behaviour, and many controllers have a separate warm-up strategy for exactly this.

Change one parameter at a time, in small increments, and give it several cycles under realistic load before judging. Write down what you changed and what it was before. A machine with three visits' worth of undocumented parameter changes is genuinely hard to recover.

## What to record

Group temperature and offset per group, steam pressure, warm-up time to stable, and the load-recovery figures. Six numbers.

Take them at commissioning and at every annual service. Almost every temperature question a client asks is answerable by comparing today's six numbers with last year's — and unanswerable without them.
