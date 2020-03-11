Python Types
==============

## Strings

Python has a built-in string class named "str" with many handy features.
String literals can be enclosed by either double or single quotes, although
single quotes are more commonly used.

```python
'Hello'
"Hello"
```

Backslash escapes work the usual way within both single and double quoted
literals -- e.g. `\n` `\'` `\"`.

```python
print('first\nsecond')
print('I didn\'t do it')
```

A double quoted string literal can contain single quotes without any fuss (e.g.
`"I didn't do it"`) and likewise single quoted string can contain double quotes.

A string literal can span multiple lines, but there must be a backslash `\` at
the end of each line to escape the newline.  String literals inside triple
quotes, `"""` or `'''`, can span multiple lines of text.

Python strings are "immutable" which means they cannot be changed after they
are created. Since strings can't be changed, we construct **new** strings as we
go to represent computed values. So for example the expression `'hello' +
'there'` takes in the 2 strings 'hello' and 'there' and builds a new string
`'hellothere'`.

Characters in a string can be accessed using the standard `[ ]` syntax,
and like Java and C++, Python uses zero-based indexing, so if `str` is
`'hello'` `str[1]` is `'e'`.

If the index is out of bounds for the string, Python raises an error. The
Python style (unlike Perl) is to halt if it can't tell what to do, rather than
just make up a default value.

The handy "slice" syntax (below) also works to extract any substring from a
string. The `len(string)` function returns the length of a string. The `[ ]`
syntax and the `len()` function actually work on any sequence type -- strings,
lists, etc.. Python tries to make its operations work consistently across
different types.

**Python newbie gotcha:** don't use `len` as a variable name to avoid blocking
out the `len()` function.

The `+` operator can concatenate two strings. Notice in the code below that
variables are not pre-declared -- just assign to them and go.

```python
s = 'hi'
print(s[1])          ## i
print(len(s))        ## 2
print(s + ' there')  ## hi there
```

Unlike Java, the `+` does not automatically convert numbers or other
types to string form. The `str()` function converts values to a string
form so they can be combined with other strings (and is why `str` is not a good
variable name).

```python
pi = 3.14
text = 'The value of pi is ' + pi        ## No, does not work
text = 'The value of pi is '  + str(pi)  ## Yes
```

## Numbers

For numbers, the standard operators, `+`, `-`, `/`, `*` work in the usual way.
There is no `++` operator (don't worry if you don't know what that is), 
but `+=`, `-=`, etc. work (they add or subtract the right hand side
to the left hand). If you want integer division, it is most correct to
use 2 slashes -- e.g. `6 // 5` is `1` (in Python 2, a single
`/` does int division with ints anyway, but moving forward `//` is
the preferred way to indicate that you want int division.) You use `%`
to get the remainder (modulo) of an integer division, so `6%5` is `1`
for the remanider of `6//5`.

# Printing

The "print" operator prints out one or more python items followed by a
newline (leave a trailing comma at the end of the items to inhibit the
newline).

A "raw" string literal is prefixed by an 'r' and passes all
the chars through without special treatment of backslashes, so r'x\\nx'
evaluates to the length-4 string 'x\\nx'. **Except** for `\"` (or `\'`) which are
printed as `"` and `'`, so be careful with windows paths as `r"c:\temp\"` is not valid 
as the `\` hides the final `"`, see this [stackoverflow question](https://stackoverflow.com/questions/647769/why-cant-pythons-raw-string-literals-end-with-a-single-backslash) for more explanation. 

```python
raw = r'this\t\n and that'
print(raw)     ## this\t\n and that

text = 'this\t\n and that'
print(text)

multi = """It was the best of times.
It was the worst of times."""
```

## String Methods

Here are some of the most common string methods. A method is like a
function, but it runs "on" an object. If the variable `s` is a string,
then the code `s.lower()` runs the `lower()` method on that string object
and returns the result (this idea of a method running on an object is
one of the basic ideas that make up Object Oriented Programming, OOP).
Here are some of the most common string methods:

-   `s.lower()`, `s.upper()` -- returns the lowercase or uppercase version
    of the string
-   `s.strip()` -- returns a string with whitespace removed from the start
    and end
-   `s.isalpha()`/`s.isdigit()`/`s.isspace()`... -- tests if all the string
    chars are in the various character classes
-   `s.startswith('other')`, `s.endswith('other')` -- tests if the string
    starts or ends with the given other string
-   `s.find('other')` -- searches for the given other string (not a
    regular expression) within `s`, and returns the first index where it
    begins or `-1` if not found
-   `s.replace('old', 'new')` -- returns a string where all occurrences of
    `'old'` have been replaced by `'new'`
-   `s.split('delim')` -- returns a list of substrings separated by the
    given delimiter. The delimiter is not a regular expression, it's
    just text. `'aaa,bbb,ccc'.split(',')` -&gt; `['aaa', 'bbb', 'ccc']`.
    As a convenient special case `s.split()` (with no arguments) splits on
    all whitespace chars.
-   `s.join(list)` -- opposite of `split()`, joins the elements in the given
    list together using the string as the delimiter. e.g.
    `'---'.join(['aaa', 'bbb', 'ccc'])` -&gt; `'aaa---bbb---ccc'`

A google search for "python str" should lead you to the official
[python.org string
methods](http://docs.python.org/library/stdtypes.html#string-methods)
which lists all the str methods.

Python does not have a separate character type. Instead an expression
like `s[8]` returns a string-length-1 containing the character. With
that string-length-1, the operators `==`, `<=`, ... all work as you would
expect, so mostly you don't need to know that Python does not have a
separate `char` type.

## String Slices

The "slice" syntax is a handy way to refer to sub-parts of sequences --
typically strings and lists. The slice `s[start:end]` is the elements
beginning at start and extending up to but not including end. Suppose we
have `s = "Hello"`

![the string 'hello' with letter indexes 0 1 2 3
4](images/hello.png)

-   `s[1:4]` is `'ell'` -- chars starting at index 1 and extending up to
    but not including index 4
-   `s[1:]` is `'ello'` -- omitting either index defaults to the start or
    end of the string
-   `s[:]` is `'Hello'` -- omitting both always gives us a copy of the
    whole thing (this is the pythonic way to copy a sequence like a
    string or list)
-   `s[1:100]` is `'ello'` -- an index that is too big is truncated down
    to the string length

The standard zero-based index numbers give easy access to chars near the
start of the string. As an alternative, Python uses negative numbers to
give easy access to the chars at the end of the string: s[-1] is the
last char `'o'`, `s[-2]` is `'l'` the next-to-last char, and so on. Negative
index numbers count back from the end of the string:

-   `s[-1]` is `'o'` -- last char (1st from the end)
-   `s[-4]` is `'e'` -- 4th from the end
-   `s[:-3]` is `'He'` -- going up to but not including the last 3 chars.
-   `s[-3:]` is `'llo'` -- starting with the 3rd char from the end and
    extending to the end of the string.

It is a neat truism of slices that for any index n,
`s[:n] + s[n:] == s`. This works even for n negative or out of bounds.
Or put another way `s[:n]` and `s[n:]` always partition the string into
two string parts, conserving all the characters. As we'll see in the
list section later, slices work with lists too.

### String Formatting

Python allows you to use a template style string rather than having to add a
number of strings together. This is more efficient if your program is going to
do a lot of string manipulation (as otherwise the strings keep having to be
copied). You tell python that it should **f**ormat the string by prepending `f`
to it.

```console
> pigs=3
> huff="huff"
> puff="puff"
> rest="blow your house down"
> text = f"{pigs} little pigs come out or I'll {huff} and {puff} and {rest}"
> text
"3 little pigs come out or I'll huff and puff and blow your house down"
> pigs=2
> text
"3 little pigs come out or I'll huff and puff and blow your house down"
> text = f"{pigs} little pigs come out or I'll {huff} and {puff} and {rest}"
> text
"2 little pigs come out or I'll huff and puff and blow your house down"
>
```
As you can see the variables' values are substituted into the string when it is
used, so if you change a value you need to recreate the string. You will also
see the alternative `%` operator which takes a tuple of values and inserts them
into the string where items are indicated by `%type` sections.

```python
> s = "%d pigs little pigs come out or I'll %s and %s and %s" % (pigs,huff,puff,rest)
> s
"3 pigs little pigs come out or I'll huff and puff and blow your house down"

```

The variable placeholders in a string template can also be formatted for display; for example you might wish to format a `float` value to show 2 decimal places:

```python
> import math
> f"pi to 3 decimal places is {math.pi:.3f}"
'pi to 3 decimal places is 3.142'
```

See the [Python string documentation for formatting examples](https://docs.python.org/3/library/string.html#format-examples).

Python also provides a [full string
formatter](https://docs.python.org/3/library/string.html#string-formatting)
if you need to carry out type conversions of your variables but you are
unlikely to need this in your day to day work.

### Unicode 😀

In python2 you had to handle unicode characters specially, fortunately in
python3 unicode is supported by default. As English speakers we don't worry too
much about accents and other special characters, but they do crop up in place
and people's names. You can insert unicode characters using your keyboard (if
you know how to type it) or using the octal (\u018e) or hex (\xf1) code which
are easy to look up on the internet. Llanarmon-yn-Iâl is a village in 
Denbighshire, Wales if you were wondering.

See the [python documentation](https://docs.python.org/3/howto/unicode.html) for
a longer discussion of unicode's development and how python uses it.
 
```console
> place="Llanarmon-yn-Iâl"
> print(place)
Llanarmon-yn-Iâl
> place="Llanarmon-yn-I\u00E2l"
> print(place)
Llanarmon-yn-Iâl
>
> string = 'A unicode \u018e string \xf1'
> print(string)
A unicode Ǝ string ñ

```


# If Statement

Python does not use { } to enclose blocks of code for if/loops/function
etc.. Instead, Python uses the colon (:) and indentation/whitespace
to group statements. The boolean test for an if does not need to be
in parenthesis, and it can have `elif` and `else` clauses (mnemonic:
the word `elif` is the same length as the word `else`).

Any value can be used as an if-test. The "zero" values all count as
`false`: `None`, `0`, `''`, empty list `[]`, empty dictionary `{}`,
anything else is true. There is also a Boolean type with two values:
`True` and `False` (converted to an integer, these are `1` and `0`).

Python has the usual comparison operations: `==`,
`!=`, `<`, `<=`, `>`, `>=`. That is equals, not equals, less than, less than or
equal to, greater than, and greater than or equal to.

The boolean operators are the spelled out
words `and`, `or`, `not` (Python does not use the C-style `&&` `||`
`!`). Here's what the code might look like for a policeman pulling over a
speeder -- notice how each block of then/else statements starts with a `:`
and the statements are grouped by their indentation:

```python
if speed >= 80:
    print('License and registration please')
    if mood == 'terrible' or speed >= 100:
        print('You have the right to remain silent.')
    elif mood == 'bad' or speed >= 90:
        print("I'm going to have to write you a ticket.")
    else:
        print("Let's try to keep it under 80 ok?")
```

I find that omitting the ":" is my most common syntax mistake when
typing in the above sort of code, probably since that's an additional
thing to type vs. my C++/Java habits. Also, don't put the boolean test
in brackets -- that's a C/Java habit. If the code is short, you can put
the code on the same line after ":", like this (this applies to
functions, loops, etc. also), although some people feel it's more
readable to space things out on separate lines.

```python
if speed >= 80: print('You are so busted')
else: print('Have a nice day')
```

Exercise: string1.py
--------------------

To practice the material in this section, try the **string1.py**
exercise in the [Basic
Exercises](basic).

----

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 3.0
License](http://creativecommons.org/licenses/by/3.0/), and code samples
are licensed under the [Apache 2.0
License](http://www.apache.org/licenses/LICENSE-2.0). 
