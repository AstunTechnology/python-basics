Python Utilities
================

In this section, we look at a few of Python's many standard utility
modules to solve common problems.

File System -- os, os.path, shutil
----------------------------------

The *os* and *os.path* modules include many functions to interact
with the file system. The *shutil* module can copy files.

-   [os module docs](https://docs.python.org/3/library/os.html)
-   `filenames = os.listdir(dir)` -- list of filenames in that directory
    path (not including . and ..). The filenames are just the names in
    the directory, not their absolute paths.
-   `os.path.join(dir, filename)` -- given a filename from the above list,
    use this to put the dir and filename together to make a path
-   `os.path.abspath(path)` -- given a path, return an absolute form, e.g.
    /home/nick/foo/bar.html
-   `os.path.dirname(path)`, `os.path.basename(path)` -- given
    dir/foo/bar.html, return the dirname "dir/foo" and basename
    "bar.html"
-   `os.path.exists(path)` -- true if it exists
-   `os.mkdir(dir_path)` -- makes one dir, `os.makedirs(dir_path)` makes
    all the needed dirs in this path
-   `shutil.copy(source_path, dest_path)` -- copy a file (dest\_path
    directory should exist)

```python
## Example pulls filenames from a dir, prints their relative and absolute paths
import os

def printdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print(filename)
        print(os.path.join(dir, filename))
        print(os.path.abspath(os.path.join(dir, filename)))
```

Exploring a module works well with the built-in python `help()` and `dir()`
functions.

```python
import os

dir(os)
help(os.listdir)
dir(os.path)
help(os.path.dirname)
```

Running External Processes -- subprocess
----------------------------------------

The `subprocess` module is a simple way to run an external command and
capture its output.

-   [subprocess module docs](https://docs.python.org/3/library/subprocess.html)
-   `subprocess.check_output(["cmd", "argument1"])` -- Run command with
    arguments and return its output as a byte string. If the return code was
    non-zero it raises a `CalledProcessError`. The `CalledProcessError` object will
    have the return code in the returncode attribute and any output in the
    output attribute.
-   If you want more control over the running of the sub-process, see
    the ["Popen" constructor](https://docs.python.org/2.7/library/subprocess.html#popen-constructor)
    which provides fine grained control when executing processes

```python
## Given a dir path, run an external 'ls -l' on it --
## shows how to call an external program
import shlex
import subprocess

def listdir(dir):
    args = shlex.split('ls -l ' + dir)
    output = subprocess.check_output(args)
    print(output)
```

Exceptions
----------

An exception represents a run-time error that halts the normal execution
at a particular line and transfers control to error handling code. This
section just introduces the most basic uses of exceptions. For example a
run-time error might be that a variable used in the program does not
have a value (`ValueError` .. you've probably seen that one a few times),
or a file open operation error because a file does not exist (`IOError`).
Learn more in [the exceptions
tutorial](https://docs.python.org/3/tutorial/errors.html) and see [the entire
exception list](https://docs.python.org/3/library/exceptions.html).

Without any error handling code (as we have done thus far), a run-time
exception just halts the program with an error message. That's a good
default behavior, and you've seen it many times. You can add a
"try/except" structure to your code to handle exceptions, like this:

```python
filename = 'does_not_exist.txt'
try:
    with open(filename) as f:
      for line in f:
        print(line,end=" ")
except IOError as e:
    print(e.strerror)
    print(e.filename)
```
Or you could write that in this way, if you prefer to keep error handling near the
function that throws them:

```python
try:
    f = open(filename)
except IOError:
    print('error')
else:
    with f:
        print(f.readlines())
```
The try: section includes the code which might throw an exception. The except:
section holds the code to run if there is an exception. If there is no
exception, the except: section is skipped (that is, that code is for error
handling only, not the "normal" case for the code). The optional `else` section
is useful for code that must be executed if the try clause does not raise an
exception.

HTTP -- requests
---------------------------

The module *requests* provides url fetching -- making a url look like a
file you can read from. While *Requests-html* makes parsing HTML as simple as
possible.

-   [requests module](http://docs.python-requests.org/en/master/#)
    [docs](http://docs.python-requests.org/en/master/api/)
-   [requests-html module](https://html.python-requests.org/)
    [docs](https://html.python-requests.org/#api-documentation)
-   `r = requests.get('https://api.github.com/events')` -- returns a response object for that
    url
-   `text = r.text` -- get the contents of the page.
-   `content = r.content` -- get the **binary** contents of the response.
-   `json = r.jason()` -- get response parsed into a JSON object.
-   `r.status_code` -- the HTTP status code (200=all good).
-   `r.headers` shows the headers of the response

```python
## Given a url, try to retrieve it.
## print its base url and its text.

import requests

def wget(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print(r.headers['Content-Type'])
        print(r.url)
        text=r.text
        print(text)
    else:
        print(f"Problem opening URL ({url}) gave {r.status_code}")


wget('http://httpbin.org/ip')
# Fails due to HTTP 418 (teapot)
wget('http://httpbin.org/status/418')
```



Exercise
--------

To practice the file system and external-commands material, see the
[Copy Special
Exercise](copy-special).
To practice the requests material, see the [Log Puzzle
Exercise](log-puzzle).

----

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 3.0
License](http://creativecommons.org/licenses/by/3.0/), and code samples
are licensed under the [Apache 2.0
License](http://www.apache.org/licenses/LICENSE-2.0). 
