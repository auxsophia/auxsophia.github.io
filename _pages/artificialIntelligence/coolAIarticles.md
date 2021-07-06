---
layout: default
title: Philosopher Scholar - Artificial Intelligence
permalink: /ai/coolAIarticles/
---

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
