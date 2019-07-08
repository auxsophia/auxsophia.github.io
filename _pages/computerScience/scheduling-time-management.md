---
layout: default
title: Philosopher Scholar - Scheduling Humans
permalink: /CS/schedulingHumans/
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
Procrastination is actually an optimal strategy for the _wrong_ metric. "Putting off work on a major project by attending instead to various trivial matters can likewise be seen as "the hastening of subgoal completion"-which is another way of saying that procrastinators are acting (optimally!) to reduce as quickly as possible the number of outstanding tasks on their minds. It's not that they have a bad strategy for getting things done; they have a great strategy for the wrong metric." This is similar to a "denial of service" attack: overwhelm the system with too many trivial tasks and the important things get lost in the chaos.

### Priority Inversion and Precedence Constraints
Example: In the summer of 1997, Jet Propulsion Laboratory (JPL) launched the $150 million Mars Pathfinder spacecraft which traveled 309 million miles of space to land on the Martian surface. Pathfinder's highest priority task (to move data into and out of its "information bus") was mysteriously being neglected in favor of low priority work.

This was a case of **priority inversion**, a low priority process took hold of some resource, say a database. When the process is interrupted by the timer which invokes the scheduler, it runs a high priority task next. However, the low priority task is still reserving the database which the high priority task needs. The scheduler instead runs a mid-level task which doesn't need access to the database. The low priority task reserving the database is now stuck behind all the other medium priority tasks such that the high priority tasks can be neglected for arbitrarily long amounts of time.

Ironically for JPL, testing this scheduling problem was considered a low priority task and was put off due to deadlines. Once JPL reproduced the error, the beamed code to the Pathfinder for a solution, **priority inheritance**. If a low priority task is blocking a high priority task, that low priority task inherits/gains the high priority since this task needs to be completed to free the resources for the high priority task.

**So a commitment to doing the most important tasks first doesn't escape scheduling pitfalls that look a lot like procrastination.**

> When a certain task can't be started until another one is finished, scheduling theorists call that a "precedence constraint."

Expert on precedence constraints Eugene "Gene" Lawler worked on various solutions. Lawler's first investigation suggested precedence constraints could be handled easily. Take the **Earliest Due Date** algorithm to minimize the maximum lateness of a set of tasks. In 1968 Lawler proved you should build the schedule back to front: look only at the tasks that no other tasks depend on, and put the one with the __latest__ due date at the __end__ of the schedule. Then simply repeat this process, again considering at each step only those tasks that no other (as-yet unscheduled) tasks depend upon as a prerequisite.

However, the **Shortest Processing Time** algorithm did not have an efficient solution-it's what the computer science field calls "intractable."

> In scheduling, it's clear by definition that every set of tasks and constraints has __some__ schedule that's the best, so scheduling problems aren't unanswerable, per se - but it may simply be the case that there's no straightforward algorithm that can find you the optimal schedule in a reasonable amount of time.

Even a subtle change can make a scheduling problem go from tractable to intractable. Examples: Moore's algorithm of minimizing rotten fruits works when all the fruits are weighted equally. When some fruits are more or less important, the problem becomes intractable. **Having to wait until a certain time to start some of your tasks makes nearly all of the scheduling problems intractable.**

### Preemption
Preemption allows for tasks to be paused while another task is completed. This allows previously intractable problems to have efficient solutions.

> In both cases, the classic strategies-Earliest Due Date and Shortest Processing Time, respectively-remain the best, with a fairly straightforward modification. When a task's starting time comes, compare that task to the one currently under way. If you're working by Earliest Due Date and the new task is due even sooner than the current one, switch gears; otherwise stay the course. Likewise, if you're working by Shortest Processing Time, and the new task can be finished faster than the current one, pause to take care of it first; otherwise, continue with what you were doing.

It turns out these strategies are still optimal (on average) for their metrics even if you don't know when tasks will begin.

