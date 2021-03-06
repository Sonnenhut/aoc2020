### [Advent of code 2020](https://adventofcode.com/2020) in python

things I learned:

 - You can get going in python really fast.
 - No boilerplate of imports on stdlib needed i.e. [open](https://docs.python.org/3/library/functions.html#open), [map](https://docs.python.org/3/library/functions.html#map)
 - Most of the time code readability > performance (it can be X times more performant, but who would still understand the code?)
 - Out of the box memoization with [@functools.cache](https://docs.python.org/3/library/functools.html#functools.cache) (when arguments are hashable) 
 - itertools has some nice functions like [combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations)
 - [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) instead of `list(map(lambda: foo * 2,bar))` you can do `[foo * 2 for foo in bar]`
 - Reversing a string or array with `"Hello World"[::-1]`, which means: start at 0 until the end and step with an increase of -1 (this works because `"Hello World"[-1]` will look at the last index -1)
 - calling `map()` with mutliple arguments are passed down to function: `map(sum, [1,2,3], itertools.repeat(1))`
