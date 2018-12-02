---
layout: default
title: Philosopher Scholar - Artificial Intelligence
permalink: /ai/
---

# [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)
[Outline of AI](https://en.wikipedia.org/wiki/Outline_of_artificial_intelligence)

[Provably Beneficial AI | Stuart Russell](https://www.youtube.com/watch?v=pARXQnX6QS8)
- Value misalignment
  - AI systems that incredibly good at achieving something other than what we really want
  - AI, economics, statistics, operations research, control theory all assume utility to be _exogenously specified_
- Instrumental goals
  - For _any primary goal_, the odds of success are improved by
    1. Maintaining one's own existence
    2. Acquiring more resources
  - With value misalignment, these lead to obvious problems
- Reasons not to pay attention:
  - Human-level AI will never happen
  - It's too soon to worry about it
    - 2066 asteroid collision: when exactly do we worry? (Sam Harris argument?)
    - When should we have worried about climate change?
  - It's like worrying about overpopulation on Mars
    - No, it's as if we were spending billions moving humanity to Mars with no plan for what to breathe
  - Just don't have explicit goals for the AI system
    - We need to steer straight, not remove the steering wheels
  - Don't worry, we'll just have human-AI teams
    - Value misalignment precludes teamwork
  - You can't control research
    - Yes, we can: we don't genetically engineer humans (SAD!)
  - You're just Luddites/anti-AI
  - Don't worry, we can just switch it off
    - As if a superintelligent entity would never think of that
  - Don't put in "human" goals like self-preservation
    - Death isn't bad per se. It's just hard to fetch the coffee after you're dead (see instrumental goals)
  - Don't mention risks, it might be bad for funding
    - See nuclear power, GMOs, tobacco, global warming

Center for Human-Compatible AI: reorient the general thrust of AI research towards provably beneficial systems

### Three simple ideas
1. The robot's only objective is to maximize the realization of human values
2. The robot is initially uncertain about what those values are
3. The best source of information about human values is human behavior

### Value alignment
- _Inverse reinforcement learning_: learn a value function by observing another agent's behavior
  - The value function is a succinct explanation for what the other agent is doing

### _Cooperative_ inverse reinforcement learning
- A 2-player game with "human" and "robot"
  - Human "knows" the value function (usually acts according to it)
- Optimal solutions have these properties:
  - Robot has an incentive to ask questions first
  - Human has an incentive to teach the robot

### The off-switch problem
- A robot, given an objective, has an incentive to disable its own off-switch
  - How can we prevent this?
  - Answer: robot isn't given an objective!
  - Instead, it must allow for uncertainty about the true human objective
    - The human will only switch off the robot if that leads to better outcomes for the true human objective
    - Theorem: it's *in the robot's interest* to allow it

### Uncertainty in objectives
- Largely ignored, even though uncertainty has been central to AI since early 1980's
- *Irreleveant* in standard decision problems...
  - Integrate over uncertainty and it is provably irrelevant because you will behave the same
- *...Unless* the environment provides further information about objectives
  - E.g., observable human actions, reward signals in RL

### Reward signals
- Wireheading
  - In a real RL problem, rewards come from environment
  - => RL agent hijacks the reward-generating mechanism
- Mathematical framework for RL is wrong: reward signals are _not_ actual rewards
  - A "reward signal" is a human action that provides _information_ about the true reward
  - Hijacking the mechanism _loses information_

## Provably beneficial AI
- Define a formal problem F that we assume the robot solves arbitrarily well
  - The robot is an F-solver, not just "AGI"
- Desired theorem: the human is provably better off with the robot
- Move the theoretical framework gradually towards reality

### Reasons for optimism
- Vast amounts of evidence for human behavior and _human attitudes towards that behavior_
- We need value alignment even for _subintelligent_ systems in human environments; strong economic incentives!
  - E.g., are all photo misclassification costs equal?

### Reasons for working hard
- Humans are nasty, irrational, inconsistent, weak-willed, computationally limited, and heterogeneous

## Practical projects
- It's hard to work on control of AGIs
- Okay, work on something simpler:
  - Intelligent personal assistant
  - Smart home
  - Etc.
- Simulation environments where real (simulated) disasters can happen

### Questions
- Can we change the way AI defines itself?
  - A civil engineer says "I design bridges," not "I design bridges that don't fall down"
  - Willingness to re-examine foundations
- How can we engage social scientists?
- Where do human value systems come from?
- Can AI optimize future social evolution?
- Will it make us better people?

# [3 principles for creating safer AI | Stuart Russell](https://www.youtube.com/watch?v=EBK-a94IFHY)
