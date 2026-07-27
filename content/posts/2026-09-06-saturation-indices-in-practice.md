---
title: Saturation Indices in Practice
date: 2026-09-06
tag: Water
description: Langelier and its relatives predict whether water will scale or corrode. Useful framing for understanding why very pure water attacks metal, limited as a field tool.
---

Saturation indices try to answer a genuinely useful question with one number: will this water deposit scale, or will it attack metal?

They are worth understanding because the concept explains something important — that scaling and corrosion are two ends of the same axis, not unrelated problems. They are worth being sceptical about as a working tool, for reasons that matter on real machines.

## The idea

Water can hold a certain amount of calcium carbonate in solution. That saturation point depends on temperature, calcium concentration, alkalinity, pH and total dissolved solids.

Compare the water's actual state against that equilibrium and you get three possibilities:

- **Supersaturated.** More carbonate than it can hold. It will deposit the excess as scale.
- **At equilibrium.** Neither depositing nor dissolving. The theoretical ideal.
- **Undersaturated.** Room to dissolve more. It will take carbonate into solution — including from any protective mineral layer inside your plumbing, and then from the metal itself.

The **Langelier Saturation Index** expresses this as the difference between actual pH and the pH at which the water would be saturated. Positive means scaling, negative means aggressive, zero means balanced. The Ryznar and Puckorius indices are variations that weight the inputs differently.

## What it explains well

This framing is the clean answer to a question that otherwise sounds like folklore: **why is pure water corrosive?**

Reverse osmosis permeate has almost no calcium and almost no alkalinity. It is therefore strongly undersaturated — a long way negative. Chemically it is "hungry": it will dissolve carbonate from wherever it can find it, then attack copper and brass directly. It also has essentially no buffering, so its pH wanders with any trace of dissolved CO₂.

That is why unblended RO does not belong on an espresso machine, and the index makes the reason precise rather than a warning to be taken on trust. It is not that pure water is somehow harsh; it is that it is thermodynamically driven to dissolve things.

The same framing explains why aggressive water and scaling water are the *same problem measured in opposite directions*, and why the treatment target is a balanced middle rather than "as little mineral as possible".

> The useful takeaway is directional, not numerical: treatment should move water toward balance, and both over-treatment and under-treatment have failure modes. Stripping minerals is not a safe default.

## Why it is limited in the field

Four reasons I do not calculate an index on a site visit.

**Temperature dependence is severe, and machine temperature is extreme.** The indices were developed for building services and municipal distribution, at temperatures nowhere near a 125 °C boiler. Water that is mildly undersaturated at the tap can be strongly supersaturated at an element sheath. A single index figure for "the water" does not describe what happens at the surface where scale actually forms.

**It needs inputs you may not have.** Proper calculation wants calcium, alkalinity, pH, TDS and temperature. You can get all of those, but if you have them you can already make the treatment decision directly.

**It says nothing about chloride.** Pitting corrosion in stainless steel is driven by chloride, and it is entirely outside this model. A water with a perfectly balanced index can still pit your boiler. This is a significant blind spot for espresso machines specifically.

**It ignores silica.** Which forms its own hard, acid-resistant deposit.

## How I actually use the concept

Not as a calculation. As three rules of thumb that the index justifies:

1. **Do not strip water to near-zero mineral content.** Keep calcium hardness around 50–75 mg/L as CaCO₃, not near zero. The lower bound exists because of aggressiveness, not only because of taste.
2. **Do not remove all alkalinity.** Keep 30–50 mg/L as CaCO₃. Some buffering is protective; zero buffering means an unstable pH sitting against brass.
3. **Never plumb to unblended RO.** Always blend or remineralise, and verify the result by titration rather than trusting the valve position.

Those three rules encode everything the index would tell me, without needing a calculation that the machine's operating temperature invalidates anyway.

## Where a calculation is genuinely worth doing

On a site with unusual water — very soft and acidic supplies, or a building with a history of pinhole leaks in copper — running the numbers is informative. It tells you whether the incoming water is aggressive before treatment, which changes the specification: aggressive source water needs remineralisation rather than dealkalisation, and that is the opposite of the usual answer.

If you are in that situation, get a full lab analysis and either use the utility's own index figure if they publish one, or hand the analysis to a water treatment specialist. It is a case where the extra rigour earns its keep, and it is rare enough that it does not need to be routine.

## The one-sentence version

Water can be too mineral or too pure, both cause damage by opposite mechanisms, and the target is a deliberate middle — which is why every specification in this month's writing has a lower bound as well as an upper one.
