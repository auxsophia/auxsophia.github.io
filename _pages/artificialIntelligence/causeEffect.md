---
layout: default
title: Philosopher Scholar - Cause and Effect
permalink: /ai/causeEffect/
---

# "Correlation is not causation."

A phrase repeated to break down certainty in inferring cause and effect relationships.




---

## Interesting research

[Algorithms for Causal Reasoning in Probability Trees](https://arxiv.org/abs/2010.12237)

> Probability trees are one of the simplest models of causal generative processes. They possess clean semantics and -- unlike causal Bayesian networks -- they can represent context-specific causal dependencies, which are necessary for e.g. causal induction. Yet, they have received little attention from the AI and ML community. Here we present concrete algorithms for causal reasoning in discrete probability trees that cover the entire causal hierarchy (association, intervention, and counterfactuals), and operate on arbitrary propositional and causal events. Our work expands the domain of causal reasoning to a very general class of discrete stochastic processes.

I notice they treat the causal hierarchy (Judea Pearl's ladder of causation) as a basic fact. Probability trees are an alternative to causal Bayesian networks with contextual properties.

"It is worth pointing out that we distinguish between probabilistic and logical truth. A min-cut for
a given event is determined solely through the skeleton of the probability tree without taking into
account the transition probabilities (see the example in Figure 2f).
Once a min-cut for an event has been determined, then the probability of said event is given by
the sum of the probability of the true nodes. Probability distributions, expectations, etc. are then
determined from these probabilities in the obvious manner."

"For every event, we can also identify the nodes where the very next transition determines whether a
given event will not occur. These are the critical nodes. Formally, given the min-cut for an event,
we define the critical set as the set of all nodes that are parents of a node in the false set. They are
highlighted in purple in Figure 2. The critical set can be thought of as the collection of mechanisms
in the tree that we need to manipulate in order to bring about a given event. Critical nodes are the
Markov blankets: all the variables bound within a path from the root to the critical node constitute the
“exogenous variables” for the mechanisms downstream. They are (implicitly) used in defining the
three operations of the causal hierarchy [2] presented later."

"A statement such as “the event where Y = 1 precedes Z = 0”, written Y = 1 ≺ Z = 0, cannot be stated logically. Rather, it is a causal statement that requires the causal relations provided in the probability tree."

Wow! They actually formally show how to calculate the causal hierarchy for and, or, and not!

Algorithms about O(N) where N is the number of nodes (recursive descent down the tree).

Great reference list! Lots of Pearl.

[Github link](https://github.com/deepmind/deepmind-research/tree/master/causal_reasoning) with a Google Collab.

---
