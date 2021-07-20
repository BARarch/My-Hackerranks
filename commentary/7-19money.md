# Doing a New thing
My daily jounals is going to be here in the editor today
My development goal is to complete the itertools section from code signal, and to solve two problems in the algorithms section.  There is no work on the groover.py software collection.  That progect has developed critical mass and is stable.  It gives enough functionality for sucessful use at this stage of our training.

## Itertools
This has always been one of my favorite python libraries.  Very efficient iterators and tools to combine and manipulate seqeuces.  These exercises help train me into using them powerfully.  I had to look at and use methods in itertools in a different manner in this campain.

## Lists
I guess this section stresses the use of list opporations map, filter and even reduce.  Throw in a little comprehension and you have the nessarry tools to golf these solutions.  I can't wait to get to do the general challenges with these new golfing techniuques.  They will make for efficent code.
I did the very last one of these exercises.  When it passed I was surprised becuause I knew it was not the most efficent.  When I finnished I noticed the best published solution looks just like the one I did.  Holy f**k I have the best golf form!

Solution of the Day
def primesSum(a, b):
    return sum(filter(lambda x: all(x % i for i in range(2, int(x**0.5) + 1)), range(max(2, a), b+1)))

## Generators