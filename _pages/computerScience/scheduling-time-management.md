---
layout: default
title: Philosopher Scholar - Scheduling Humans
permalink: /computer-science/scheduling-humans/
---

I'm currently reading selected parts of _Algorithms to Live By - The Computer Science of Human Decisions_ by Brian Christian and Tom Griffiths. The book is awesome so far. The only downside is they don't explicitly list their references in their work. It's just a long bibliography in the back. This is a break down of chapter 5 of their book on scheduling (time management).

> "How we spend our days is, of course, how we spend our lives." - Annie Dillard

Looking at other time-management guides:
- _Getting Things Done_ advocates immediately doing any task which takes two minutes or less as soon as it comes to mind
- _Eat The Frog!_ advises beginning with the most difficult task and moving toward easier and easier things
- _The Now Habit_ suggests first scheduling one's social engagements and leisure time and then filling the gaps with work - rather than the other way around

"Every guru has a different system, and it's hard to know who to listen to."

---

Time management became more rigorous in modern history with Frederick Taylor in 1874 who worked as a machinist. He rose through the ranks and became a foreman where he developed a discipline of time management he called "Scientific Management."

> Taylor created a planning office, at the heart of which was a billboard displaying the shop's schedule for all to see. The board depicted every machine in the shop, showing the task currently being carried out by that machine and all the tasks waiting for it.

This was further developed by Henry Gantt which turned into (yes, you guessed it) [Gantt charts](https://en.wikipedia.org/wiki/Gantt_chart).

> Taylor and Gantt made scheduling an object of study, and they gave it visual and conceptual form. But they didn't solve the fundamental problem of determining which schedules were best. The first hint that this problem even _could_ be solved wouldn't appear until several decades later in a 1954 paper published by RAND Corporation mathematician Selmer Johnson.

Johnson's problem was based on book binding where one machine printed the book and the other machine bound it. This is also adapted to an analogous problem of washing machines and loads of laundry.

> When you wash your clothes, they have to pass through the washer and the dryer in sequence, and different loads will take different amounts of time in each. A heavily soiled load might take longer to wash but the usual time to dry; a large load might take longer to dry but the usual time to wash. So, Johnson asked, if you have several loads of laundry to do on the same day, what's the best way to do them?

> His answer was that you should begin by finding the single step that takes the least amount of time-the load that will wash _or_ dry the quickest. If that shortest step involves the washer, plan to do that load _first_. If it involves the dryer, plan to do it _last_. Repeat this process for the remaining loads, working from the two ends of the schedule toward the middle.

> Intuitively, Johnson's algorithm works because regardless of how you sequence the loads, there's going to be some time at the start when the washer is running but not the dryer, and some time at the end when the dryer is running but not the washer. By having the shortest washing times at the start, and the shortest drying times at the end, you maximize the amount of overlap-when the washer and dryer are running simultaneously. Thus you can keep the total amount of time spent doing laundry to the absolute minimum. Johnson's analysis had yielded scheduling's first optimal algorithm: start with the lightest wash, end with the smallest hamper.

> Beyond its immediate applications, Johnson's paper revealed two deeper points: first, that scheduling could be expressed algorithmically, and second, that optimal scheduling solutions existed. This kicked off what has become a sprawling literature, exploring strategies for a vast menagerie of hypothetical factories with every conceivable number and kind of machines.

But a subset of this literature is on scheduling tasks for single machines, and "...the scheduling problem that matters the most involves just one machine: ourselves." - Well, the scheduling problem that matters the most for personal time management.

Think about this: if all our tasks are of equal time and importance, it doesn't matter what order we do them in. If we do all of our tasks, it will end up taking the same time.

"Thus we encounter the first lesson in single-machine scheduling literally before we even begin: _make your goals explicit_."

Which scheduling approach is optimal or best depends entirely on the metric we are trying optimize.

### Metrics and Strategies  
- Earliest Due Date:
  - Trying to minimize maximum lateness
  - **Optimal** strategy: work on the tasks in order of the earliest due date
  - "But some of its implications are surprising. For example, how long each task will take to complete is entirely irrelevant: it doesn't change the plan, so in fact you don't even need to know. All that matters is when the tasks are due."
- Moore's Algorithm
  - Consider groceries with an expiration date (minimizing maximum lateness - rottenness)
  - Earliest due date will minimize the rottenness of the _single most rotten thing_ you'll have to eat
  - If you want to minimize the _number_ of foods that spoil, use Moore's algorithm
  - Schedule out the produce in order of spoilage date, earliest first, one item at a time
  - As soon as it looks like we can't eat the next item, look back over the meals you've planned and _throw out_ the biggest item (the one it would take the most days to consume)
  - Repeat the above step until no meals in our plan will spoil, then we have our plan
  - Moore's Algorithm minimizes the **number of items you'll need to throw away**
  - For projects "...where you can't simply discard a project, but in which the _number_ - rather than the severity - of late projects is still your biggest concern, Moore's Algorithm is just as indifferent about how those late tasks are handled. Anything booted from the main portion of your schedule can get done at the very end, in any order; it doesn't matter, as they're all already late."
- Shortest Processing Time
  - _Do the difficult things while they are easy and do the great things while they are small._ - Lao Tzu
  - Say you have a 1 day project and a 4 day project each due to 2 different clients
    - If you do the 4 day project first, finish on Thursday, then do the 1 day project on Friday, client 1 waits 5 days and client 2 waits 4 days for a total of 9 days waiting for both clients
    - If you do the 1 day project on Monday and turn in the 4 day project on Friday, client 1 waits 1 day and client 2 waits 5 days for a total of 6 days waiting
    - Optimizing for this metric, **minimizing the sum of completion times**, leads to a very simple **optimal** algorithm called Shortest Processing Time
  - **Always do the quickest task you can**
  - It's like focusing above all on minimizing your to do list
- Shortest Processing Density
  - Not all tasks are equal, some are more important
  - Simple modification to Shortest Processing Time: divide the _weight_ of each task by how long it will take to finish, then work in order from the highest resulting importance to the lowest
  - Weight or density: how important a task is divided by the time it takes to complete the task
    - One easy example of density: prioritize based on which task brings in the most money per unit of time
  - This strategy shows up in animal foraging: "Animals, seeking to maximize the rate at which they accumulate energy from food, should pursue foods in order of the ratio of their caloric energy to the time required to get and eat them-and indeed appear to do so."
  - Minimizing the amount of debt you have: ignore the total debt and focus on paying off those loans with the highest interest rates as quickly as possible
    - Shortest Processing Time however will minimize the number of debts you

---

### An explanation of procrastination
Procrastination is actually an optimal strategy for the _wrong_ metric. "Putting off work on a major project by attending instead to various trivial matters can likewise be seen as "the hastening of subgoal completion"-which is another way of saying that procrastinators are acting (optimally!) to reduce as quickly as possible the number of outstanding tasks on their minds. It's not that they have a bad strategy for getting things done; they have a great strategy for the wrong metric."
