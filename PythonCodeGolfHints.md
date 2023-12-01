# Hints for code golfing in Python

The following document describes a few techniques I used to make my Python code as compact as possible. Some of the simple rules (especially those which are easy to accidentally overlook when writing code by hand) can even be automatically checked with the [golf checker script](golfchecker.py).



## Short identifiers

The most obvious thing to do is using short names for functions, variables and (if used) class methods and fields. Exploit the fact that Python is case-sensitive; `G` is not the same as `g`. Furthermore, `_` is a valid identifier, too. This gives a total of 53 different single-letter identifers, enough for almost any program.



## Temporary variables

The only thing that's better than a short variable name is no variable at all. If the result of an expression is only used once, don't assign it to a variable first; instead, put that expression right where it's used, unless it's too deep in a loop and the extra runtime for re-computing it every time is prohibitive.

On the other hand, if an expression is long enough, it should get its own variable, even if it isn't runtime-critical. This doesn't work always, though: Introducing an additional variable may break some other transforms that rely on everything being representable as a single statement, so it may in some cases still be beneficial to keep the repetition in if it's short enough.



## Embrace functional programming

One of the things that make Python such a useful language is the combination of imperative, object-oriented and functional approaches. This can also be used to great effect when golfing; generator expressions, list comprehensions, `map`/`filter`/`reduce`, `sorted`/`enumerate`, `min`/`max`/`sum` and `any`/`all` are very useful tools!

Some experimentation is needed: Sometimes `map` is the right way to do things, sometimes an equivalent list comprehension is shorter. <br>
`filter` is rarely worthwile, because unless the filter condition is just a function call with no parameters other than the value in question, the combination `filter(lambda x:[...],D)` is longer than `[x for x in D if [...]]`. <br>
For similar reasons, `reduce` is only worthwile when there's actually a (non-trivial) reduction function or the number of items isn't known beforehand. For example, to compute the product of numbers in a list, `reduce(lambda a,b:a*b,X)` is only shorter if there's an unknown or too large number of items; for up to five items, `a,b,c,d,e=X;a*b*c*d*e` is shorter.



## Avoid unneccessary whitespace

Remove whitespace wherever possible. Indent blocks with a single space (or tab, if you must). Don't keep whitespace around braces and operators. Write

    x=[a+"foo"for a,b in X if b*c>7]

instead of

    x = [a + "foo" for a, b in X if b * c > 7]

In general, remove any whitespace except where letters or numbers follow letters. Some syntax highlighters go crazy when seeing stuff like `7and`, but for the Python tokenizer, this is just a `7` followed by `and`, no trouble. One exception is the combination `0 or`: this can *not* be joined together, because anything starting with `0o` looks like an octal integer literal to it and it'll bail out on the following `r`.

Also, use Unix-style line endings (LF) instead of DOS/Windows-style (CR LF), regardless of which platform you're on.



## Avoid unneccessary braces

Don't add braces where operator precedence doesn't require them. `a*b&c` is certainly harder to read than `(a*b)&c`, but it's also shorter.



## Merge lines

In indented blocks, try to cram as much stuff as possible into a single line. Separating multiple statements by a semicolon (`;`) is one byte, doing this with a newline followed by indentation is *at least* two.

If the body of a block (`def`, `class`, `if`, `for`, `while` etc.) doesn't contain any other blocks in it, it can be written directly on the same line:

    if x:y=5;z*=6



## Use operators instead of methods

When manipulating lists and sets, the overloaded operators are usually much shorter than the equivalent methods:

| operation                | non-golf            | golf      |
| ------------------------ | ------------------- | --------- |
| extend list by list      | `x.extend(y)`       | `x+=y`    |
| append item to list      | `x.append(i)`       | `x+=[i]`  |
| add item to set          | `x.add(i)`          | `x\|={i}` |
| set union                | `a.union(b)`        | `a\|b`    |
| set difference           | `a.difference(b)`   | `a-b`     |
| set intersection         | `a.intersection(b)` | `a&b`     |
| convert iterable to list | `list(x)`           | `[*x]`    |



