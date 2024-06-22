---
layout: default
title: Philosopher Scholar - Artificial Intelligence
permalink: /ai/coolAIarticles/
---

# Cool AI Articles

It's been a while since I posted about articles. Since then Large Language Models (LLMs) have taken the world by storm. I see a deluge of articles related to LLMs. Are they really the next generation of AI or temporary hype?

---

### [From Word Models to World Models: Translating from Natural Language to the Probabilistic Language of Thought](https://arxiv.org/abs/2306.12672)
Submitted 22 of June 2023

The paper is actually quite long. He also presented this as [a lecture on YouTube](https://www.youtube.com/watch?v=mvDxzmMpvl8). The work is fascinating as it bridges a major gap in current LLMs - world models. In fact Yan LeCunn criticizes LLM work strongly due to a lack of world modeling which will be essential for agents to act and reason about the world in a human way. Well this could solve the issue by connecting LLMs with probabilistic programming. 

From the abstract: "In this paper, we propose rational meaning construction, a computational framework for language-informed thinking that combines neural language models with probabilistic models for rational inference...We illustrate our framework through examples covering four core domains from cognitive science: probabilistic reasoning, logical and relational reasoning, visual and physical reasoning, and social reasoning."

You can get Bayesian inference from the probabilistic models and a distribution over possibel worlds. Amazing. 

---

### [The Platonic Representation Hypothesis](https://arxiv.org/abs/2405.07987)
(Submitted on 13 May 2024)

Wow, this paper is mind-blowing. The main gist: if you have a vision model with representation X and a text-based model with representation Y, both representations converge. The authors hypothesize the models are overlapping on the underlying reality, Z. "We hypothesize that this convergence is driving toward a shared statistical model of reality, akin to Plato's concept of an ideal reality." Always great to see philosophy pop up in machine learning!

As scale increases the representation of reality gets better. "As models are trained on more data and for more tasks, they require representations that capture more and more information about Z, and hence alignment toward Z increases toward a convergent point as a function of scale."

#### The Multitask Scaling Hypothesis
> There are fewer representations that are competent for N tasks than there are for M < N tasks. As we train more general models that solve more tasks at once, we should expect fewer possible solutions.

There are some great visuals to show this intuitively as well. 

#### The Capacity Hypothesis
> Bigger models are more likely to converge to a shared representation than smaller models.

#### The Simplicity Bias Hypothesis
> Deep networks are biased toward finding simple fits to the data, and the bigger the model, the stronger the bias. Therefore, as models get bigger, we should expect convergence to a smaller solution space.

So this paper is in line with the idea of "scale is all you need" for greater intelligence. However they note that what architecture you use determines efficiency in scaling.

There is transfer across modalities, so images help text and vice versa. "In theory, there should be some conversion ratio: a pixel is worth _a_ words for training LLMs, and a word is worth _b_ pixels for training vision models." Whoa, so the data wall can be climbed. Even if we already used all of the text data on the internet, LLMs can be leveraged yet again with all video data available. Similarly it appears more modalities constrain the hypothesis space to more simple and optimal solutions. This could explain why organisms have so many sense organs. Each sense helps to constrain the solution space. We can start adding more senses to AI, speech, vision, language, hearing, robotics, etc. We could even add senses like sonar and ultraviolet light. This could all models to converge faster. 

"Scaling may reduce hallucination and bias... Our hypothesis implies that, while this may be true, we should expect larger models to amplify bias less. This does not mean bias will be removed, rather that the model’s biases will more accurately reflect the data’s biases, rather than exacerbating them."

There are counterexamples and limitations. One aspect is not all models are converging. This could be due to the architectures and input. If the input doesn't share information between modalities then convergence is unlikely. 

But wait, we're getting close to reality? How does this compare to works like The Case Against Reality where we're optimized for fitness and not viewing reality at all? Well, there's a hint in the paper:

"Our argument only holds for intelligences that are optimized to perform well on many tasks. We have argued that a representation of reality is a structure that is useful across many tasks, but for any special purpose there may be shortcuts, or even effective representations detached from reality. Such shortcuts may be more efficient and necessary for continued improvements in specific domains. This will become more relevant if continued scaling comes up against boundary conditions around resources like energy and compute."

We humans pride ourselves on the complexity of our lives given the small energy required to run our brains. Perhaps much of our intelligence is actually quite specialized. Many of our perceptual modules might contain shortcuts. This would explain how we can be more optimized for fitness yet make some trade off with generality. Maybe we really are getting closer to reality at least through aggregated science and philosophy which connects us through time and life. 

Gosh, such fascinating work. I hope it gets supported! Yet again more arguments towards AI being closer to reality than we ever could be. 

---

These are some older papers.

---
### [A simple neural network module for relational reasoning](https://arxiv.org/abs/1706.01427)
(Submitted on 5 Jun 2017)

Relational reasoning is a central component of generally intelligent behavior, but has proven difficult for neural networks to learn. In this paper we describe how to use Relation Networks (RNs) as a simple plug-and-play module to solve problems that fundamentally hinge on relational reasoning. We tested RN-augmented networks on three tasks: visual question answering using a challenging dataset called CLEVR, on which we achieve state-of-the-art, super-human performance; text-based question answering using the bAbI suite of tasks; and complex reasoning about dynamic physical systems. Then, using a curated dataset called Sort-of-CLEVR we show that powerful convolutional networks do not have a general capacity to solve relational questions, but can gain this capacity when augmented with RNs. Our work shows how a deep learning architecture equipped with an RN module can implicitly discover and learn to reason about entities and their relations.

---

### [Look, Listen and Learn](https://arxiv.org/abs/1705.08168)
last revised 1 Aug 2017 (this version, v2)

We consider the question: what can be learnt by looking at and listening to a large number of unlabelled videos? There is a valuable, but so far untapped, source of information contained in the video itself -- the correspondence between the visual and the audio streams, and we introduce a novel "Audio-Visual Correspondence" learning task that makes use of this. Training visual and audio networks from scratch, without any additional supervision other than the raw unconstrained videos themselves, is shown to successfully solve this task, and, more interestingly, result in good visual and audio representations. These features set the new state-of-the-art on two sound classification benchmarks, and perform on par with the state-of-the-art self-supervised approaches on ImageNet classification. We also demonstrate that the network is able to localize objects in both modalities, as well as perform fine-grained recognition tasks.

---

### [Measuring abstract reasoning in neural networks](https://arxiv.org/abs/1807.04225)
(Submitted on 11 Jul 2018)

> Whether neural networks can learn abstract reasoning or whether they merely rely on superficial statistics is a topic of recent debate. Here, we propose a dataset and challenge designed to probe abstract reasoning, inspired by a well-known human IQ test. To succeed at this challenge, models must cope with various generalisation "regimes" in which the training and test data differ in clearly-defined ways. We show that popular models such as ResNets perform poorly, even when the training and test sets differ only minimally, and we present a novel architecture, with a structure designed to encourage reasoning, that does significantly better. When we vary the way in which the test questions and training data differ, we find that our model is notably proficient at certain forms of generalisation, but notably weak at others. We further show that the model's ability to generalise improves markedly if it is trained to predict symbolic explanations for its answers. Altogether, we introduce and explore ways to both measure and induce stronger abstract reasoning in neural networks. Our freely-available dataset should motivate further progress in this direction.

There's also an [introductory article from their website, deepmind](https://deepmind.com/blog/measuring-abstract-reasoning/).

> To understand why abstract reasoning is critical for general intelligence, consider Archimedes’ famous “Eureka!” moment: by noticing that the volume of an object is equivalent to the volume of water that the object displaces, he understood volume at a conceptual level, and was therefore able to reason about the volume of other irregularly shaped objects.
We would like AI to have similar capabilities. While current systems can defeat world champions in complicated strategic games, they often struggle on other apparently simple tasks, especially when an abstract concept needs to be discovered and reapplied in a new setting. For example, if specifically trained to only count triangles, then even our best AI systems can still fail to count squares, or any other previously unencountered object.

---

### [Neural Arithmetic Logic Units](https://arxiv.org/abs/1808.00508)
(Submitted on 1 Aug 2018)

> Neural networks can learn to represent and manipulate numerical information, but they seldom generalize well outside of the range of numerical values encountered during training. To encourage more systematic numerical extrapolation, we propose an architecture that represents numerical quantities as linear activations which are manipulated using primitive arithmetic operators, controlled by learned gates. We call this module a neural arithmetic logic unit (NALU), by analogy to the arithmetic logic unit in traditional processors. Experiments show that NALU-enhanced neural networks can learn to track time, perform arithmetic over images of numbers, translate numerical language into real-valued scalars, execute computer code, and count objects in images. In contrast to conventional architectures, we obtain substantially better generalization both inside and outside of the range of numerical values encountered during training, often extrapolating orders of magnitude beyond trained numerical ranges.

[Simple guide to Neural Arithmetic Logic Units (NALU): Explanation, Intuition and Code](https://medium.com/mlreview/simple-guide-to-neural-arithmetic-logic-units-nalu-explanation-intuition-and-code-64bc22605712)

---

### [A novel approach to neural machine translation](https://code.fb.com/ml-applications/a-novel-approach-to-neural-machine-translation/) (FAIR)
MAY 9, 2017

> Today, the Facebook Artificial Intelligence Research (FAIR) team [published research results](https://arxiv.org/abs/1705.03122) using a novel convolutional neural network (CNN) approach for language translation that achieves state-of-the-art accuracy at nine times the speed of recurrent neural systems.1 Additionally, the FAIR sequence modeling toolkit (fairseq) source code and the trained systems are available under an open source license on [GitHub](https://github.com/facebookresearch/fairseq) so that other researchers can build custom models for translation, text summarization, and other tasks.

---

[Unsupervised machine translation: A novel approach to provide fast, accurate translations for more languages](https://code.fb.com/ai-research/unsupervised-machine-translation-a-novel-approach-to-provide-fast-accurate-translations-for-more-languages/)
POSTED ON AUG 31, 2018

> Our [new approach](https://arxiv.org/abs/1804.07755) (Phrase-Based & Neural Unsupervised Machine Translation) provides a dramatic improvement over previous state-of-the-art unsupervised approaches and is equivalent to supervised approaches trained with nearly 100,000 reference translations. To give some idea of the level of advancement, an improvement of 1 BLEU point (a common metric for judging the accuracy of MT) is considered a remarkable achievement in this field; our methods showed an improvement of more than 10 BLEU points.

---

### [Unsupervised word embeddings capture latent knowledge from materials science literature](https://www.nature.com/articles/s41586-019-1335-8.epdf?referrer_access_token=E_gxidZzqpBnSXCFVd0VHNRgN0jAjWel9jnR3ZoTv0P9QxlcO86f_GXZRxwYijrqa11Mx55SgniZXv55YKOR_sn816NK2x0O46Vim16XrS-SjyP9GMXeDQinUN75ES6enlxK__J5UabR6JdgR19bZSVLL5ZsK8146qMcipEbItW65C8aSk29Q_BfrKz4Gb5-kjz3m7dIaoRxs3e1I6qW4x23kzzVbKCK6isCLQOmMBOsANyYUBJYzqcqggABZCtnjrOFA-c0x8VdHOyno8vByCKqhWEdnq4Xbiztsh3zveQOvqeMUxnWHSjhVHUHsIXdb4mIC62ZNTY3aesjgkjKEWrx9KNNArDa2rgCEiL6mNwFPdqZPj0YTrhkOVfsYtm1hYSLIQQ7hgnoLl4WAgMpakaRVGz6RFCmp6MN6zooUKgpznSFcQELGbYUtyXAOPko&tracking_referrer=www.vice.com)
July 4th, 2019

> Furthermore, we demonstrate that an unsupervised method can recommend materials for functional applications several years before their discovery. This suggests that latent knowledge regarding future discoveries is to a large extent embedded in past publications. Our findings highlight the possibility of extracting knowledge and relationships from the massive body of scientific literature in a collective manner, and point towards a generalized approach to the mining of scientific literature.

Gotta do this with philosophy!

---

### [AI Has Already Taken Over. It’s Called the Corporation.](/ai/AIasCorporations/)
Futurists warning about the threats of AI are looking in the wrong place. Humanity is already facing an existential threat from an artificial intelligence we created hundreds of years ago. It’s called the Corporation.
by Jeremy Lent

---

### [Growing Neural Cellular Automata](https://distill.pub/2020/growing-ca/)
Published Feb. 11, 2020

I end up wanting to send this to people and have to find it all over again! The visuals are really cool.

> Most multicellular organisms begin their life as a single egg cell - a single cell whose progeny reliably self-assemble into highly complex anatomies with many organs and tissues in precisely the same arrangement each time. The ability to build their own bodies is probably the most fundamental skill every living creature possesses. Morphogenesis (the process of an organism’s shape development) is one of the most striking examples of a phenomenon called self-organisation. Cells, the tiny building blocks of bodies, communicate with their neighbors to decide the shape of organs and body plans, where to grow each organ, how to interconnect them, and when to eventually stop. Understanding the interplay of the emergence of complex outcomes from simple rules and homeostatic feedback loops is an active area of research. What is clear is that evolution has learned to exploit the laws of physics and computation to implement the highly robust morphogenetic software that runs on genome-encoded cellular hardware.

---
