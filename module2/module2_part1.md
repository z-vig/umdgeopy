Module 2: Using Scientific Packages from the Internet :mag:
---
### *Part 1: Functions and Classes*

## Background
The term is thrown around quite a bit among python users. You might have heard early on in your python journey something along the lines of "oh, there's a python package for that!" Unfortunately, unless you have experience either making or using a python package, the term itself is quite meaningless. In this module, we will go over exactly what a package is and how you, as a scientist, can get into using one right away for your needs, just by looking on the internet! To start this journey to becoming a pro python package user, we first need to understand the fundamental pieces of code that python packages allow you to access: 1) `functions` and 2) `classes`.

## Module Tasks
- [ ] Download the `function_demo.py`, `class_demo.py` and `sample_geochemical_data.csv` files from github
- [ ] Learn about functions and classes as concepts
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
#### Type Hints and Function Docstrings
Although these simple examples are straight forward and easy to follow, when you install a package from the internet, you are likely to encounter many different functions that each are likely to have several input parameters that give you possibly multiple outputs. Two mechanisms are designed to work in tandem to make this experience easier: 1) type hints and 2) docstrings. In the `np.polyfit()` example, these are expressed on the documentation website. Looking at the first parameter, for example, you will see:
```python
x : array-like, shape(M,)
    x-coordinates of the M sample points (x[i], y[i]).
```
The array-like part is your type-hint, telling you that this parameter must be either a strict numpy array or something that can be converted to a numpy array, like a list or `Pandas` Series. The annotations below the type-hint describe what the parameter is supposed to represent. Docstrings will also describe the function as a whole. This description is featured at the top of the page, stating with "Least squares polynomial fit...". If you are writing your own function, you can easily add type-hints on each argument of the function using ":" and docstrings using triple quotations immediately following the function signature:
```python
def myfunction(arg: float):
    """
    Adds five and ten to the argument and returns both additions.

    Parameters
    ----------
    arg: float
        Number that has not yet been added to.
    
    Returns
    -------
    added_five: float
        Argument plus five.
    added_ten: float
        Argument plus ten.
    """
    added_five = arg + 5
    added_ten = arg + 10
    return added_five, added_ten
>>> out1, out2 = myfunction(5)  # None
>>> print(out1, out2)  # 10 15
```
Often times, it is helpful to start writing your own functions by writing the docstrings, since you will always have a clear idea of the basic functionality of your function: what goes in and what goes out?

## Python Classes
If you have ever heard the term "Object-Oriented Programming" or "OOP", classes are exactly what people are talking about. At the most basic level, everything that you code in Pyhton is an object. From numpy arrays to lists to floats and even functions themselves are objects. Each object in python can be initialized using some data, processes this data in some way and then offers different ways to access this newly processed data and can even be acted upon by specialized functions that are tailored to the input data. Classes are essentially a blueprint for creating objects. All of the data processing, access and specialized functions are handled in a python `class`. Now that was all pretty abstract, so lets break down a class into its pieces.

#### Instances
Many classes that you will see in python will start something like this:
```python
class MyData:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

>>> dat1 = MyData(5, 10)
>>> dat2 = MyData(10, 15)
>>> print(dat1.data1)  # 5
>>> print(dat1.data2)  # 10
>>> print(dat2.data1)  # 10
>>> print(dat2.data2)  # 15
```
A lot of this code is idomatic in the sense that, unless you've seen these words and syntax before, it is quite impossible to figure out what they mean. The first interesting thing you see is this function-like `def __init__(self,...)` signature. "init" in the situation is shorthand for initialize and whatever is beneath this signature will be called as a function each time an object is created using this class. People often refer to signature like this, with two underscores preceding and following the name as "dunder" functions, so that this signature would be called "dunder init". To create an object from this class, simply call the class as you would if it were a function. The arguments for this function are the arguments to the `__init__` signature. "But wait!" you may be saying "there's another argument there!" And you would be correct! There is the `self` argument involved. You can think of this argument as signaling to the function "hey, whenever I do stuff, I have access to the data in the particular instance of this class". We will see this argument pop up again when discussing methods. Finally, by calling the class signature `MyData` as if it were a function, it creates an instance of the class that can be stored in a variable like `dat1` or `dat2` above. Both `dat1` and `dat2` are objects of the same class, but are different instances, so the data available to them is different, but the underlying mechanics for each of the objects is the same.

