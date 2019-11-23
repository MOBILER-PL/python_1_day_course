## Python: Code, Test, Deploy

# Enough Python to build something
 ---

# Synopsis

---
# Enough Python to build something
Source: https://docs.python.org/3/

## Python Glossary
[docs](https://docs.python.org/3/glossary.html)

Review the following terms and get to know them they are crucial to understanding Python
* argument: A value passed to a function (or method) when calling the function
`print('stuff')`, the argument is the string 'stuff'
* attribute: A value associated with an object which is referenced by name using dotted expressions.
* binary file: A file object able to read and write bytes-like objects. 
* class: A template for creating user-defined objects.
```python
class Restaurant:

    company_name = "International Investing"
    name = ""
    r_type = ""
    hours = ""
    property_value = 0.00

    def __init__(self, name, r_type,hours,property_value):
        self.name = name
        self.r_type = r_type
        self.hours = hours
        self.property_value = property_value

    def investment_report(self):
        print(f"Investor:{self.company_name}")
        print(f"Restaurant name: {self.name}")
        print(f"Restaurant type: {self.r_type}")
        print(f"Operating hours: {self.hours}")
        print(f"Total Value: ${self.property_value}")

Chochkies = Restaurant("Joff's","Casual","8:00 to 21:00","1567121")
```
calling investment_report on on instance of the Restaurant class:
```bash
>>> Chochkies.investment_report()
Investor:International Investing
Restaurant name: Joff's
Restaurant type: Casual
Operating hours: 8:00 to 21:00
Total Value: $1567121
```
* coercion: The implicit conversion of an instance of one type to another during an operation which involves two arguments of the same type.
In the following example a float is added to an int and the result is a sum of the two numbers expressed as a float
```bash
>>> 3.0 + 3 == 6.0
True
```
* context manager: An object which controls the environment seen in a with statement by defining __enter__() and __exit__() methods.
* docstring: A string literal which appears as the first expression in a class, function or module. 
`"""This class is for managing restaurants in the companies portfolio"""`

### Namespaces and Scopes
The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects
[source]()

Global namespace
Objects in this namespace are available to any other objects in your project
```python
a_global_object = "a few words"

def print_stuff():
    print(a_global_object)

print_stuff()
```
running the above code outputs the following:
`a few words`

Local namespace
Objects in the local namespace are only available to other objects in this namespace
```python
def write_string(string):
    glue_word = "stuff"
    return string + glue_word
    
print(glue_word)
```
running the above code outputs the following:
```python
Traceback (most recent call last):
  File "scripts.py", line 21, in <module>
    print(glue_word)
NameError: name 'glue_word' is not defined
```



## Standard Library
This includes all of the modules that are installed with Python
[explore it](https://docs.python.org/3/library/index.html)

### Built-in Types
[docs](https://docs.python.org/3/library/stdtypes.html), [wikipedia](https://en.wikipedia.org/wiki/Type_system)



#### True or False?
Assign the value of x to 4
`x = 4`
All objects in Python can be tested for their truth value:
`if x:
     do stuff`
     
An object will return False if it is empty, or if it is a `__bool__` method that returns False   

Source: [docs](https://docs.python.org/3/library/stdtypes.html#truth-value-testing")

#### Boolean Operations (or, and, not)
`x or y` if x is false, then y, else x
`x and y` if x is false, then x else y
`not x` if x is false, then True, else False

Source: [docs](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

## Micro-Quiz 0:
What will be printed to the Python console when running this line: `0 or 0 and 0 or 1`?

1. False
2. True
3. 1
4. 0

#### Comparison operators
`<` less than
`>` greater than
`<=` less than or equal to
`>=` greater than or equal to
`==` equal
`!=` not equal
`is` object identity
`is not` negated object identity


Source: [docs](https://docs.python.org/3/library/stdtypes.html#comparisons)

## Micro-Quiz 1:

What will be the value of `a` after running the following line in the **ipython** interpreter?

`a = 9 | a > 3 < 1000 > 0.4 < 3 < 9`

1. True
2. False
3. 9
4. 9.0
5. error

#### Numeric types
* `int()`, integers (i.e. 0,12343,-12234) [docs](https://docs.python.org/3/library/functions.html#int)
* `float()`, floating-point numbers (i.e. 1.0,-3.878) [docs](https://docs.python.org/3/library/functions.html#float)
* `complex()`, complex numbers (i.e. (x+1)<sup>2</sup>=-9) [docs](https://docs.python.org/3/library/functions.html#complex) [wikipedia](https://en.wikipedia.org/wiki/Complex_number)

Source:[docs](https://docs.python.org/3/library/stdtypes.html#numeric-types)

##### Operations
* `x+y`, Add two numbers together
* `x-y`, Subtract two numbers
* `x*y`, Multiply two numbers
* `x/y`, Divide two numbers
* `x%y`, return remainder of x/y
* `abs(x)`, absolute value of x
* `int(x)`, convert x to an interger
* `float(x)`, convert x to a float
* `complex(re, im)`, create a complex number where re=real portion and im=imaginary
* `x ** y`, x to the power of y

Review other operators: [docs](https://docs.python.org/3/library/stdtypes.html#numeric-types)

Extra time? Read this section: [Bitwise Operations on Integer Types](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)

#### Mutable Sequence Types
The types in this section can be modified in place.

Modifying an item in list `x` updates the value of the item in list `x`. No new list is created.
```python
a = [1,2,3]
a[0] = 9
print(a)
[9,2,3]
a is a
#True
```

##### Lists
Used to store collections of items

`people_named_steve = ['Steve Jobs','Steve McQueen','Steve Irwin']`

###### Common Operations

Get the value of the first item in `a = [1,2,3]`
`a[0]`

Change the value of the last item in list `a`:
`a[-1] = 9` or `a[2] = 9`

Delete the second to last item in list `a`:
`del a[-2]`

Add an item to the end of list `a`:
`a.append(9)`

Add all the individual items in list `b = [4,5,6]` to the end of list `a`:
`a.extend(b)`

Reverse the order of items in list `a`:
`a.reverse()`

Remove the last item in `a` and assign it to `x`.
`x = a.pop()`

[Read](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) about more operations you can do on lists.

## Micro-Quiz 3:
Question 1:
What will be the value of `people_named_steve` after the following operation: `people_named_steve[1][5]='k'`?

1. `['Steve Jobs','Steve McQueen','Steve Irwin']`
2. `['Steve Jobs','Stevk McQueen','Steve Irwin']`
3. `TypeError: 'str' object does not support item assignment`

Question 2:
What will be the result of the following command `list('python')`?

1. `['python']`
2. `['p', 'y', 't', 'h', 'o', 'n']`
3. `list index out of range`

#### Immutable Sequence Types

###### Tuples
Immutable sequences (cannot be changed once created) that are used to store heterogenous items, for example unique id numbers. In addition they tend to be faster for performing certain computations versus lists.

Create an empty tuple:
`a = ()`

Create a tuple with the number `3,4,5` and assign it to `a`:
`a = 3,4,5`

###### Ranges
Immutable sequences of numbers

Create a range of numbers between 0 and 100 (inclusive):
`my_numbers = range(0,101)`

Iterate through a list of 1000 digits:
```python
for i in range(0,1000):
    print(i)
```
## Micro-Quiz 4:

Question 1:
Write a script that will create a range that will include the following numbers 1,18,35,...,341 and that has a length of 21


###### str: Text Sequence Type
[docs](https://docs.python.org/3/library/stdtypes.html#string-methods)

Create a string (`str`):
`first_name = 'the house'` OR
`first_name = "the house"` OR
`first_name = """the house"""`

Make all the letters in 'kitten' uppercase:
`"kitten".upper()`

Make the title of the book correctly formatted:
`"the bornhold superiority".title()`

Check if the word 'mitten' ends with any of the strings ['ten','ton','tin']:
`"mitten".endswith(('ten','ton','tin'))`

Count how many times the string 'pot' appears in the sentence "The Potter's pot was put on the pit for potable water."
`"The Potter's pot was put on the pit for potable water.".count("pot")`
Why does it return 2 not 3?

At what index does the word 'on' appear for the first time in the string "Elvis Donson"?
`"Elvis Donson".find('don')`
Returns `-1` if no match is found

Check if the a string contains only numbers:
`"alsLKJLKJDSerty34566".isalnum()`

Create a long string by joining all items in a list:
`my_name = " ".join(["George","Granders"])`

Return a new string where the first matche of substring is replaced with newstring
`"The only way that Steve will admit to it is if Steve is here.".replace("Steve","Jeff",1)`

Replace the words {dog_name} and {cat_name} with "Rex" and "Cleo" using Python f-string:

```python
dog_name, cat_name = ("Rex", "Cleo")
f"{dog_name} is my dog, and {cat_name} is my cat" 
```

Split a string into a list of tokens using `.split()`
`the dog and pony show".split(' ')` returns `['the','dog','and','pony','show']`

## Exercise #2
The following snippet of code takes a string and magic_number and outputs an encoded verion of the string.

```python
from itertools import cycle

def encode(target="The United States of America", magic_value=326):
    """takes a string target and returns a scrambled version 
    of the target string"""
    secret_code = []
    a_list = [x for x in target]
    count = 0
    for i in cycle(a_list):
        count += 1
        if count % 326==0:
            #add to the code

            secret_code.append(i)
        if len(secret_code) == len(target):
            break
    return "".join(secret_code)
```
Based on what you know about Python so far:
1.Determine if it would be possible to add a function that would decode 
a string given the correct magic_number, and
2. Write the function if it's possible OR write a short explanation why it's impossible.

#### Set Types

##### set
a collection of unique hashable objects i.e. strings

create an empty set
`a = set()`

add an object to the set
`a.add(object)`

remove an element from the set
`a.remove('1992')`

remove a random (non specific) element from the set
`a.pop()`

collect unique letters in a string
`unique_letters = set([a for a in "this is a long sentence with many words"])`

iterate over items in a set
```python
for i in set([1,2,2,2,2,2,3,4]):
    print(i)
```
check if `99-v` exists in the set `x`:
`"99-v" in x`

get the number of items in the set `x`:
`len(x)`

confirm that the set `x` has no elements in common with the set `y`:
`x.isdisjoint(y)`

merge sets together
`a.union(b)`

return a new set that contains elements in `a` that are not in sets `b`, `c` or `d`:
```python
a = set([1,2,3,9,13])
b = set([2,3,4,11,29])
c = set([3,4,5,11,59])
d = set([5,6,7,22])
a.difference(b,c,d)
```

#### Mapping Types

##### dict
[docs](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
Maps hashable values i.e. strings to various objects
*If an item is not hashable it cannot be used as a dict key*

Create an empty dictionary
`d = dict()` OR
`d = {}`

Combine 2 lists of keys and values into new dictionary
```python
a = [1,2,3,4,5]
b = ['steve','joe','mark','susan','tom']
{a[count]:b[count] for count,i in enumerate(b)}
```
return a view of the dicts values
`x.values()`

return a list of all keys in dict `x`:
`list(x)`

return item `i` from dict `x`:
`x[i]`

set key to value
`x[i] = 99`

return the value of key 'stuff' if exists in dict `x`, otherwise return 'no results':
`x.get('stuff','no results')`

remove and return a value if key exists in `x`, otherwise return the default
`x.pop('stuff','missing')`

#### Other Built-in Types

##### Classes
A class is a template that can be used to create other objects. In the following example the class `Board` is used to create an instance named `map_1`
```python
class Board:

    map = []
    
    def __init__(self, height,width):
        "Create new game boards"""
        self.height = height
        self.width = width
        
    def build_board(self):
        "Print the game map to the terminal"""
        for count, i in enumerate(range(0, self.height)):
            self.map.append([])
            for j in range(0, self.width):
                self.map[count].append([])

    def print_board(self):
        for row in self.map:
            print(row)

map_1 = Board(10,10)
map_1.build_board()
map_1.print_board()
```
which outputs:
```bash
[[], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], []]
```

##### Functions

create an empty function
```python
def useless_function():
     """this doesn't do anything useful"""
     pass
```
create a function that returns the first two and last two characters in a string
```python
def bookends(string, size=2):
    """for a given string return the first size and last size characters
    if the string is less than size*2 characters long return None"""
    result = None
    if len(string) >= size*2:    
        result = (string[0:size],string[-size:])
    return result    
```
create a function that is decorated by another function (this is very powerful)


##### Generators
create a generator that returns numbers from a range, and when it runs out of numbers it prints a message
```python
def number_grow(start,end,message=None):
    for i in range(start, end, message):
        yield i
    print(message)
```
initialize the above generator function and pass the parameters start, end, and message
```python
my_numbers = number_grow(1,3,'wow!')
# call next on the generator
next(my_numbers)
```

### Popular and useful modules:
* collections: Container datatypes [docs](https://docs.python.org/3/library/collections.html)
     * `Counter(x).most_common(10)`, returns a list of tuples of the 10 most common items in the iterator `x`.
* itertools: Functions creating iterators for efficient looping [docs](https://docs.python.org/3/library/itertools.html)
     * `itertools.count(5,3)`, returns a generator that starts at `5` and counts by `3`.
     * `itertools.cycle('EATING')`, returns a generator that loops over the list `[E,A,T,I,N,G]` forever
     * `itertools.repeat(10, 15)`, returns a generator that repeats `100` `15` times.
     * `itertools.compress('FRZG',[1,0,1,0])` , returns a generator that includes only those items that occur at the same index as 1's: `F,Z`
     * `itertools.permutations('SOS')`, returns a generator that includes all possible orderings of the input with no repeated elements.
* pickle: Python object serialization [docs](https://docs.python.org/3/library/pickle.html)
     * `pickle.dump(obj, file)`, takes `obj` and writes it to `file` for later retreiveal using: `pickle.load(file)`
* urllib: URL handling modules [docs](https://docs.python.org/3/library/urllib.html)
     * `urllib.parse.urlparse("https://www.google.com/search?term=cool+stuff&result=100")`, returns `ParseResult(scheme='https', netloc='www.google.com', path='/search', params='', query='term=cool+stuff&result=100', fragment='')`
* math: Mathematical functions [docs](https://docs.python.org/3/library/math.html)
     * `math.floor(3.032)` = `3.0`
     * `math.ceil(3.032)` = `4.0`
* random: Generate pseudo-random numbers [docs](https://docs.python.org/3/library/random.html)
     * `random.seed(212)`, sets the seed to `212` so that random results will be the same every time you call random: very useful for writing tests that rely on the random module
     * `random.choice([2,3,4])` = `3` (result is random, so your result may vary)
     * `random.choices([2,3,4,5,6,7],k=2)` = `[2,5]` (result is random, so your result may vary)
     * `random.random()`, returns a number in the range 0.0 to 1.0
* uuid: UUID objects according to RFC 4122 [docs](https://docs.python.org/3/library/uuid.html)
     * `uuid.uuid1(1222)`, returns `UUID('3c712e12-0d20-11ea-befa-0000000004c6')`, useful for generating unique identifiers on-the-fly (as needed).
* subprocess: Subprocess management [docs](https://docs.python.org/3/library/subprocess.html)
     * `subprocess.run(["mkdir","stuff"])`, creates a new directory named `stuff` in the current directory. Useful for running shell commands within Python.
* argparse: Parser for command-line options, arguments and sub-commands [docs](https://docs.python.org/3/library/argparse.html)
     * 
file my_random_num.py
```python
import argparse     
import random

parser = argparse.ArgumentParser(description='Return a random number less than x')
parser.add_argument('max_number', type=int, help='the max number from which to select a random number (0...max)')

args = parser.parse_args() 

result = random.choice(range(0,args.max_number))
print(result)
```

run the file in the terminal

`python3 my_random_num.py 30`

returns a random number from 0 to 29

* pathlib: Object-oriented filesystem paths [docs](https://docs.python.org/3/library/pathlib.html)
     * `Path('X').exists()`, returns True if the path `X` exists
     * `Path('X').glob('*.txt*)`, returns all files within the path `X` that end in `.txt`
     * `Path('X').glob('**/*.txt'))`, returns all paths in directories and subdirectories in the path `X` that end in `.txt`.
* datetime: Basic date and time types [docs](https://docs.python.org/3/library/datetime.html)
     *
Calculate the number of days until the US presidential election in 2020
```python
import time
from datetime import date

today = date.today()
us_election = date(today.year+1, 11, 1) # November 1st 2020
days_until_election = abs(us_election - today)
print(days_until_election
```
, results in the answer `347 days, 0:00:0`

## Bonus Python Links!
Free resources to practice programming
* [Code Kata](http://codekata.com/)
* [The Python Challenge](http://www.pythonchallenge.com/)
* [Code Wars](https://www.codewars.com/)
* [Project Euler](https://projecteuler.net/)

## Exercise #3 (16 min.)

1. **5 min**: Browse the Python standard library and choose a module that looks intersting.
2. **10 min**: Write a small Python program that uses one of these modules.
3. **1 min**: Present your script and results to the class.
