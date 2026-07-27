---
title: Electrical Faults: Elements, Contactors and SSRs
date: 2026-08-22
tag: Diagnostics
description: Testing an element properly, why contactors weld shut, and how to tell a failed SSR from a failed controller. Plus the loose terminal that burns a machine's loom.
---

Electrical faults on an espresso machine are mostly unglamorous and mostly predictable: a heating element that has come to the end of its life, a switching device that has done a few million operations, or a joint that was not tight enough.

They also carry real risk, so the first paragraph is the boring one. Isolate at the local disconnect, prove dead, and work on a machine that cannot be energised by someone else. There is mains voltage and several kilowatts of heating load behind the panel, sitting next to plumbing.

## Testing an element properly

Two measurements, and the second one is the one people skip.

**Resistance across the element.** Compare against the expected value from the rating: resistance ≈ voltage² ÷ power. A 2 kW element at 230 V should read around 26 Ω. Open circuit means the element has failed. A reading well away from expected means it is failing.

**Insulation resistance to earth.** This is the important test. Use an insulation tester between the element terminals and the boiler body. A healthy element reads very high. A degrading element reads progressively lower as moisture penetrates the insulation, and that falling value is what eventually trips the RCD.

Two details that matter:

- **Test hot as well as cold.** Some elements pass every test cold and fail once expanded and at temperature. If a machine trips only after warm-up, that is your fault, and a cold test will declare the element healthy.
- **Disconnect the element from the circuit** before testing insulation, or you are measuring everything else attached to it.

An element with falling insulation resistance is on a countdown. Replace it on a planned visit rather than waiting for the trip during service.

## Nuisance tripping versus a real fault

Covered in the electrical install post, worth restating as a diagnostic:

- **Machine trips its own dedicated RCBO, repeatedly** — genuine fault. Test elements hot and cold to earth. Check for water ingress onto terminals and for a chafed loom.
- **Machine trips a shared device, especially on morning switch-on** — probably accumulated leakage from several appliances adding up. The fix is separate protection per appliance, not a bigger device.

Establish which of the two you have before opening anything: ask what else is on that device, and whether it trips at switch-on or during service.

## Contactors

Contactors switch the element load. They are electromechanical, they operate a great many times, and they fail in two characteristic ways.

**Welded closed.** Contacts arc every time they open. Eventually they weld together and the element is permanently energised. The machine over-heats, over-pressures, and the relief valve or thermal cutout becomes the only thing between you and a serious incident.

This is the failure mode to take seriously. The signature is a machine that keeps heating past its setpoint with the controller calling for no heat. **If pressure or temperature climbs with the controller satisfied, isolate the machine immediately** — do not leave it running while you investigate.

**Burnt or high-resistance contacts.** Pitted contacts develop resistance, which produces heat and reduced element power. The machine heats slowly and never quite keeps up during a rush. The tell is a hot, discoloured contactor and often a smell.

Contactors are consumables. On a high-cycling machine, replacing them at a scheduled interval is cheaper than the consequences of a weld. Inspect them at every annual service — discoloured housings, chattering, or a mechanical buzz all mean replace.

## Solid-state relays

Many PID machines switch the element with an SSR instead of a contactor, cycling far more often — which is how tight temperature control is achieved.

**SSRs fail short circuit.** That is the normal failure mode, and it produces the same dangerous outcome as a welded contactor: element permanently on. Same rule — heating with the controller satisfied means isolate now.

**They fail from heat.** An SSR must be mounted to an adequate heatsink with thermal compound, in moving air. A hot cabinet shortens its life, which is another way the heat-load conversation shows up as an electrical fault.

Diagnosing SSR versus controller:

1. Isolate and inspect. A failed SSR is often visibly discoloured or smells.
2. With the controller calling for no heat, check whether the SSR is still passing current to the element. If it is, the SSR is short.
3. If the SSR is not passing but the controller *is* sending a control signal to it, the SSR has failed open.
4. If the controller is sending no signal when it should, the fault is upstream — controller, or the probe feeding it.

Check the heatsink mounting whenever you replace one. An SSR that failed from heat will do it again on the same bad mounting.

## The loose terminal

The mundane one that does real damage.

A screw terminal carrying 25 A with a fraction of a turn less than it needs has resistance. Resistance at that current makes heat. The heat oxidises the joint, which raises the resistance further, which makes more heat. It runs away over months.

The result is a charred terminal block, insulation cooked off the adjacent conductors, and sometimes a loom that needs replacing — from a fault whose fix, caught early, was a screwdriver.

So: check element and contactor terminal tightness at commissioning and at every annual service. Look for discoloured insulation, browned terminal blocks and any smell of hot plastic. Discolouration around a terminal is not cosmetic; it is a thermal history.

## Water and electricity in one box

Espresso machines put a boiler above an electrical bay. Leaks land on electrical components.

When investigating any electrical fault, look for evidence of water having been where it should not: mineral staining on the chassis, corrosion on terminals, a tide mark on a control board. That evidence points at the real fault, which may be a weeping fitting three months ago rather than the component that has just failed.

Fixing the electrical part and leaving the leak means doing the job twice.

## Annual electrical service

1. Element resistance and insulation to earth, cold and hot, per element. Recorded.
2. All element and contactor terminals checked for tightness.
3. Contactors and SSRs inspected; SSR heatsink mounting confirmed.
4. Earth continuity to body and boiler, verified and recorded.
5. Interior inspected for water ingress evidence.
6. Confirm no protective device has been bypassed.
7. Readings written into the log, so next year's numbers mean something.

Insulation resistance in particular is only useful as a trend. One reading tells you the element is alive today. Three years of readings tell you which winter it is going to fail.
