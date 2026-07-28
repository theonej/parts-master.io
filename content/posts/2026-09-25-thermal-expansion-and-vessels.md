---
title: Thermal Expansion and Expansion Vessels
date: 2026-09-25
tag: Water
description: Heating water in a closed system spikes pressure hard enough to weep fittings and fatigue joints. Sizing a vessel, setting its precharge, and why an unchecked precharge makes it useless.
---

Yesterday's post ended with the problem: fitting a backflow preventer closes the water circuit, and a closed circuit cannot absorb the expansion of water being heated.

This is one of the most common causes of mystery leaks on well-installed machines, and the fix is a cheap component that is routinely omitted or fitted wrong.

## The mechanism

Water expands as it heats — around 4% by volume between cold and boiling.

In an open system, that expansion pushes back up the supply pipe harmlessly. In a closed system it has nowhere to go, and because water is nearly incompressible, a small volume increase produces a very large pressure rise. Pressures can exceed the machine's normal operating range substantially, within minutes of the elements coming on.

## Symptoms

- **The brew-side expansion valve relieving to drain**, routinely, during warm-up. A trickle to waste every morning.
- **Brew pressure spiking above setpoint**, then settling.
- **Gauges reading high during heat-up** and normal later.
- **Fittings that weep intermittently** and cannot be found leaking when cold.
- **Joints loosening over months**, from repeated pressure cycling.
- Occasionally, a **safety valve lifting** when nothing is wrong with the boiler.

The diagnostic that confirms it: watch inlet pressure with the machine heating and **no water being drawn**. If pressure climbs steadily as the boiler heats, you have thermal expansion with no path.

> An expansion valve that relieves every morning is not doing its job well. It is telling you there is no expansion path, and each relief cycle is water to drain and a pressure excursion through the whole circuit.

## The fix

An **expansion vessel** on the treated water line, positioned **downstream of the check valve or backflow preventer** and upstream of the machine.

A vessel is a sealed can divided by a flexible bladder or diaphragm. One side connects to the water; the other is a sealed air charge. As water expands, it pushes the bladder and compresses the air, which absorbs the volume with only a modest pressure rise.

Requirements:

- **Potable-rated**, with a bladder material approved for drinking water. A heating-system vessel is the wrong component — different bladder material, not approved for potable contact.
- **Rated for the system pressure.**
- **Supported properly.** A full vessel is heavy; bracket it rather than hanging it on the pipe.
- **Accessible**, so the precharge can be checked and the vessel replaced.

## Sizing

For a single espresso machine, vessels in the 0.5–2 litre range are typically adequate. Sizing depends on the volume of water in the closed section, the temperature rise, and the acceptable pressure increase.

Given how small and cheap these are, err slightly larger rather than smaller. An oversized vessel costs a little more and works fine; an undersized one lets pressure rise anyway and gives false confidence.

Where there is significant pipework in the closed section, or several machines, do the calculation properly or ask the vessel manufacturer.

## Precharge — the step that gets skipped

**This is the detail that makes the difference between a working vessel and an ornament.**

The air side has a precharge pressure, set via a Schrader valve like a tyre valve. It must be set **slightly below the system's static water pressure.**

- **Precharge too high** — the bladder never moves, because water pressure cannot overcome the air charge. The vessel does nothing. Pressure still spikes. Everyone assumes the vessel is working because it is fitted.
- **Precharge too low** — the bladder is fully compressed at rest, so there is no reserve travel. Also useless.

Setting it:

1. Isolate and drain the vessel so there is no water pressure on the bladder.
2. Check the air pressure at the Schrader valve with a tyre gauge.
3. Set it to just below measured static system pressure — commonly a few tenths of a bar below.
4. Reconnect, pressurise, and confirm the machine's warm-up pressure rise is now modest.

Factory precharge is a nominal figure and will not match your site's static pressure. **Check it on installation, every time.**

## Maintenance

Bladders fail, and air charges leak away slowly over years. A vessel with a failed bladder or a lost charge looks identical from outside and does nothing.

- **Check the precharge annually**, with the water side depressurised.
- **Tap test:** a vessel with a healthy charge sounds hollow at the top and solid at the bottom. Solid throughout suggests it is waterlogged.
- **Water at the Schrader valve** when depressing it means the bladder has failed. Replace the vessel.
- **Replace on a lifecycle basis** rather than waiting for failure — they are inexpensive, and the failure mode is silent.

Add it to the annual service list next to the safety valve and vacuum breaker checks.

## Do not solve it the wrong way

Two tempting shortcuts that make things worse.

**Raising the expansion valve setting** so it stops relieving. Now the pressure excursion happens with nothing to relieve it, and the load goes into fittings and the boiler instead.

**Removing the check valve.** That is a code requirement, and removing it to solve a pressure problem trades a plumbing nuisance for a contamination risk and a failed inspection.

The correct sequence is: backflow device because code requires it, expansion vessel because the backflow device requires it, precharge checked because the vessel requires it. Three components, one of which is usually missing and one of which is usually unchecked.
