---
layout: default
title: Philosopher Scholar - The Meaning of Life
permalink: /meaningOfLife_4/
---

# The Drive of Intelligent Agents and Subjective Meaning

You can watch the video for this page here:

{:refdef: style="text-align: center;"}
<iframe width="680" height="480" src="https://youtube.com/embed/ql7OYP6mLqI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
{:refdef }

So far much of this explanation is objective. For many this will not help our personal woes or provide direction. We expect the meaning of life to tell us what we _should_ be doing. First we will attempt to explain why we are currently doing what we are doing.

I found the work of Juergen Schmidhuber incredible. In his paper, [Driven by Compression Progress: A Simple Principle Explains Essential Aspects of Subjective Beauty, Novelty, Surprise, Interestingness, Attention, Curiosity, Creativity, Art, Science, Music, Jokes](https://arxiv.org/abs/0812.4360), Schmidhuber gives an algorithmic framework of the drive of all intelligent creatures.

The abstract:
> I argue that data becomes temporarily interesting by itself to some self-improving, but computationally limited, subjective observer once he learns to predict or compress the data in a better way, thus making it subjectively simpler and more beautiful. Curiosity is the desire to create or discover more non-random, non-arbitrary, regular data that is novel and surprising not in the traditional sense of Boltzmann and Shannon but in the sense that it allows for compression progress because its regularity was not yet known. This drive maximizes interestingness, the first derivative of subjective beauty or compressibility, that is, the steepness of the learning curve. It motivates exploring infants, pure mathematicians, composers, artists, dancers, comedians, yourself, and (since 1990) artificial systems.

A simple example of compression is:
“For example, if you receive a data package which contains "AAAAABBBB", you could compress that into "5A4B", which has the same meaning but takes up less space. This type of compression is called "run-length encoding", because you define how long the "run" of a character is. In the above example, there are two runs: a run of 5 A's, and another of 4 B's,” [Data Compression - Wikipedia](https://simple.wikipedia.org/wiki/Data_compression).

In the human case, our data stream is not a sequence of letters but the whole of our experience, our thoughts, feelings, and sensations. Our encoding, decoding, and compression scheme is still not fully known. However, the algorithmic framework is given in section 1.2 as follows (with citations removed):

1. **Store everything**. During interaction with the world, store the entire raw history of actions and sensory observations including reward signals—the data is holy as it is the only basis of all that can be known about the world. To see that full data storage is not unrealistic: A human lifetime rarely lasts much longer than 3×10^9 seconds. The human brain has roughly 10^10 neurons, each with 10^4 synapses on average. Assuming that only half of the brain’s capacity is used for storing raw data, and that each synapse can store at most 6 bits, there is still enough capacity to encode the lifelong sensory input stream with a rate of roughly 10^5 bits/s, comparable to the demands of a movie with reasonable resolution. The storage capacity of affordable technical systems will soon exceed this value. If you can store the data, do not throw it away!

2. **Improve subjective compressibility**. In principle, any regularity in the data history can be used to compress it. The compressed version of the data can be viewed as its simplifying explanation. Thus, to better explain the world, spend some of the computation time on an adaptive compression algorithm trying to partially compress the data. For example, an adaptive neural network may be able to learn to predict or postdict some of the historic data from other historic data, thus incrementally reducing the number of bits required to encode the whole.

3. **Let intrinsic curiosity reward reflect compression progress**. The agent should monitor the improvements of the adaptive data compressor: whenever it learns to reduce the number of bits required to encode the historic data, generate an intrinsic reward signal or curiosity reward signal in proportion to the learning progress or compression progress, that is, the number of saved bits.

4. **Maximize intrinsic curiosity reward**. Let the action selector or controller use a general Reinforcement Learning (RL) algorithm (which should be able to observe the current state of the adaptive compressor) to maximize expected reward, including intrinsic curiosity reward. To optimize the latter, a good RL algorithm will select actions that focus the agent’s attention and learning capabilities on those aspects of the world that allow for finding or creating new, previously unknown but learnable regularities. In other words, it will try to maximize the steepness of the compressor’s learning curve. This type of active unsupervised learning can help to figure out how the world works.

Section 1.3 discusses the relation to external reward. The description given applies to internal rewards, curiosity, satisfaction, but "Of course, the real goal of many cognitive systems is not just to satisfy their curiosity, but to solve externally given problems. Any formalizable problem can be phrased as an RL problem for an agent living in a possibly unknown environment, trying to maximize the future external reward expected until the end of its possibly finite lifetime."

In many contexts, we live in a rare reward environment. One way of focusing and directing our actions is through our internal rewards of compression until an external (rare) reward is reached.

Section 2 discusses the consequences of the compression progress drive which Schmidhuber argues intelligence and cognition are by-products of.

2.1 Compact Internal Representations or Symbols as By-Products
of Efficient History Compression

> "To compress the history of observations so far, the compressor (say, a predictive neural network) will automatically create internal representations or _symbols_ (for example, patterns across certain neural feature detectors) for things that frequently repeat themselves. Even when there is limited predictability, efficient compression can still be achieved by assigning short codes to events that are predictable with high probability. For example, the sun goes up every day. Hence it is efficient to create internal symbols such as _daylight_ to describe this repetitive aspect of the data history by a short reusable piece of internal code, instead of storing just the raw data. In fact, predictive neural networks are often observed to create such internal (and hierarchical) codes as a by-product of minimizing their prediction error on the training data."

2.2 Consciousness as a Particular By-Product of Compression
> "There is one thing that is involved in all actions and sensory inputs of the agent, namely, the agent itself. To efficiently encode the entire data history, it will profit from creating some sort of internal _symbol_ or code (e. g., a neural activity pattern) representing the agent itself. Whenever this representation is actively used, say, by activating the corresponding neurons through new incoming sensory inputs or otherwise, the agent could be called _self-aware_ or _conscious_.
This straight-forward explanation apparently does not abandon any essential aspects of our intuitive concept of consciousness, yet seems substantially simpler than other recent views. In the rest of this paper we will not have to attach any particular mystic value to the notion of consciousness—in our view, it is just a natural by-product of the agent’s ongoing process of problem solving and world modeling through data compression, and will not play a prominent role in the remainder of this paper."

2.3 The Lazy Brain’s Subjective, Time-Dependent Sense of Beauty

Schmidhuber argues our subjective sense of beauty is directly proportional to the number of bits required to encode an experience. Think of human faces. One way to efficiently encode human faces is to build a _prototype_ face. New faces are compared to the prototype which has proportions as an average of every face seen. The more a face is like the prototype, the less information is needed to encode the face, thus the face feels beautiful to the observer. "...in principle, the compressor may exploit any regularity for reducing the number of bits required to store the data."

A face which is symmetrical on each side from the center will be very beautiful if the encoding of the face can be compressed to nearly half the size since the face can mostly be mirrored with one half of the face.

> "Generally speaking, among several sub-patterns classified as _comparable_ by a given observer, the subjectively most beautiful is the one with the simplest (shortest) description, given the observer’s current particular method for encoding and memorizing it. For example, mathematicians find beauty in a simple proof with a short description in the formal language they are using. Others like geometrically simple, aesthetically pleasing, low-complexity drawings of various objects.

> This immediately explains why many human observers prefer faces similar to their own. What they see every day in the mirror will influence their subjective prototype face, for simple reasons of coding efficiency."

2.4 Subjective Interestingness as First Derivative of Subjective Beauty: The Steepness of the Learning Curve

> "What’s beautiful is not necessarily interesting. A beautiful thing is interesting only as long as it is new, that is, as long as the algorithmic regularity that makes it simple has not yet been fully assimilated by the adaptive observer who is still learning to compress the data better...the first derivative of subjective beauty: as the learning agent improves its compression algorithm, formerly apparently random data parts become subjectively more regular and beautiful, requiring fewer and fewer bits for their encoding. As long as this process is not over the data remains interesting and rewarding."

Think of a [first derivative](https://www.mathsisfun.com/calculus/derivatives-introduction.html) as finding the slope of a line at a single point. The slope tells us the rate of change. In this case, interestingness is the rate of expected compression.

2.6 True Novelty & Surprise vs Traditional Information Theory

Imagine two visual observers where one is kept completely in the dark and one is exposed to a screen of random white noise. The darkness is extremely compressible as it's always the same. The noise is "...highly unpredictable and fundamentally incompressible data. In both cases the data is boring as it does not allow for further compression progress."

2.7 Attention / Curiosity / Active Experimentation

> "In absence of external reward, or when there is no known way to further increase the expected external reward, our controller essentially tries to maximize _true novelty or interestingness_, the _first derivative_ of subjective beauty or compressibility, the steepness of the learning curve. It will do its best to select action sequences expected to create observations yielding maximal expected future compression _progress_, given the limitations of both the compressor and the compressor improvement algorithm. It will learn to focus its attention and its actively chosen experiments on things that are currently still incompressible but are expected to become compressible/predictable through additional learning. It will get bored by things that already are subjectively compressible. It will also get bored by things that are currently incompressible but will apparently remain so, given the experience so far, or where the costs of making them compressible exceed those of making other things compressible, etc."

Here we see the drive to action observed of exploring human infants and other intelligent agents. Why do scientists work on smaller, specific problems instead of bigger, universal problems? An explanation is given above, the scientists expect the problem will not be compressible in the near future, so they lose attention and curiosity in that problem.

2.8 Discoveries

"An unusually large compression breakthrough deserves the name _discovery_. For example, as mentioned in the introduction, the simple law of gravity can be described by a very short piece of code, yet it allows for greatly compressing all previous observations of falling apples and other objects."

2.9 Beyond Standard Unsupervised Learning

> "Where there is predictability, compression can be achieved by assigning short codes to those parts of the observations that are predictable from previous observations with high probability. Generally speaking we may say that a major goal of traditional unsupervised learning is to improve the compression of the observed data, by discovering a program that computes and thus explains the history (and hopefully does so quickly) but is clearly shorter than the shortest previously known program of this kind.
Traditional unsupervised learning is not enough though—it just analyzes and encodes the data but does not choose it. We have to extend it along the dimension of active action selection, since our unsupervised learner must also choose the actions that influence the observed data, just like a scientist chooses his experiments, a baby its toys, an artist his colors, a dancer his moves, or any attentive system its next sensory input. That’s precisely what is achieved by our RL-based framework for curiosity and creativity."

2.10 Art & Music as By-Products of the Compression Progress Drive

> "Good observer-dependent art deepens the observer’s insights about this world or possible worlds, unveiling previously unknown regularities in compressible data, connecting previously disconnected patterns in an initially surprising way that makes the combination of these patterns subjectively more compressible (art as an eye-opener), and eventually becomes known and less interesting. I postulate that the active creation and attentive perception of all kinds of artwork are just by-products of our principle of interestingness and curiosity yielding reward for compressor improvements...
Artificial or human observers must perceive art sequentially, and typically also actively, e.g., through a sequence of attention-shifting eye saccades or camera movements scanning a sculpture, or internal shifts of attention that filter and emphasize sounds made by a pianist, while surpressing background noise. Undoubtedly many derive pleasure and rewards from perceiving works of art, such as certain paintings, or songs. But different subjective observers with different sensory apparati and compressor improvement algorithms will prefer different input sequences. Hence any objective theory of what is good art must take the subjective observer as a parameter, to answer questions such as: Which sequences of actions and resulting shifts of attention should they execute to maximize their pleasure? According to our principle they should select one that maximizes the quickly learnable compressibility that is new, relative to their current knowledge and their (usually limited) way of incorporating / learning / compressing new data."

2.15 How Artists and Scientists are Alike

> "From our perspective, scientists are very much like artists. They actively select experiments in search for simple but new laws compressing the resulting observation history. In particular, the _creativity_ of painters, dancers, musicians, pure mathematicians, physicists, can be viewed as a mere by-product of our curiosity framework based on the compression progress drive. All of them try to create new but non-random, non-arbitrary data with surprising, previously unknown regularities. For example, many physicists invent experiments to create data governed by previously unknown laws allowing to further compress the data. On the other hand, many artists combine well-known objects in a subjectively novel way such that the observer’s subjective description of the result is shorter than the sum of the lengths of the descriptions of the parts, due to some previously unnoticed regularity shared by the parts.
What is the main difference between science and art? The essence of science is to _formally nail down_ the nature of compression progress achieved through the discovery of a new regularity. For example, the law of gravity can be described by just a few symbols. In the fine arts, however, compression progress achieved by observing an artwork combining previously disconnected things in a new way (art as an eye-opener) may be subconscious and not at all formally describable by the observer, who may _feel_ the progress in terms of intrinsic reward without being able to say exactly which of his memories became more subjectively compressible in the process.
The framework in the appendix is sufficiently formal to allow for implementation of our principle on computers. The resulting artificial observers will vary in terms of the computational power of their history compressors and learning algorithms. This will influence what is good art/science to them, and what they find interesting."

2.16 Jokes and Other Sources of Fun

> "Just like other entertainers and artists, comedians also tend to combine well-known concepts in a novel way such that the observer’s subjective description of the result is shorter than the sum of the lengths of the descriptions of the parts, due to some previously unnoticed regularity shared by the parts."

3.3 Reward for Relative Entropy between Agent’s Prior and Posterior (1995)

Our intrinsic reward can be related to Bayesian inference in the difference between prior and posterior odds.

5 Conclusion & Outlook

> "We pointed out that a surprisingly simple algorithmic principle based on the notions of data compression and data compression _progress_ informally explains fundamental aspects of attention, novelty, surprise, interestingness, curiosity, creativity, subjective beauty, jokes, and science & art in general. The crucial ingredients of the corresponding _formal_ framework are (1) a continually improving predictor or compressor of the continually growing data history, (2) a computable measure of the compressor’s progress (to calculate intrinsic rewards), (3) a reward optimizer or reinforcement learner translating rewards into action sequences expected to maximize future reward."

---

With this framework, many difficult questions can now be answered. Notice the framework contributes to the compression of our history of experience with intelligent agents. We can understand and predict the actions of intelligent agents within the context of the framework.

Why are some experiences beautiful to some and not to others? - Because each individual has their own unique experiences which determines their ability to compress new experiences.

Is beauty subjective or objective? - Both. Aspects of beauty will be objective such as geometric regularities which reduce the size of the compressed experience, therefore creating a strong sense of beauty. However, each person has a unique perspective due to their experience and compression ability.

Why are jokes funny to some people and not others? - Jokes combine elements into a previously unrecognized regularity in a connection we haven't experienced before. There are jokes specific to a field or time which are unfunny to those not steeped in similar experiences. The reason is clear, jokes appear unfunny when there is no connection to be made in the history of the observer or the connection is already obvious or known. This also explains why old jokes aren't funny once learned. So much of a joke depends on the _punchline_. The punchline, the conclusion of the joke, is often a shorter description than the entire joke. Explaining a joke almost always takes away the humor. We see that a joke is unfunny when explained because the punchline is now the opposite, it's a much longer description of why it's funny and the opposite of compressed.

The reach of the explanatory framework is far and wide with a nearly unending list of examples. Let us return to the meaning of life and apply the framework.

The sense of the meaning of life is dependent on the compression of our history. We look for a unifying explanation for our past experiences and direction of our future.

When our past feels random we are unable to compress the experience in a connected way leading us to a feeling of absurdity in our existence. There appears to be no coherent direction. At this stage, we use words like absurd and random to describe those aspects of our lives which cannot be compressed further. Notice how the framework explains why we lose interest and attention in the question of meaning and often give up the search: the unifying answer appears unobtainable given the time and information we have. Our attention is drawn to immediate or answerable concerns.

Recognize a subjective sense of meaning in life at this time can only come from within. Only you have access to the history of your experience. Only you can compress your life in a subjectively meaningful way. Others can give you ideas and direction, but you must do the information processing yourself. The deep answer to your life can be explained to you by someone else, but that is them observing the information they experience of you and what you are able to express to them, then they apply their internal compressor to condense the history of your experience. Even if their compressed version is meaningful to you, you must do the work of unifying your past experiences in your mind.

The existentialist _Jean-Paul Sartre_ said "existence precedes essence." Many have lived and died believing the opposite, essence precedes existence. Essence is purpose, what we were made to do, meant to do, but we were not meant or designed for any purpose. Our essence is the unifying direction of our choices. We evolved under the constraints of natural selection with all kinds of drives, urges, and desires which lead to exactly the state of the world at every moment. We exist before we have a true essence. Our essence is given to ourselves from the compression of our personal history. We all shape our past, present, and future.

### If an intelligent agent wants meaning, they will have to reflect on their history to identify meaningful experiences. If an intelligent agent wants more meaningful direction and control of their future, they must work to adapt their internal representations of the world to direct their actions toward meaning, a cause and effect relationship of their past experiences cohering with expected futures.

Notice we can give multiple descriptions of the same data. From many equal interpretations we choose one. Our choices can change and evolve over time, but how do we choose an interpretation? How should we? If we want a meaningful life, we should choose a description of our history which opens opportunity for further growth and compression.

While we have talked much about meaning in terms of cause and effect, there are other types of meaning, interdependence. I recommend The Great Courses _The Meaning of Life: Perspectives from the World's Great Intellectual Traditions_ by Professor Jay L. Garfield, particularly his lecture on the Buddha. The below is referenced from lecture 34 on His Holiness the Dalai Lama XIV.

### 3 types of the interdependence

Causal factors:

Objective meaning, the meaning of cause and effect. We can have a mapping of one cause to one effect, or multiple causes to one effect, or one to multiple, or multiple to multiple.

Part-whole:

The interdependence of structures. We experience part-whole interdependence as self-organized dissipative structures. Each part of you is a cell, but a person is not a cell. A person is the whole of one body. We have an influence on each cell and each cell has an influence on us. Much of this interdependence is a function of how our bodies are organized. The influence is about energy flow. How you breathe changes the function of your cells. Top-down control is the whole influencing the parts. Bottom-up control is the parts influencing the whole. You can hold your breath (top-down), but your cells will send hunger for air (bottom-up). We are not just one person. We are a part of lower and higher levels of systems. In ecosystems, as the complexity increases the parts become more dependent on the whole.

Conceptual imputation:

Imputation is filling in missing data. We smooth over reality to make our processing more comfortable. Imputation works because our outcomes are still accurate or effective. Concepts are ideas. Conceptual imputation is when we have learned an idea which covers the gaps of reality, raw data.

{:refdef: style="text-align: center;"}
[Part 4](/meaningOfLife_3/) • [Part 6](/meaningOfLife_5/)
{:refdef }
