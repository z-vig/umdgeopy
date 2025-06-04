Module 2: Using Scientific Packages from the Internet :mag:
---
### *Part 1: Functions and Classes*

## Background
The term is thrown around quite a bit among python users. You might have heard early on in your python journey something along the lines of "oh, there's a python package for that!" Unfortunately, unless you have experience either making or using a python package, the term itself is quite meaningless. In this module, we will go over exactly what a package is and how you, as a scientist, can get into using one right away for your needs, just by looking on the internet! To start this journey to becoming a pro python package user, we first need to understand the fundamental pieces of code that python packages allow you to access: 1) `functions` and 2) `classes`.

## Module Tasks
- [ ] Download the `function_demo.py` and `class_demo.py` files from github
- [ ] Use both arguments and keyword arguments as inputs into a `function`
- [ ] "Wrap" a pre-written code block in a `function`
- [ ] Make a dog and celebrate its birthday
- [ ] Turn the `function` you wrote into a `class`

## Python Functions
At the simplest level, a python `function` reads in arguments, does something with those arguments and returns a new (and ideally useful) value. If you forget this most basic operation, you'll be dead in the pythonic waters. The basic syntax for a function is as follows:
```python
def myfunction(argument):
    arg_plus_five = argument + 5
    return arg_plus_five

>>> myfunction(5)  # 10
```
When using a python package from the internet, it will likely make many functions available for use in your local environment. The first thing to look for when you encounter a function you have never seen is for what the inputs and outputs are. 

#### Function Inputs
As for inputs, functions will often have some that are required and some that are optional, but have default values associated with them. These are known as "keyword arguments" For example:
```python
def myfunction(required_argument, optional_argument="blank"):
    print(optional_argument)

>>> myfunction(5)  # blank
>>> myfunction(5, optional_argument="not blank")  # not blank
```
By setting `optional_argument` equal to "blank" in the function argument list, you are telling the function that if the user does not specify the keyword, set `optional_argument` equal to "blank". An example of this use of keyword arguments can be found on the documentation for numpy's `np.loadtxt()` function [found here](https://numpy.org/doc/2.2/reference/generated/numpy.loadtxt.html). The first argument, `fname`, is the only required argument and it is followed by a slew of keyword arguments that allow you to customize how the function operates. You will also notice that order matters in two ways: 1) Arguments (`*args`) always come before keyword arguments (`**kwargs`) and 2) Keyword arguments do not have to be explicitly listed if they are in order. If you try to call something like:
```python
myfunction(optional_argument="not blank", 5)
```
you will get an error. Also, if you have multiple `kwargs`, you do not have to specify their name as long as they are in order.
```python
def myfunction(arg1, kwarg1="one", kwarg2="two"):
    print(kwarg1, kwarg2)

>>> myfunction(5, "five", "seven")  # five, seven
>>> myfunction(5, kwarg2="seven", kwarg1="five")  # five, seven
```

#### Function Outputs
To specify what is coming out of a `function`, python uses the `return` statement. Using the return statement will connect the output of this function with a variable set equal to it. For example:
```python
def myfunction(arg):
    added_five = arg + 5
    return added_five
>>> answer = myfunction(5)  # None
>>> print(answer)  # 10
```
In the numpy docs mentioned above, it tells you under the section labeled "Returns" that it returns an `ndarray`, so you can be certain that it will return a numpy array. Sometimes, however, functions can have multiple returns:
```python
def myfunction(arg):
    added_five = arg + 5
    added_ten = arg + 10
    return added_five, added_ten
>>> out1, out2 = myfunction(5)  # None
>>> print(out1, out2)  # 10 15
```
An example of a function that displays this behavior is numpy's [polynomial fitting function](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html), which, along with the fit coefficients, it can return the fit residual and a covariance matrix. If you miss the number of outputs that a function from a package on the internet has, this could cause an error where you expect to have a singular output from your function, but instead get a tuple with all the outputs included. A way to around this is either to use underscores to just a hanging comma.
```python
>>> p = np.polyfit(x, y, 2, full=True)
>>> print(p)  # (p0, residuals, cov)
>>> p, _, _ = np.polyfit(x, y, 2, full=True)
>>> print(p)  # p0
>>> p, = np.polyfit(x, y, 2, full=True)
>>> print(p)  # p0
```

## Python Classes