#### Attributes
In the above example, you will notice that we accessed the data in the `dat` object by using `dat.data1` or `dat.data2`. `data1` and `data2` in this situation are called attributes to the `dat` object, which is of the class `MyData`. Attributes can be thought of as a call to get a piece of data that is stored in an instance of a `class`. Not all the data that is passed to a `class` instance is available to the user, however. To set an attribute, you must use the `self.data1 = data1` idiom, for example. When you are looking at classes from a package on the internet, it is important to understand which attributes are available. As an example, we can look at the `Pandas` `DataFrame` object. Go to the [docs page](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) and look at the class signature. You can see several parameters listed that are described in the parameters section. These are the equivalent to `data1` and `data2` in our simple case. From there, find the attributes section. Several pieces of useful information about your dataframe can be gained by calling its attributes such as: 
```python
>>> import pandas as pd
>>> data = {"column1":[1, 2, 3, 4], "column2":[2, 3, 4, 5]}
>>> df = pd.DataFrame(data)
>>> df.shape  # (4, 2)
>>> df.columns  # Index(['column1', 'column2'], dtype='object')
>>> df.column1  # [1, 2, 3, 4]
```
The `shape` attribute returns the shape of the table (4 rows, 2 columns). The `columns` attribute returns the column names for the data. The `column1` attribute was created based on the column names that were passed in the dataset and accses the data in the column named "column1". All of these attributes and more can be found in the documentation.

#### Methods
Arguably, the most useful mechanic in a python class is the use of its methods. Methods can be thought of as functions that implicitly have access to the data that has already been introduced to a class instance. In a classof your own, they will appear as follows:
```python
class MyData:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
    def mymethod(self):
        self.data3 = self.data1 + self.data2
        return self.data3

>>> dat = MyData(5, 10)
>>> print(dat.data3)  # AttributeError!
>>> result = dat.mymethod()
>>> print(result)  # 15
>>> print(dat.data3)  # 15
```
The first thing you might notice is the `self` argument appear again. Once again, this argument essentially tells the method that it inherently has access to the class instance data. Although the `data1` and `data2` variables are not explicitly passed to the method via its arguments, the function that makes up the method still has access to these values by caling `self.data1` and `self.data2`. Methods can also set new attributes that are inaccessible until the method is called, using the same syntax that was used in the initialization function to set attributes. In the above example, the `data3` attribute was set. At the same time, methods can also work like functions, so that a returned value can be set to a variable and used in the code from there. Additional arguments can also be passed via methods:
```python
same...
def mymethod(self, arg1):
    self.data3 = self.data1 + self.data2 + arg1
    return self.data1 + self.data2
>>> dat.mymethod()  # ArgumentError!
>>> result = dat.mymethod(10)
>>> print(dat.data3)  # 25
>>> print(result)  # 15
```
In this case, an additional argument `arg1` is added into the method so that the `data3` attribute now incorporates this extra argument. 

Moving on to our `Pandas` `DataFrame` example, scroll down to the Methods section. Here you will find many useful capabilities that the `DataFrame` class can provide. Some methods that I find particularly useful are the `.sort_values(by)` method, which lets you specify the name/index of a row or column and sorts the entire dataframe by that row or column, and the `.mean()`, which takes the mean values of the dataframe along the rows or the columns or all together, depending on the keyword arguments that are passed!  

## Final Thoughts
You now, hopefully, have some solid background knowledge to go an start understanding the documentation that you find online for scientific python packages. Although the docs that we looked at in part1 of this module above were all perfectly formatted and clear, this, alas, is nary the case for all packages you can find online. Sometimes, it is easier to go in and find the source code for a package, use your knowledge of classes and functions and look for the functions and classes that are explicitly defined. Even this, however, is not always a fool-proof method because many developers try to hide their source code under API calls to other programming languages (such as numpy to C!). So, although this gives a good background to get started searching the internet for python packages that fit your needs, it also gives you the basis to start designing your own scientific packages. Designing your own functions and classes to be useful, flexible and resuable will be the topic of a future module. To finish up this module and apply the background you learned above, go look at the `function_demo.py` and `class_demo.py` files that can be downloaded (or cloned, if you know how!) from this repository. Best of luck!
