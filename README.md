## Introduction
This repository contain unit testing examples for python.

## Why I am doing this?
Python unit testing gets confusing if you are using the base library. Python unit testing is flexible, but it requires some mental "kung foo" if you want to do it correctly. 

Note - sut refer to class which we are testing

We are currently covering following scenrio:

- SUT is calling external api
- SUT is calling a function
- SUT is calling a class
- SUT is call a context manager 

## Directory structure


* src
    * sut.py (this is what we are writing unit tests for)
    * nested_deps.py (nested class)
    * external_call_func.py (this file contains a function which gets called by sut.py)
    * context_manager_deps.py (this class contains a context manager which get called by sut.py)
    * context 

* tests
    * test_deps.py 

## Can I contribute to it? 
Yes

## How to play with it?

Clone the repo and install poetry and run following command

```
poetry install
```

```
poetry run pytest .
```


