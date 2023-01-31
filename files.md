# Python Files

## Files

The `open()` function opens and returns a file handle that can be used
to read or write a file in the usual way. The code `f = open('foo.txt',
'r')` opens the file into the variable `f`, ready for reading operations,
and use `f.close()` when finished. The `'r'` stands for the read "mode",
instead of `'r'`, use `'w'` for writing, and `'a'` for append. Python's
file objects can now support end of line conventions other than the one
followed by the platform on which Python is running. Opening a file
with the mode 'U' or 'rU' will open a file for reading in universal
newline mode.

For a full list of modes see this [StackOverFlow question](https://stackoverflow.com/a/23566951/526860)

The standard for-loop works for text files, iterating through the lines of the
file (this works only for text files, not binary files). The for-loop technique
is a simple and efficient way to look at all the lines in a text file:

```python
# Print the contents of a file
f = open('foo.txt')
for line in f:
    print(line)

f.close()
```

Note the line `f.close()` which tells python that we are finished with the file
and it can let it go. This is important as operating systems have a limit the 
number of files that they can have open at the same time, it is especially
important if you are using Windows as it will not let anyone else interact with
that file while you have it open. This can lead to nasty bugs in production code
that are hard to find in your tests, which typically don't open a lot of files.
To help with these problems, python provides the `with` keyword this makes sure
that the file is closed when you have read all of it, even if an exception
occurs.

```python
with open('foo.txt') as f:
    for line in f:
        print(line)

f.closed # will be True
```


Reading one line at a time has the nice quality that not all the file
needs to fit in memory at one time -- handy if you want to look at every
line in a 10 gigabyte file without using 10 gigabytes of memory. The
`f.readlines()` method reads the whole file into memory and returns its
contents as a `list` of its lines. The `f.read()` method reads the whole
file into a single string, which can be a handy way to deal with the
text all at once, such as with regular expressions we'll see later.

For writing, `f.write(string)` method is the easiest way to write data to
an open output file. Again using a context block is best practice as it will make sure the file is closed when 
you are finished with it.

```python
# Add some lines to a file
with open('foo.txt', 'a') as f:
  f.write('Yet another line\n')
  f.write('And another!\n')
```

### Files Unicode

As with strings reading and writing unicode used to be hard to handle in 
python2, in python3 UTF-8 is the default encoding so most of the time you will
not need to specify an encoding. Sometimes you may need to use something like `open(fname,
encoding="latin-1")` to specify a different encoding (especially if you get
files from Windows users). 

```python

with open('foo.html', 'w') as f:
  f.write("\U0001F383" * 10)

with open('foo.html') as f:
  for line in f:
    print(line,end=' ')

```

## Exercise: wordcount.py

Return to the `wordcount.py` file and modify it to read in a file of text and extract the word list from it. 
There are two files to try `small.txt` and a longer one `alice.txt`. Work with the small one until you are 
confident in your program.


**Note**: if you are using the QGIS console for development then you will need to use the full path to the 
file name in the `main` statement at the end of the file:

~~~py
main(r'C:\Users\PhotonUser\My Files\Home Folder\python\basic\small.txt', True)
~~~

----

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 3.0
License](http://creativecommons.org/licenses/by/3.0/), and code samples
are licensed under the [Apache 2.0
License](http://www.apache.org/licenses/LICENSE-2.0). For details, see
our [Site Policies](https://developers.google.com/terms/site-policies).
