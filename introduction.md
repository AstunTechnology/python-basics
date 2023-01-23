# Python Introduction

## Prelude

This material is based on [Google's Python
Class](https://developers.google.com/edu/python/) licensed under [Creative
Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/),
and code samples are licensed under the [Apache 2.0
License](http://www.apache.org/licenses/LICENSE-2.0).

## Language Introduction

Python is a dynamic, interpreted (bytecode-compiled) language. There are
no type declarations of variables, parameters, functions, or methods in
source code. This makes the code short and flexible, and you lose the
compile-time type checking of the source code. Python tracks the types
of all values at runtime and flags code that does not make sense as it
runs.

An excellent way to see how Python code works is to run the Python
interpreter and type code right into it. If you ever have a question
like, "What happens if I add an `int` to a `list`?" Just typing it into
the Python interpreter is a fast and likely the best way to see what
happens. (See below to see what really happens!)

```python
$ python        ## Run the Python interpreter
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 6
>>> a
6
>>> a + 2
8
>>> a = 'hi'
>>> a
'hi'
>>> len(a)
2
>>> a + len(a)          ## try something that doesn't work
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> a + str(len(a))
'hi2'
>>> foo                 ## try something else that doesn't work
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'foo' is not defined
```

**Note:** you may need to type `python3` to make sure you are working with the
latest version of python. If you see Python 2.7.9 instead of Python 3.6.7 or later try
that or ask your instructor.

As you can see above, it's easy to experiment with variables and
operators. Also, the interpreter throws, or "raises" in Python parlance,
a runtime error if the code tries to read a variable that has not been
assigned a value. Like C++ and Java, Python is case sensitive so "`a`" and
"`A`" are different variables. The end of a line marks the end of a
statement, so unlike C++ and Java, Python does not require a semicolon
at the end of each statement. Comments begin with a `#` and extend to
the end of the line.

## Python source code

Python source files use the ".py" extension and are called "modules".
With a Python module `hello.py`, the easiest way to run it is with the
shell command 

    python hello.py Alice
    
which calls the Python interpreter
to execute the code in `hello.py` (in the current directory), passing it the command line argument
"Alice". See the [official docs
page](http://docs.python.org/using/cmdline) on all the different options
you have when running Python from the command-line.

## Variable Names

Since Python variables don't have any type spelled out in the source
code, it's extra helpful to give meaningful names to your variables to
remind yourself of what's going on. So use "name" if it's a single name,
and "names" if it's a list of names, and "tuples" if it's a list of
tuples. Many basic Python errors result from forgetting what type of
value is in each variable, so use your variable names (all you have
really) to help keep things straight.

As far as actual naming goes, some languages prefer underscored\_parts
for variable names made up of "more than one word," but other languages
prefer camelCasing. In general, Python
[prefers](http://python.org/dev/peps/pep-0008/#function-names) the
underscore method but guides developers to defer to camelCasing if
integrating into existing Python code that already uses that style.
Readability counts. Read more in [the section on naming conventions in
PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions).

As you can guess, keywords like 'print' and 'while' cannot be used as
variable names — you'll get a syntax error if you do. However, be
careful not to use built-ins as variable names. For example, while 'str'
and 'list' may seem like good names, you'd be overriding those system
variables. Built-ins are not keywords and thus, are susceptible to
inadvertent use by new Python developers.


Now we can look at the different types of python variable we can create in the [next section](strings)

----

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 3.0
License](http://creativecommons.org/licenses/by/3.0/), and code samples
are licensed under the [Apache 2.0
License](http://www.apache.org/licenses/LICENSE-2.0). For details, see
our [Site Policies](https://developers.google.com/terms/site-policies).
