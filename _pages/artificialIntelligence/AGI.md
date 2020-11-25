---
layout: default
title: Philosopher Scholar - AGI
permalink: /AGI/
---

## [The MIT AGI Course](https://agi.mit.edu)

[Building machines that see, learn, and think like people | Josh Tenenbaum](https://www.youtube.com/watch?v=7ROelYvo8f0&list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4&index=56&t=0s)

Center for Brains, Minds, and Machines (CBMM).

Fundamental principle of CBMM: The basic science of how intelligence arises in biological systems can lead to fundamental advances in the engineering of intelligence - if we approach our science like engineers.

---

[Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](https://arxiv.org/abs/cs/0309048)

[Wikipedia article](https://en.wikipedia.org/wiki/G%C3%B6del_machine)

[Juergen Schmidhuber](https://people.idsia.ch/~juergen/) - 2003

[Schmidhuber's page on Goedel Machines](https://people.idsia.ch/~juergen/goedelmachine.html)

> We present the first class of mathematically rigorous, general, fully self-referential, self-improving, optimally efficient problem solvers. Inspired by Kurt Goedel's celebrated self-referential formulas (1931), such a problem solver rewrites any part of its own code as soon as it has found a proof that the rewrite is useful, where the problem-dependent utility function and the hardware and the entire initial code are described by axioms encoded in an initial proof searcher which is also part of the initial code. The searcher systematically and efficiently tests computable proof techniques (programs whose outputs are proofs) until it finds a provably useful, computable self-rewrite. We show that such a self-rewrite is globally optimal - no local maxima! - since the code first had to prove that it is not useful to continue the proof search for alternative self-rewrites. Unlike previous non-self-referential methods based on hardwired proof searchers, ours not only boasts an optimal order of complexity but can optimally reduce any slowdowns hidden by the O()-notation, provided the utility of such speed-ups is provable at all.

[Ultimate Cognition a la Goedel](https://people.idsia.ch/~juergen/ultimatecognition.pdf)

> "All life is problem solving," said Popper. To deal with arbitrary problems in arbitrary environments, an ultimate cognitive agent should use its limited hardware in the ‘‘best’’ and ‘‘most efficient’’ possible way. Can we formally nail down this informal statement, and derive a mathematically rigorous blueprint of ultimate cognition?
Yes, we can, using Kurt Godel’s celebrated self-reference trick of 1931 in a new way. Godel exhibited the limits of mathematics and computation by creating a formula that speaks about itself, claiming to be unprovable by an algorithmic theorem prover: either the formula is true but unprovable, or math itself is flawed in an algorithmic sense. Here we describe an agent-controlling program that speaks about itself, ready to rewrite itself in arbitrary fashion once it has found a proof that the rewrite is useful according to a user-defined utility function. Any such a rewrite is necessarily globally optimal—no local maxima!—since this proof necessarily must have demonstrated the uselessness of continuing the proof search for even better rewrites. Our self-referential program will optimally speed up its proof searcher and other program parts, but only if the speed up’s utility is indeed provable—even ultimate cognition has limits of the Godelian kind.

---

[AIXI](https://en.wikipedia.org/wiki/AIXI)

> AIXI is a theoretical mathematical formalism for artificial general intelligence. It combines Solomonoff induction with sequential decision theory. AIXI was first proposed by Marcus Hutter in 2000 and several results regarding AIXI are proved in Hutter's 2005 book Universal Artificial Intelligence.
AIXI is a reinforcement learning agent. It maximizes the expected total rewards received from the environment. Intuitively, it simultaneously considers every computable hypothesis (or environment). In each time step, it looks at every possible program and evaluates how many rewards that program generates depending on the next action taken. The promised rewards are then weighted by the subjective belief that this program constitutes the true environment. This belief is computed from the length of the program: longer programs are considered less likely, in line with Occam's razor. AIXI then selects the action that has the highest expected total reward in the weighted sum of all these programs.