> In fact, the weighted version of Shortest Processing Time is a pretty good candidate for best general-purpose scheduling strategy in the face of uncertainty. It offers a simple prescription for time management: each time a new piece of work comes in, divide its importance by the amount of time it will take to complete. If that figure is higher than for the task you're currently doing, switch to the new one; otherwise stick with the current task. This algorithm is the closest thing that scheduling theory has to a skeleton key or Swiss Army knife, the optimal strategy not just for one flavor of problem but for many. Under certain assumptions it minimizes not just the sum of weighted completion times, as we might expect, but also the sum of the weights of the late jobs and the sum of the weighted lateness of those jobs.

> Intriguingly, optimizing all these other metrics is intractable if we know the start times and durations of jobs ahead of time. So considering the impact of uncertainty in scheduling reveals something counterintuitie: there are cases where clairvoyance is a burden. Even with complete foreknowledge, finding the perfect schedule might be practically impossible. In contrast, thinking on your feet and reacting as jobs come in won't give you __as__ perfect a schedule as if you'd seen into the future-but the best you __can__ do is much easier to compute. That's some consolation.

Page 119.

### Preemption and Context Switching
> First of all, people and computer operating systems alike face a curious challenge: the machine that is doing the scheduling and the machine being scheduled are one and the same. Which makes straightening out your to-do list an item __on__ your to-do list - needing, itself, to get prioritized and scheduled.
 Second, preemption isn't free. Every time you switch tasks, you pay a price, known in computer science as a __context switch__. When a computer processor shifts its attention away from a given program, there's always a certain amount of necessary overhead. It needs to effectively bookmark its place and put aside all of its information related to that program. Then it needs to figure out which program to run next. Finally it must haul out all the relevant information for that program, find its place in the code, and get in gear.
 None of this switching back and forth is "real work"-that is, none of it actually advances the state of any of the various programs the computer is switching between. It's __metawork__. Every context switch is wasted time.

 When a computer receives too many tasks, the overhead of storing/freeing resources causes it to __thrash__. All of the time is spent on metawork, calculating priorities, switching tasks, such that no real work gets done at all.

### Interrupt Coalescing
> Part of what makes real-time scheduling so complex and interesting is that it is fundamentally a negotiation between two principles that aren't fully compatible. These two principles are called __responsiveness__ and __throughput__: how quickly you can respond to things, and how much you can get done overall.

One solution is the time slice (AKA __quantum__), the minimum processing time given to any task. If we shrink the slice of time to be divided between all programs, the quantum could become less than the needed time to context switch. Setting a limit on how small the time slice gets avoids this problem. The cost is responsiveness. Some processes simply must wait. The human equivalent is saying no to added tasks. **if the minimum slice is longer than the time it takes to context switch, then the system can never get into a state where context switching is the __only__ thing it's doing.**

> The moral is that you should try to stay on a single task as long as possible without decreasing your responsiveness below the minimum acceptable limit. Decide how responsive you need to be-and then, if you want to get things done, be no more responsive than that.

**Interrupt coalescing**: complete all the interruptions at once. Example: text messages, designate a block of time when you answer all texts. This is why regular meetings can be a benefit despite their drawbacks, they should minimize the number of interruptions.

> Perhaps the patron saint of the minimal-context-switching lifestyle is the legendary programmer Donald Knuth. "I do one thing at a time," he says. "This is what computer scientists call batch proccessing-the alternative is swapping in and out. I don't swap in and out." Knuth isn't kidding. On January 1, 2014, he embarked on "The TeX Tuneup of 2014," in which he fixed all of the bugs that had been reported in his TeX typesetting software over the previous __six years__. His report ends with the cheery sign-off "Stay tuned for The TeX Tuneup of 2021!" Likewise, Knuth has not had an email address since 1990. "Email is a wonderful thing for people whose role in life is to be on top of things. But not for me; my role is to be on the bottom of things. What I do takes long hours of studying and uninterruptible concentration." He reviews all his postal mail every three months, and all his faxes every six.
