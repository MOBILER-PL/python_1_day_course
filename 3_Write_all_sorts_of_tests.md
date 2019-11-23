## Python: Code, Test, Deploy

# Write all sorts of tests
 ---

# Synopsis

# Write all sorts of tests
Source: https://docs.pytest.org/en/latest/

We will primarily focus on the following testing types in this course:
* Unit testing [wikipedia](https://en.wikipedia.org/wiki/Unit_testing),test individual functions, modules, and classes
* Integration testing [wikipedia](https://en.wikipedia.org/wiki/Integration_testing),combining individual objects together and testing them as a group
* Acceptance testing [wikipedia](https://en.wikipedia.org/wiki/Acceptance_testing),a suite of tests designed to verify that the software meets the requirements specified by the team. One example is testing an application by interacting with it from the front-end (via Chrome) instead of through API calls.

We will try to touch on all three, but at least 60% of our time in this module will be spent on unit testing using Pytest.

## What is Pytest?
A testing framework that helps make it "easy to write small tests, yet scales to support complex functional testing..." (docs.pytest.org)

### A Bare-bones test example
```python
def skip_every_other_letter(string):
    return string

def test_skip_every_other_letter():
    assert skip_every_other_letter('doe') == 'o'
```
the test is then run:
```bash
(venv) mr> pytest
======================================= test session starts ========================================
platform linux -- Python 3.6.8, pytest-5.3.0, py-1.8.0, pluggy-0.13.1
rootdir: /home/section_3/
collected 1 item                                                                                   

test_app.py F                                                                                [100%]

============================================= FAILURES =============================================
___________________________________ test_skip_every_other_letter ___________________________________

    def test_skip_every_other_letter():
>       assert skip_every_other_letter('doe') == 'o'
E       AssertionError: assert 'doe' == 'o'
E         - doe
E         + o

test_app.py:6: AssertionError
======================================== 1 failed in 0.06s =========================================
(venv) >
```
the function is refactored
```python
def skip_every_other_letter(string):
    limited = ""
    keep = range(0,len(string),2)
    for i in keep:
        limited+=string[i]
    return limited
```
and test is re-run
```bash
(venv) > pytest
======================================= test session starts ========================================
platform linux -- Python 3.6.8, pytest-5.3.0, py-1.8.0, pluggy-0.13.1
rootdir: /home/section_3_testing
collected 1 item                                                                                   

test_app.py .                                                                                [100%]

======================================== 1 passed in 0.01s =========================================
```
### Assert that a specific exception is raised
```python
import pytest

def divide_by_zero():
    return 10/0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_by_zero()
```
running Pytest now returns the following
```bash
(venv) > pytest
======================================= test session starts ========================================
platform linux -- Python 3.6.8, pytest-5.3.0, py-1.8.0, pluggy-0.13.1
rootdir: /home/section_3_testing
collected 2 items                                                                                  

test_2.py .                                                                                  [ 50%]
test_app.py .                                                                                [100%]

======================================== 2 passed in 0.02s =========================================
```
### Reduce clutter, use Classes to group tests

```python
class TestClass:
    def test_a(self):
        x = 23232
        assert '32' in str(x)

    def test_b(self):
        x = "rta"
        assert x[-1] == 'a'
```
call the test specifying the file
```bash
(venv) > pytest -q test_2.py
..                                                                                           [100%]
2 passed in 0.01s
```
## Exercise #4: (30 min)
1. Write 10 tests for functions that you'd like to develop
2. Run pytest
3. Watch all your tests fail
4. Develop your functions until all your tests pass

**TIP:** See how far you can take Pytest by reading this

## Bonus Testing Links!
* [The Hitchhiker's Guide to Python: Testing Your Code](https://docs.python-guide.org/writing/tests/)
