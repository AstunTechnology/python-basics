Python Dict and File
====================

Dict Hash Table
---------------

Python's efficient key/value hash table structure is called a `dict` (its like a
dictionary).
The contents of a dict can be written as a series of `key:value` pairs
within braces `{ }`, e.g. `dict = {key1:value1, key2:value2, ... }`. The
"empty dict" is just an empty pair of curly braces `{}`.

Looking up or setting a value in a dict uses square brackets, e.g.
`dict['foo']` looks up the value under the key 'foo'. Strings, numbers,
and tuples work as keys, and any type can be a value. Other types may or
may not work correctly as keys (strings and tuples work cleanly since
they are immutable). Looking up a value which is not in the dict throws
a `KeyError` -- use `in` to check if the key is in the dict, or use
`dict.get(key)` which returns the value or None if the key is not present
(or `get(key, not-found)` allows you to specify what value to return in
the not-found case).

```python
## Can build up a dict by starting with the empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value-for-that-key

d = {}
d['a'] = 'alpha'
d['g'] = 'gamma'
d['o'] = 'omega'

print(d)

# Access the value associated with the key 'a'
print(d['a'])

# Update the value associated with key 'a'
d['a'] = 'amy'
print(d['a'])

# Does the dict contain the key 'a'?
'a' in d

print(d['z'])                    ## Throws KeyError

if 'z' in d: print(d['z'])       ## Avoid KeyError
print(d.get('z'))                ## None (instead of KeyError)
print(d.get('z', ''))            ## Empty string (instead of None)
```

![dict with keys 'a' 'o' 'g'](images/dict.png)

A for loop on a dictionary iterates over its keys by default. The keys
will appear in an arbitrary order. The methods `dict.keys()` and
`dict.values()` return lists of the keys or values explicitly. There's
also an `items()` which returns a list of `(key, value)` tuples, which is
the most efficient way to examine all the key value data in the
dictionary. All of these lists can be passed to the `sorted()` function.

```python

d = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.
for key in d:
    print(key)

## Exactly the same as above
for key in d.keys():
    print(key)

## Get the .keys() list:
print(d.keys()) ## ['a', 'o', 'g']

## Likewise, there's a .values() list of values
print(d.values()) ## ['alpha', 'omega', 'gamma']

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(d.keys()):
    print(key, d[key])

## .items() is the d expressed as (key, value) tuples
print(d.items())  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in d.items():
    print(k, '>', v)
```

**Strategy note**: from a performance point of view, the dictionary is one
of your greatest tools, and you should use it where you can as an easy
way to organize data. For example, you might read a log file where each
line begins with an IP address, and store the data into a dict using the
IP address as the key, and the list of lines where it appears as the
value. Once you've read in the whole file, you can look up any IP
address and instantly see its list of lines. The dictionary takes in
scattered data and makes it into something coherent.

Del
---

The `del` operator does deletions. In the simplest case, it can remove
the definition of a variable, as if that variable had not been defined.
Del can also be used on list elements or slices to delete that part of
the list and to delete entries from a dictionary.

```python
num = 6
del num  # num no more!

list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print(list)     ## ['b']

d = {'a':1, 'b':2, 'c':3}
del d['b']   ## Delete 'b' entry
print(d)     ## {'a':1, 'c':3}
```

## Exercise Incremental Development

When building a Python program, don't write the whole thing in one step.
Instead identify just a first milestone, e.g. "well the first step is to
extract the list of words." Write the code to get to that milestone, and
just print your data structures at that point, and then you can do a
`sys.exit(0)` so the program does not run ahead into its not-done parts.

Once the milestone code is working, you can work on code for the next
milestone. Being able to look at the printout of your variables at one
state can help you think about how you need to transform those variables
to get to the next state. Python is very quick with this pattern,
allowing you to make a little change and run the program to see how it
works. Take advantage of that quick turnaround to build your program in
little steps.

Combining all the basic Python material -- strings, lists, dicts,
tuples -- try the summary **wordcount.py** exercise in the [Basic
Exercises](basic).

----

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 3.0
License](http://creativecommons.org/licenses/by/3.0/), and code samples
are licensed under the [Apache 2.0
License](http://www.apache.org/licenses/LICENSE-2.0). For details, see
our [Site Policies](https://developers.google.com/terms/site-policies).
