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
- Video published on Jun 6, 2017

"...that reading is not yet happening in machines, at least with understanding. But that will happen, and when that happens, very soon afterwards, machines will have read everything that the human race has ever written. And that will enable machines, along with the ability to look further ahead than humans can, as we've already seen in Go, if they also have access to more information, they'll be able to make better decisions in the real world than we can. So is that a good thing? Well, I hope so.

Our entire civilization, everything that we value, is based on our intelligence. And if we had access to a lot more intelligence, then there's really no limit to what the human race can do. And I think this could be, as some people have described it, the biggest event in human history. So why are people saying things like this, that AI might spell the end of the human race?"

"Even if we could keep the machines in a subservient position, for instance, by _turning off the power_ at strategic moments, we should, as a species, feel greatly humbled." - Alan Turing 1951

> So here's another quotation: "We had better be quite sure that the purpose put into the machine is the purpose which we really desire." This was said by Norbert Wiener in 1960, shortly after he watched one of the very early learning systems learn to play checkers better than its creator. But this could equally have been said by King Midas. King Midas said, "I want everything I touch to turn to gold," and he got exactly what he asked for. That was the purpose that he put into the machine, so to speak, and then his food and his drink and his relatives turned to gold and he died in misery and starvation. So we'll call this "the King Midas problem" of stating an objective which is not, in fact, truly aligned with what we want. In modern terms, we call this "the value alignment problem."

> So this single-minded pursuit in a very defensive mode of an objective that is, in fact, not aligned with the true objectives of the human race -- that's the problem that we face. And in fact, that's the high-value takeaway from this talk. If you want to remember one thing, it's that you can't fetch the coffee if you're dead.

> It's very simple. Just remember that. Repeat it to yourself three times a day.

> And in fact, this is exactly the plot of "2001: [A Space Odyssey]" HAL has an objective, a mission, which is not aligned with the objectives of the humans, and that leads to this conflict. Now fortunately, HAL is not superintelligent. He's pretty smart, but eventually Dave outwits him and manages to switch him off. But we might not be so lucky. So what are we going to do?

> I'm trying to redefine AI to get away from this classical notion of machines that intelligently pursue objectives. There are three principles involved. The first one is a principle of altruism, if you like, that the robot's only objective is to maximize the realization of human objectives, of human values. And by values here I don't mean touchy-feely, goody-goody values. I just mean whatever it is that the human would prefer their life to be like. And so this actually violates Asimov's law that the robot has to protect its own existence. It has no interest in preserving its existence whatsoever.

> The second law is a law of humility, if you like. And this turns out to be really important to make robots safe. It says that the robot does not know what those human values are, so it has to maximize them, but it doesn't know what they are. And that avoids this problem of single-minded pursuit of an objective. This uncertainty turns out to be crucial.

> Now, in order to be useful to us, it has to have some idea of what we want. It obtains that information primarily by observation of human choices, so our own choices reveal information about what it is that we prefer our lives to be like. So those are the three principles.

3. Human behavior provides information about human values
- Learn to predict which life each human will prefer

"The real difficulty is **us**."

You could come home after a hard day's work, and the computer says, "Long day?"

"Yes, I didn't even have time for lunch."

"You must be very hungry."

"Starving, yeah. Could you make some dinner?"

"There's something I need to tell you."

(Laughter)

"There are humans in South Sudan who are in more urgent need than you."

(Laughter)

"So I'm leaving. Make your own dinner."

(Laughter)

So we have to solve these problems, and I'm looking forward to working on them.

### Changing AI
- We require provably beneficial AI
- The key components are
  - purely altruistic robots,
  - with uncertain **objectives**,
  - that learn more by observing (all) humans

Question: And you couldn't just boil it down to one law, you know, hardwired in: "if any human ever tries to switch me off, I comply. I comply."

Stuart Russell: Absolutely not. That would be a terrible idea. So imagine that you have a self-driving car and you want to send your five-year-old off to preschool. Do you want your five-year-old to be able to switch off the car while it's driving along? Probably not. **So it needs to understand how rational and sensible the person is. The more rational the person, the more willing you are to be switched off.** If the person is completely random or even malicious, then you're less willing to be switched off.
