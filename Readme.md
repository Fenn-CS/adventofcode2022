# Advent of Code 2022

This repo tracks my advent of code solutions for 2022, each days work in contained it's own folder. 
See: [Advent of code](https://adventofcode.com/2022/about) 

*NB: Not flowing with the days, I try or tried to do as much as I can (Whenever you are looking at this, it may be in the year when 2122 I would be gone but know that I TRIED)*

## How it went?

I have been adding my experience for each day in my commits, decided it would be more fun to also put those here:

### Day 7

```
commit c25c2c88582fde616e8942dac35bc23dd753317a (HEAD -> master)
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Sun Dec 11 02:21:25 2022 +0100

    Day 7 solution part 2

    Again, my fancy file system was of much use! I just
    needed to added a method which I can pass to traverse!

    Sweet! (Performance checks required)

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

commit 437ea8dea95dea59652d477a2fa53ffe13850455 (origin/master)
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Sun Dec 11 01:59:46 2022 +0100

    Day 7 solution part 1

    As imagined, my fancy filesytem added in
    fa66d79993cf7cb71c272a9e3f900de20823bff5 made this pretty much
    painless.

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

commit fa66d79993cf7cb71c272a9e3f900de20823bff5
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Sat Dec 10 23:14:45 2022 +0100

    Day 7, my fancy file system

    Sounding like I did something big, "Well, I
    designed this file system because I believe it's
    going to be of excessive use in the actual problem
    of finding large files. I rest my case"

    Actual commit message:

    - This is just a generalized tree implementation
    with a traverse function that can basically do anything
    it may be useful in solving day 7.

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

```

### Day 2 (Finally)

It's 9 and I have not done day 7. Phew!

```
commit d1229d985f477434aeef053489a815cb7b01f2b7 (HEAD -> master)
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Fri Dec 9 18:02:49 2022 +0100

    Day 2 solution part 2

    I tried to use my old solution, so in this case, I need to
    take an input and map it to the corresponding that would yield
    the desired result (win, draw, lose).

    I got one rule wrong, and then used trial and error to get it
    right. Looks like I don't like thinking about the R-P-S game!

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

commit eab7dc354253b69f6ecedb753acac8190ebf4f93 (origin/master)
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Fri Dec 9 16:54:03 2022 +0100

    Day 2 solution part 1

    Rock-papper-scissors is a pretty straigfoward game.
    The inputs where easy to capture.

    BUT I GOT THE RULES WRONG. (Just like when you are being taught
    a game, you stop the teacher and claim you have gotten it then
    go ahead to get well beaten, yeah).

    See why I got the rules wrong in commit : 921167b34edd8118c3a8131d4517669d742cbd74

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

commit 921167b34edd8118c3a8131d4517669d742cbd74
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Fri Dec 9 16:15:37 2022 +0100

    Day 2 Debug point

    At this point, I was wondering what was wrong everything seemed
    fined based on my defination of the problem.

    I decided to debug my outputs againts : https://dev.to/doctorlai/avent-of-code-day-02-rock-paper-scissors-27d4

    After comparing the outputs for the 2nd and 3rd lines it turns out I
    forgot and important part of the problem.

    Even though rock awards just a point (1) it still beats scissors which offers 3 points.

    So translating each input and using it's weight would always result in a win for playing
    scissors over rock!

    APOLOGIES: The first time I read about ROCK PAPER SCISSORS was on this issue, so,
    I really missed the rules for the game.

    Well, well, HOPEFULLY that was it.

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

```

### Day 6

```
commit 732bf8b3c0b756329a283a1cc8dac3f5d8d3ca5f (HEAD -> master)
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Fri Dec 9 12:58:44 2022 +0100

    Day 6 solution part 2

    Simply added a generalized fucntion which does same thing
    as in part 1 using a different parameter (14 in this case)

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

commit 0a4e2715347e5b62e4ead86fce5d9053217794a1
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Fri Dec 9 12:41:41 2022 +0100

    Day 6 solution part 1

    This is pretty straight forward, my alogorithm needs to be
    stress-tested to see how it perfoms when the stream is too large
    and the packet market is burried right within.

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

```


### Day 5

```
commit d08fb976d0e7ac0f8cc69616520406dff97be30b (HEAD -> master)
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Fri Dec 9 01:03:53 2022 +0100

    Day 5 solution part 2

    Well not so hard given part 1 was already done.

    However, this is probably not efficient and VERY WET!

    If my colleage [Liam](https://github.com/liam-lloyd) were
    to look at this code he would have lot of ideas on how I could
    make things DRY like he does with my code at work :).

    Well, sorry Liam and DRY-code warriors, day 5 was long overdue.

    See you day 6.

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>


commit 46c22b0b6927cb40a7071285de24d2ecde17cf8b (HEAD -> master)
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Fri Dec 9 00:36:09 2022 +0100

    Day 5 solution part 1

    Actual solution for day5 part 1.

    This is the first problem where I needed to run the test set
    on my code to get the actual input right!

    Maybe the lesson for day 5 is, ALWAYS RUN THE TEST SET.

    - It helps me realize whether I captured the inputs in a way that
    works for that example and in future for the inputs
    - Let's you know if the algorithm works quickly

    CONFESSION : I don't write down any algorithm, I just start coding.

    Guess, I am learning the hard way, I am not that smart. Time to start
    writing my psedu code down before attempting code???

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

commit 7b2a8445beaf4c3bec3f27a98190fe0e7df06e40
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Fri Dec 9 00:33:02 2022 +0100

    CRAY! : Input formatting day 5! 🙄

    For day 5, I really wonder if the aim was for the actual
    issue was for the elves to receive any help.

    I mean, they really don't deserve it! Their input was poor
    and terrible.

    Shamefully, I spent about four hours over 2 days trying to
    get the input in a sane way for me to use.

    It's still terrible but it works!

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
```

### Day 4

```
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Wed Dec 7 22:19:17 2022 +0100

    Day 4 solution part 2

    Some more thought could be put into this, I believe
    generating ranges makes the algorithm significantly slower.

    However, given how much time I spent on part 1 of this problem
    in 211b0b7626e27c810cf3f7696fb57fc2b9f7c2ab I just want to get past day 4.

    Mind you, it's day 7.

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Wed Dec 7 21:52:56 2022 +0100

    Day 4 solution part 1

    This took me longer than expected, I think a good 3
    hours spread across 2 days.

    WHY? I was looking fully contained section assigments
    across all group assignments.

    The problem grouped the assignments in parts and the check
    was only supposed be for each pair and not across pairs (my bad!).

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
```

### Day 3

```
commit b50cf16f8221196643372b1110fee2bf77c0b31f
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Tue Dec 6 00:34:51 2022 +0100

    Day 3 solution part 2

    I am suprised part 2 was little disconnected from part 1.
    I mean, I was not able to simply continue with the work already
    done in part 1, weird.

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>

commit 5ceeb985f56ef0d9e36da3c075a6d4750fc2cd3c
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Mon Dec 5 23:17:45 2022 +0100

    Day 3 solution part 1

    Felt more straight-forward than day2
    
	Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
```

### Day 1

```
commit a17ca5c575220a23b7632630faaa4efbee4cd59c
Author: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
Date:   Mon Dec 5 23:10:21 2022 +0100

    Day 1 solution

    Quite straighforward!

    Signed-off-by: Fon E. Noel NFEBE <fenn25.fn@gmail.com>
```
