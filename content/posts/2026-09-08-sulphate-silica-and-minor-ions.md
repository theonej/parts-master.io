---
title: Sulphate, Silica and the Minor Ions
date: 2026-09-08
tag: Water
description: What else is in the analysis. Silica forms deposits that acid will not touch, sulphate changes the taste, and iron destroys the resin you just paid for.
---

Hardness, alkalinity, chloride and chlorine cover most decisions. The rest of a lab analysis is not filler, and two entries on it can invalidate a treatment specification entirely.

## Silica — the deposit acid cannot remove

The most important minor ion, and the one that catches people out.

Silica forms a deposit that is glassy, extremely hard and **highly resistant to acid**. A machine descaled with a conventional product can come back with the deposit essentially untouched, because it was never carbonate.

The diagnostic signature is exactly that: a machine that has been descaled, apparently correctly, and still has restricted flow and a coated element. If you meet that, suspect silica and get an analysis.

It is common in volcanic regions and in some groundwater. Levels above roughly 20–30 mg/L are worth taking seriously in a machine running at boiler temperature, where silica concentrates by evaporation exactly as chloride does.

**What removes it:** reverse osmosis, largely. Not carbon, not softening, not weak acid cation resin. So like chloride, silica is a parameter that decides the treatment architecture rather than a detail to manage within it — and like chloride, blending untreated feed back into RO permeate brings it back proportionally.

## Sulphate

Sulphate contributes **permanent (non-carbonate) hardness**. It does not decompose on heating, so it is not part of the carbonate scale mechanism.

Two things it does do:

**Taste.** Sulphate reads as dryness and a mineral sharpness. In modest amounts it is unobjectionable and can add definition; at high levels it makes coffee taste dry, hard and slightly bitter, and the effect is not something you can dial out at the grinder.

**Calcium sulphate deposit,** at high concentrations. Far less common than carbonate scale, but calcium sulphate is dense, adherent and unpleasant to remove. It becomes a consideration on genuinely high-sulphate water concentrated in a steam boiler.

Below roughly 50 mg/L, ignore it. Above a few hundred, it belongs in the conversation.

## Sodium

Matters for two reasons, neither structural.

**Taste.** High sodium gives a distinctly salty edge. The SCA brew standard targets around 10 mg/L for a reason.

**As a diagnostic.** High sodium with near-zero hardness is the unmistakable signature of an ion exchange softener upstream. If you measure that combination on a supply that the utility reports as hard, you are downstream of a building softener nobody told you about — and you should also check chloride, because regeneration brine contributes it.

## Magnesium

Part of total hardness, and frequently discussed as though it were interchangeable with calcium. It is not quite: magnesium is generally considered to extract slightly differently, and some people describe it as giving a brighter, more complex extraction than calcium alone.

For practical specification purposes it sits inside the hardness number and you rarely control it independently. It becomes a real decision only if you are remineralising RO permeate from scratch, where you choose the ratio deliberately.

## Iron and manganese

These deserve attention because they damage equipment you are about to install.

**They foul ion exchange resin and RO membranes.** Iron oxidises and precipitates onto media, coating it and destroying capacity. Fitting a WAC cartridge on iron-bearing water without addressing the iron first means a cartridge that is exhausted long before its rated volume.

They also stain, and they taste metallic.

If iron shows up above about 0.3 mg/L, it needs oxidation and filtration ahead of anything else in the train. This is specialist territory and it is worth handing to a water treatment company rather than improvising.

## Organics and total organic carbon

Contribute taste and odour, exert a chlorine demand, and foul both carbon and membranes. Surface-water supplies carry more, and more in summer.

Practically: they are the reason carbon has a finite life for taste removal even though chlorine reduction is catalytic, and the reason surface-water sites need shorter cartridge intervals than the volume calculation suggests.

## Dissolved gases

**Carbon dioxide** lowers pH and makes water more aggressive to copper and brass. It matters most in low-alkalinity water, where there is no buffering to resist it — another argument against stripping alkalinity to zero.

**Hydrogen sulphide** announces itself: rotten eggs. Removed by oxidation and carbon.

## Nitrate and the rest

Nitrate is a public health parameter and the utility's problem, not an equipment one. Fluoride likewise. They appear on the analysis and can be noted and set aside.

## What to actually do

One full lab analysis per site at specification time catches all of this, and it is inexpensive relative to the treatment it specifies. From it, act on:

1. **Silica** above ~20–30 mg/L → RO, and remineralise rather than blend.
2. **Iron or manganese** present → dedicated removal ahead of everything, get specialist input.
3. **Sodium high with hardness low** → you are downstream of a softener; find out and reconsider the whole supply.
4. **Sulphate very high** → expect a taste effect and note it.

Everything else goes in the water log as baseline, where it costs nothing and occasionally explains something years later.