## Avoid break and continue

Try to avoid using `break` and `continue` in loops and move the break condition into the loop condition instead.

Don't use `continue` if its only purpose is skipping some irrelevant steps; sometimes, the following code can just be executed without any ill side effects, or can be tricked into doing so by setting some variables.

If `continue` is really necessary, keep in mind that it's only useful if more than eight lines of code follow it in the current block. If that's not the case, reversing the condition (from `if x<5:continue` to `if x>4:[...]`) and indenting the following lines is shorter.



## Alias frequently-used functions

If your code uses e.g. `range` a lot, it may be shorter to just assign the built-in function `range` to a single-letter variable and use that:

    _=range;x=[_(n-1)+_(n+1,100)for n in _(100)]

(Note that the whitespace between `in` and `_` must remain, otherwise the parser sees a single token "`in_`".)

For functions with six or more letters, this already saves space if they occur at least twice; for four- and five-letter functions, the "break even" point is at three occurences; for three-letter functions (like `min`, `max`, `map` and `sum`) the threshold is at four occurrences.



## Short imports

When importing from modules with short names (like `re`), it's usually best to use a standard import:

    import re
    N=[map(int,re.findall('-?\d+',l)for l in open("input.txt")]

This is optimal unless the number of calls to this module's functions gets too large or the module name gets too long. The latter is typically the case for the very useful `itertools`, in which case just importing all functions into the global namespace works best:

    from itertools import*
    for p in product(A,B,C):[...]

(Note the missing whitespace after `import`; it's simply not needed!)

When multiple modules are required, global imports aren't optimal and aliasing the module to a single letter is the best approach instead:

    import re,itertools as I
    N=map(int,re.findall('\d+',open("input.txt").read()))
    for p in I.permutations(N):[...]



## Use lambdas instead of functions

Replicated code above a certain length is obviously best put into a function of its own. However, if this function can be written as a single `return` statement, it's usually better to use a `lambda` instead. For example, the following two lines define the same function:

    def F(n):return sum(x for x in n if x>10)
    F=lambda n:sum(x for x in n if x>10)



## Use set literals

The `set` type is a very useful tool in Python, but declaring an empty set is a whopping five bytes (`set()`), and declaring a set with one starting item is even more (`set([x])`). However, there's a relatively little known syntax for specifying set literals: `{1,2,3}` creates a `set([1,2,3])`.

It's not possible to declare an empty set this way though; `{}` would be an empty `dict`, not a `set`. In these cases, there's no way around `set()` unless it is safe to have a "dummy" element in the set that can't possibly do any harm. This is typically the case if the set is only used to track whether a specific value has already been processed; `{0}` (or `{-1}` if `0` is a valid value) works fine in many cases.



## Use comparisons instead of equality checks

A check for equality like `a==0` can be rewritten as a comparison `a<1` if `a` is guaranteed to be non-negative. The same is true for inequality checks: `a==5` becomes `a>4` if `5` is the highest possible value anyway.

This also works with strings: If `x` can either be `"foo"` or `"bar"`, don't write `x=="bar"`, because `x<"f"` is much shorter. Be careful though, as the comparison in the other direction is tricky: `x>"b"` would be true for `"bar"` as well, because `"bar" > "b"`!



## Reverse comparisons to save whitespace

In some cases, swapping the order of the operands in a comparison can save a byte of whitespace:

* `if x>"a"` becomes `if"a"<x`
* `5>y or` becomes `y<5or`
* `if z>(1,2)` becomes `if(1,2)<z`



## Use multiple assignments

When assigning the same value to multiple variables, chain the assignments together into a single statement:

    a=b=c=0



## Don't use `None`

`None` is nice and useful, but long. In many cases, a simple integer literal zero (`0`) does the job just as well.



## Avoid classes

Object-oriented programming may be nice and all, but it's quite verbose with the `class` keyword, indented methods and all. However, if a class is indeed the best option, exploit the fact that the `self` parameter is not a keyword, but a mere convention in Python, and use a single-letter identifier instead.



## Don't use `pass`

Sometimes a loop with an empty body is required. Instead of using `pass` as intended, just writing `0` works just as fine. This even works with empty (i.e. pure data) classes.



## Don't use `defaultdict`

There's no denying that the `defaultdict` class in the `collections` module is genuinely useful. However, it comes at a high cost, because the identifiers are awkwardly long. As long as the `defaultdict` is only used to provide immutable default values (like integers or strings), it's often shorter to just use the `.get()` method with a suitable default when reading. More than 4 or 5 of such accesses (depending on context) are required to make the import and use of `defaultdict` worthwhile.



## Use arithmetic as logic

Pythons `and`, `or` and `not` operators are quite expensive in terms of code size; not only are they quite long themselves, in most cases they require at least one additional whitespace around them. However, boolean expressions like comparion results are freely convertible into integers in Python, which makes it possible to emulate the effect of `and`/`or`/`not` with `*`/`+`/`^`:

* `f(x)and f(y)` becomes `f(x)*f(y)`
* `f(x)or f(y)` becomes `f(x)+f(y)`
* `not f(x)` becomes `f(x)^1`

Note that this is usually *not* the optimal way for simple comparisons: `(a<5)*(b>7)` is a byte *longer* than the equivalent `and` expression! However, if only one of the operands is a function call that comes with its own braces anyway, it's a net win.

One particular application of the arithmetic-as-logic principle is forcing values to zero if a specific condition is not met. This is useful especially in scenarios where values are `sum`med oder `max`ed `if` they fulfill some condition. The following two expressions are equal (if `f()` returns a boolean):

    s=sum(x for x in n if f(x))
    s=sum(x*f(x)for x in n)



## Ternary operators and and/or chains

Python's ternary operator (a.k.a. [conditional expression](https://docs.python.org/2/reference/expressions.html#conditional-expressions)) is a bit cumbersome, but it is often useful to combine statements:

    def F(x):
     if x<1:return 1
     return F(x-1)

thus becomes

    def F(x):
     return1 if x<1else F(x-1)

and, in extension,

    F=lambda x:1if x<1else F(x-1)

In some situations, `and` and `or` can be used to similar effects:

* `[...] if x else 0` is equivalent to `x and [...]`
* `x if x else [...]` is equivalent to `x or [...]`

These can also be chained together. Effectively, `[foo] if x else [bar]` is just syntactic sugar for `x and [foo] or [bar]` (but only if `[foo]` is guaranteed to be non-zero).



## Replace for-if-call loops with list comprehensions

Sometimes the following pattern occurs in code:

    for x in R:
     if C(x):
      D(x)

This can be reduced to a single statement of the form

    [D(x)for x in R if C(x)]

This generates (and then immediately discards) a useless list with the results of the `D(x)` calls, but it's at least one byte shorter (more if indented) and it reduces the whole thing to a single statement that may be put into the same line with other statements, saving even more space.



## Use complex numbers to work with 2D coordinates

The straightforward way to work with 2D coordinates is using 2-tuples:

    (x,y)  # a point
    (x+u,y+v)  # add points
    for u,v in((x-1,y),(x+1,y),(x,y-1),(x,y+1)):[...]  # get neighbors
    (y,-x)  # rotate a direction vector by 90 degrees

It's workable, but requires constant packing and unpacking of the tuples.
A better way is to (ab-?)use complex numbers. Python supports them out of the box, without any `imports`, and they can be used as a very convenient wrappers for 2D coordinates:

    x+y*1j  # a point
    a+b  # add points
    for n in(p-1,p+1,p-1j,p+1j):[...]  # get neighbors
    p*1j  # rotate a direction vector by 90 degrees

They are immutable and can thus be used as keys in dictionaries and sets. Don't worry that they are based on floating-point values; when using pure integer coordinates, they work fine for values up to +/- 2^53.



## Use the `translate` string method

When parsing inputs, it's sometimes useful to clean certain characters first. For a single character, `x.replace(',','')`  is fine, but starting from two characters `x.translate(None,",.")` is shorter.
