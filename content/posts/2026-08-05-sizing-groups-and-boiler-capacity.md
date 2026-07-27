---
title: Sizing Groups and Boiler Capacity to Real Throughput
date: 2026-08-05
tag: Specification
description: Group count is set by peak fifteen minutes, not daily covers. And on a milk-heavy menu the binding constraint is usually steam, not groups.
---

Clients size machines from daily volume. "We expect four hundred cups a day, so we need three groups." Daily volume is almost irrelevant. Four hundred cups spread evenly over twelve hours is a two-group bar with time to spare. Four hundred cups with two hundred of them between 7:45 and 9:15 is a different machine entirely.

The design number is the **peak fifteen minutes**.

## Finding the peak

If the client has an existing site, the POS data has the answer — pull transactions by fifteen-minute interval across a fortnight and find the worst one. If it is a new site, estimate from the surrounding footfall and be honest that it is an estimate, then build in headroom.

Then split the peak by drink type. Espresso-based drinks load the groups. Milk drinks additionally load the steam boiler. Batch filter and hot water load neither, which means a menu with substantial filter volume needs fewer groups than its cup count suggests.

## What a group actually produces

Not the theoretical figure. Including dosing, tamping, locking in, extraction and knocking out, a competent barista working one group sustainably produces roughly **50–70 espresso-based drinks per hour**. Two baristas on a two-group machine can exceed that briefly, but not for an hour.

So:

| Peak espresso drinks per hour | Groups |
| --- | --- |
| Up to ~60 | 1, with 2 strongly preferred |
| 60–130 | 2 |
| 130–200 | 3 |
| Above 200 | 3 plus a second machine, or 4 |

Two caveats on that table.

**Baristas, not groups, are usually the limit.** A three-group machine with one barista behind it is a two-group machine with a spare. Group count has to match staffing at peak, and if the bar only ever rosters two people, the third group buys you very little throughput.

**Redundancy is a real argument for one more group.** A solenoid fails on a two-group machine and the bar is at 50% capacity until someone arrives. On a three-group machine it is at 67% and the day survives. For a site where downtime is expensive, that is often the strongest case for the extra group — stronger than the throughput case.

## Steam is frequently the actual constraint

On a menu that is mostly flat whites and lattes, the steam boiler decides whether the bar keeps up.

Steaming a jug takes 20–30 seconds and pulls a real quantity of energy out of the boiler. Do that continuously on two wands and the boiler has to replace that energy as fast as it leaves. If it cannot, pressure sags, steaming gets slower, and the queue grows — while the groups sit idle. The barista's experience is "the machine can't keep up", and adding a group would not help at all.

Two numbers matter, and they are different:

- **Boiler volume** is the buffer. It gets you through a burst.
- **Element power** is the refill rate. It gets you through an hour.

A large boiler with an undersized element handles the first five minutes of a rush and then slowly loses ground. A smaller boiler with a strong element recovers continuously. For sustained milk-heavy service, the element rating is the number to interrogate, and it is the one that rarely appears in marketing material.

Rough steam boiler volumes for planning: 7–12 litres on a two-group, 12–20 on a three-group. Treat those as sanity checks and ask the distributor for the steam boiler element rating separately.

> On a milk-forward menu, ask for the steam boiler element kW before you ask about anything else. It predicts peak performance better than group count.

## Wands, and how many

Two steam wands let two jugs be textured simultaneously, which on a milk-heavy bar effectively doubles the finishing rate. Most two- and three-group machines have two as standard. It is worth confirming rather than assuming, and worth asking whether both are on full-bore valves.

Automatic milk texturing systems are a separate decision. They deliver consistency and free up hands, at the cost of another set of components in the steam circuit to maintain and clean. On high-volume, high-turnover sites they earn their keep; on a bar built around craft they usually do not get used.

## Do not oversize

Buying a bigger machine than the bar needs has ongoing costs that nobody mentions at the point of sale:

- **Standby power.** A bigger boiler holds more water at temperature all day, whether or not it is used.
- **Room heat.** All of that standby loss goes into the space, adding to a cooling load already likely under-specified.
- **Electrical supply.** A four-group machine may push the site into a supply upgrade — a genuinely large cost.
- **Counter space,** which on most bars is the scarcest resource of all.
- **Service exposure.** More groups means more solenoids, more gaskets, more of everything on the parts list.

A right-sized machine plus proper water treatment plus better grinders beats an oversized machine on a compromised install, every time.

## The sizing conversation

Take the client's own peak data, split it by drink type, and put the arithmetic in front of them. Then present the group count and the steam element rating as two separate recommendations with two separate justifications.

That conversation also surfaces the thing worth knowing early: whether the peak they are describing is what they have measured, or what they are hoping for. Those want different machines, and it is better to name the difference than to design for optimism.
