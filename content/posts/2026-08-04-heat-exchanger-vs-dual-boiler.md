---
title: Heat Exchanger, Dual Boiler, or Multi-Boiler
date: 2026-08-04
tag: Specification
description: Three boiler architectures, what each actually gives you, and what each costs to own. The right answer depends on the menu, not on the price list.
---

This is the decision clients most want to make on brand and appearance, and it is really a decision about thermal architecture. It determines temperature behaviour, power draw, service cost and how many things can fail.

## Heat exchanger

One boiler, kept at steam pressure. Brew water is drawn from the fresh water line through a heat exchanger tube that runs through the steam boiler, picking up heat on the way.

**What it gives you.** Simplicity. One boiler, one element, one pressurestat or one PID loop. Fewer parts to fail and lower purchase price. Steam capacity is generous, because the whole boiler is a steam boiler.

**The catch.** Brew temperature is a consequence of steam pressure rather than something you set independently. Raise steam pressure for better milk performance and brew temperature follows it up. You are always trading one against the other.

The second catch is idle behaviour. Water sitting in the exchanger and group when the machine is not being used keeps absorbing heat, so the first shot after a quiet period comes out too hot. That is what the cooling flush is for — a few seconds of water run through the group to pull the overheated slug out before dosing. It works, but it depends on a barista doing it consistently, and on quiet bars it gets forgotten.

**Who it suits.** Moderate volume, one espresso recipe, a team you trust to flush. Well-made HX machines pull excellent espresso — the constraint is control, not quality.

## Dual boiler

Two separate boilers: one at brew temperature, independently controlled, and one at steam pressure.

**What it gives you.** Brew temperature as a directly settable number, held by its own PID loop, completely decoupled from steam. No cooling flush. Consistency from the first shot of the day, and consistency between a quiet Tuesday and a busy Saturday.

**The cost.** More elements, more probes, more controls, more power. Higher purchase price and a longer parts list. Warm-up draws more.

**Who it suits.** Most serious specialty bars. If the client is weighing shots, tracking extraction and cares about repeatability, this is the sensible default. The independent brew control is the single biggest step up in day-to-day consistency available.

## Multi-boiler

A separate brew boiler for each group, plus a steam boiler.

**What it gives you.** Independent brew temperature per group. Run a light Ethiopian at one temperature on group one and a dark blend three degrees lower on group two, simultaneously, with no compromise. Also excellent thermal recovery, because each group has its own dedicated thermal mass and element.

**The cost.** The highest of the three, in purchase, power and service. A three-group multi-boiler has four boilers, four elements, four probes and four control loops. Everything that can fail exists three or four times over. Electrical demand is materially higher, which loops straight back into supply sizing.

**Who it suits.** Bars genuinely running multiple coffees at different temperatures at the same time, and high-volume bars where recovery under sustained load is the binding constraint. If the bar runs one espresso recipe, the per-group temperature control is capability nobody will use, and it is expensive capability to maintain.

> Specify the architecture from the menu. "Will this bar ever brew two different coffees at two different temperatures at the same time?" If no, a multi-boiler is a service liability bought for a feature that will sit idle.

## Recovery matters more than steady-state stability

Manufacturers advertise temperature stability, usually as a tight number measured on an idle machine. That figure is close to useless for choosing a machine.

What matters on a real bar is **recovery under load**: pull four doubles back to back while steaming continuously and see where brew temperature and steam pressure end up. That is where architecture and element sizing show themselves, and where a machine either keeps up or does not.

If you can, test this before buying. A machine that holds ±0.2 °C at idle and sags two degrees through a rush is worse than one with a less impressive idle figure and better recovery.

## Group design interacts with all of this

The boiler is half the thermal story; the group head is the other half.

- **Saturated groups** are effectively part of the boiler, with brew water circulating through the group body. Very stable, high thermal mass, slow to change temperature by design.
- **Semi-saturated and thermosyphon groups** sit between, relying on circulation to keep the group at temperature.
- **E61-style groups** use a large brass mass and thermosyphon circulation. Forgiving and stable once hot, slow to warm up, and they hold heat well between shots.

A stable boiler feeding a poorly heated group does not produce stable brew water at the puck. Judge the pair together.

## The ownership question

The comparison clients rarely see:

| | Heat exchanger | Dual boiler | Multi-boiler (3gr) |
| --- | --- | --- | --- |
| Boilers | 1 | 2 | 4 |
| Elements | 1 | 2 | 4 |
| Temp probes / controls | 1 | 2 | 4 |
| Brew temp control | Via steam pressure | Independent | Independent per group |
| Cooling flush needed | Yes | No | No |
| Relative service exposure | Lowest | Moderate | Highest |

None of that argues against multi-boilers. It argues for buying the architecture the menu requires, then spending what is left on water treatment, grinders and a service contract — all of which affect the cup more than an unused temperature channel ever will.
