---
title: "Carbonate Chemistry: How Scale Actually Forms"
date: 2026-09-05
tag: Water
description: Why heating water deposits carbonate, why the hottest surface always loses, and why watt density decides how fast an element scales.
---

Scale is not dirt accumulating. It is a chemical reaction with a specific driver, and understanding the driver tells you exactly where deposit will form and what reduces it.

## The reaction

Calcium in water pairs with bicarbonate as calcium bicarbonate, which is soluble. Heat it and it decomposes:

**Ca(HCO₃)₂ → CaCO₃ + CO₂ + H₂O**

Calcium carbonate is not soluble. It comes out of solution and deposits on whatever surface it formed against. Carbon dioxide leaves as gas.

That is the whole mechanism. Note what it requires: calcium **and** bicarbonate **and** heat. Remove any one and there is no scale.

## Why heat drives it so hard

Three things push the reaction forward as temperature rises, which is why scale is an espresso machine problem rather than a plumbing problem.

**CO₂ solubility falls with temperature.** Dissolved carbon dioxide holds the bicarbonate equilibrium in place. Heat the water, CO₂ comes out of solution and escapes, and the equilibrium shifts toward carbonate.

**Calcium carbonate has retrograde solubility.** Unusually among salts, it becomes *less* soluble as temperature rises. Most things dissolve better when hot; this does the opposite. So hot water can hold less carbonate in solution precisely where it is being produced fastest.

**Local surface temperature exceeds bulk temperature.** The water in the boiler might be at 125 °C, but the metal surface transferring heat into it is hotter. The reaction happens fastest right at that surface, and that is where the deposit lands.

> Scale does not form in the water. It forms *on the hottest surface the water touches*. That is why elements and heat exchanger walls scale first, and why a boiler can be substantially deposited before anything else shows symptoms.

## Where it deposits, in order

1. **The heating element sheath.** Hottest surface in the machine, and the deposit is self-accelerating — see below.
2. **The heat exchanger wall**, on HX machines, for the same reason.
3. **Boiler surfaces near the heat input.**
4. **Small orifices downstream** — gicleurs, solenoid seats, thermosyphon restrictors. Fragments and slow accumulation both narrow them, which is why group flow rate is such a good early indicator.
5. **Level probes and their insulators**, causing the autofill faults covered earlier.

## Watt density, and why elements fail

Two elements can have the same total power and very different surface areas. Power divided by surface area is **watt density**, and it sets how hot the sheath runs.

A high watt density element runs a hotter surface, so it drives the reaction harder and scales faster. Then the deposit makes it worse: carbonate is a thermal insulator, so the element has to run hotter still to push the same heat through it. Hotter surface means faster deposition, which means more insulation.

That runaway is why elements fail rather than simply getting less efficient. The element eventually exceeds its own temperature limit and burns out — and when it comes out you can read the history off it, which is exactly how warranty claims get declined.

It also explains the temperature symptoms. A scaled element makes the boiler respond sluggishly to heat demand, so the controller overshoots and hunts. A machine that was stable for years and has "developed a PID problem" usually has a deposit, not a tuning error.

## Deposit character varies

Not all scale is the same, and it affects how bad the consequences are.

Calcium carbonate crystallises in different forms. Broadly, deposits formed at higher temperatures tend to be denser and more strongly adherent, while cooler deposits are softer and more crumbly. Hard adherent scale on an element is the worst case — thermally insulating and mechanically difficult to remove without damaging the sheath.

Magnesium and silica change the character too. Silica in particular can produce a very hard, glassy deposit that is extremely resistant to acid, which is one reason silica is worth knowing about from a lab analysis.

## What actually reduces it

Follow the reaction. You need calcium, bicarbonate and heat, and heat is not negotiable.

**Reduce bicarbonate — alkalinity.** The most effective lever, because it is usually the limiting reagent and because reducing it also fixes the flat-tasting-coffee problem. This is what weak acid cation resin and RO both do.

**Reduce calcium.** Effective for scale, but taken too far it produces thin, hollow espresso, and softening does it while leaving alkalinity in place.

**Do not attempt to change the heat.** Running a boiler cooler to reduce scaling is trading the machine's actual function for its longevity.

The practical consequence is that scale prevention and taste improvement are the *same intervention*. Reducing alkalinity to the 30–50 mg/L range simultaneously removes most of the scale potential and most of the buffering that flattens the cup. That alignment is unusual and worth pointing out to clients — you are not asking them to trade flavour for equipment life.

## The arithmetic worth quoting

Deposit accumulates roughly in proportion to volume through the machine multiplied by the scale-forming hardness in it. Halving alkalinity therefore roughly halves the deposition rate, which roughly doubles the time to a given amount of scale.

That is the number that makes the case for treatment: it is not a marginal improvement, it is a multiple on the interval before the element is in trouble.
