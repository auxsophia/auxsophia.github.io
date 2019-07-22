---
layout: default
title: Philosopher Scholar - AI and Global Warming
permalink: /ai/AIandGlobalWarming/
---



---

### [Training a single AI model can emit as much carbon as five cars in their lifetimes](https://www.technologyreview.com/s/613630/training-a-single-ai-model-can-emit-as-much-carbon-as-five-cars-in-their-lifetimes/)
Deep learning has a terrible carbon footprint.

by Karen Hao

Jun 6, 2019

"The artificial-intelligence industry is often compared to the oil industry: once mined and refined, data, like oil, can be a highly lucrative commodity. Now it seems the metaphor may extend even further. Like its fossil-fuel counterpart, the process of deep learning has an outsize environmental impact.

In a [new paper](https://arxiv.org/abs/1906.02243), researchers at the University of Massachusetts, Amherst, performed a life cycle assessment for training several common large AI models. They found that the process can emit more than 626,000 pounds of carbon dioxide equivalent—nearly five times the lifetime emissions of the average American car (and that includes manufacture of the car itself).

...

The paper specifically examines the model training process for natural-language processing (NLP), the subfield of AI that focuses on teaching machines to handle human language. In the last two years, the NLP community has reached several noteworthy performance milestones in machine translation, sentence completion, and other standard benchmarking tasks.

...

The researchers looked at four models in the field that have been responsible for the biggest leaps in performance: the Transformer, ELMo, BERT, and GPT-2. They trained each on a single GPU for up to a day to measure its power draw. They then used the number of training hours listed in the model’s original papers to calculate the total energy consumed over the complete training process. That number was converted into pounds of carbon dioxide equivalent based on the average energy mix in the US, which closely matches the energy mix used by Amazon’s AWS, the largest cloud services provider.

They found that the computational and environmental costs of training grew proportionally to model size and then exploded when additional tuning steps were used to increase the model’s final accuracy. In particular, they found that a tuning process known as neural architecture search, which tries to optimize a model by incrementally tweaking a neural network’s design through exhaustive trial and error, had extraordinarily high associated costs for little performance benefit. Without it, the most costly model, BERT, had a carbon footprint of roughly 1,400 pounds of carbon dioxide equivalent, close to a round-trip trans-America flight for one person.

What’s more, the researchers note that the figures should only be considered as baselines. “Training a single model is the minimum amount of work you can do,” says Emma Strubell, a PhD candidate at the University of Massachusetts, Amherst, and the lead author of the paper. In practice, it’s much more likely that AI researchers would develop a new model from scratch or adapt an existing model to a new data set, either of which can require many more rounds of training and tuning.

To get a better handle on what the full development pipeline might look like in terms of carbon footprint, Strubell and her colleagues used a model they’d produced in a previous paper as a case study. They found that the process of building and testing a final paper-worthy model required training 4,789 models over a six-month period. Converted to CO2 equivalent, it emitted more than 78,000 pounds and is likely representative of typical work in the field.

The significance of those figures is colossal—especially when considering the current trends in AI research. “In general, much of the latest research in AI neglects efficiency, as very large neural networks have been found to be useful for a variety of tasks, and companies and institutions that have abundant access to computational resources can leverage this to obtain a competitive advantage,” Gómez-Rodríguez says. “This kind of analysis needed to be done to raise awareness about the resources being spent [...] and will spark a debate.”

The results underscore another growing problem in AI, too: the sheer intensity of resources now required to produce paper-worthy results has made it increasingly challenging for people working in academia to continue contributing to research.

“This trend toward training huge models on tons of data is not feasible for academics—grad students especially, because we don’t have the computational resources,” says Strubell. “So there’s an issue of equitable access between researchers in academia versus researchers in industry.”

Strubell and her coauthors hope that their colleagues will heed the paper’s findings and help level the playing field by investing in developing more efficient hardware and algorithms.

Reddy agrees. “Human brains can do amazing things with little power consumption,” he says. “The bigger question is how can we build such machines.”"

---

### [Here are 10 ways AI could help fight climate change](https://www.technologyreview.com/s/613838/ai-climate-change-machine-learning/)
Machine learning has the potential to make some real inroads against our biggest threat.

by Karen Hao

Jun 20, 2019

"[The report](https://arxiv.org/abs/1906.05433) covers possible machine-learning interventions in 13 domains, from electricity systems to farms and forests to climate prediction. Within each domain, it breaks out the contributions for various subdisciplines within machine learning, including computer vision, natural-language processing, and reinforcement learning.

Recommendations are also divided into three categories: “high leverage” for problems well suited to machine learning where such interventions may have an especially great impact; “long-term” for solutions that won’t have payoffs until 2040; and “high risk” for pursuits that have less certain outcomes, either because the technology isn’t mature or because not enough is known to assess the consequences. Many of the recommendations also summarize existing efforts that are already happening but not yet at scale.

The report’s compilation was led by David Rolnick, a postdoctoral fellow at the University of Pennsylvania, and advised by several high-profile figures, including Andrew Ng, the cofounder of Google Brain and a leading AI entrepreneur and educator; Demis Hassabis, the founder and CEO of DeepMind; Jennifer Chayes, the managing director of Microsoft Research; and Yoshua Bengio, who recently won the Turing Award for his contributions to the field. While the researchers offer a very comprehensive list of some of the major areas where machine learning can contribute, they also note that it is not a silver bullet. Ultimately, policy will be the main driver for effective large-scale climate action."

1. Improve predictions of how much electricity we need

2. Discover new materials

3. Optimize how freight is routed

4. Lower barriers to electric-vehicle adoption

5. Help make buildings more efficient

6. Create better estimates of how much energy we are consuming

7. Optimize supply chains

8. Make precision agriculture possible at scale

9. Improve deforestation tracking

10. Nudge consumers to change how we shop

The authors of the paper created a website, [Climate Change + AI](https://www.climatechange.ai/) to spread awareness and centralize resources.

"Climate change is one of the greatest problems society has ever faced, with increasingly severe consequences for humanity as natural disasters multiply, sea levels rise, and ecosystems falter. Since climate change is a complex issue, action takes many forms, from designing smart electric grids to tracking greenhouse gas emissions through satellite imagery. While no silver bullet, machine learning can be an invaluable tool in fighting climate change via a wide array of applications and techniques. These applications require algorithmic innovations in machine learning and close collaboration with diverse fields and practitioners."

From the report, page 4:
"We emphasize that machine learning is not a silver bullet. The applications we highlight are impactful, but no one solution will “fix” climate change. There are also many areas of action where ML is inapplicable, and we omit these entirely. Furthermore, technology alone is not enough – technologies that would reduce climate change have been available for years, but have largely not been adopted at scale by society. While we hope that ML will be useful in reducing the costs associated with climate action, humanity also must decide to act."



---
