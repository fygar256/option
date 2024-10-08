---
title: Simple function to get options [python]
tags: Python CLI
author: fygar256
slide: false
---

I made a simple function to get options.

Because the argparse module of python is complicated.

Name: option
Arguments: (argv, optionname)
Returns: (argv, parameter)

Call it as `(argv, parameter) = option(argv, '-o')`

argv is sys.argv, and parameter returns the argument immediately after it is specified with '-o'.

space is required between `-o` and argument.

When the same option is specified, the first one is valid.

When there are no arguments, it returns a null string to parameter, so if you want to specify multiple identical options, call it repeatedly in a loop.

You can use mine.

Execution example

```
$ python test.py test1 -o test2 test3
(['test.py', 'test1', 'test3'], 'test2')
```

Execution example when different options are specified

```
$ python test.py test1 -a test2 test3
(['test.py', 'test1', '-a', 'test2', 'test3'], '')
```
