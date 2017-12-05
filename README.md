# unittest for python

## purpose

- examples followings
1. master of basic of unittest
1. can make some package

## package

- example: https://github.com/kennethreitz/samplemod
- setup.py: https://github.com/kennethreitz/setup.py
- add `test_suite='tests'` in setup.py, then do all test by using following.
```
python setup.py test
```

## command

- test for some class
```
$ python -m unittest [script].[test_case]

ex)
python unittest_hello.py -v
python -m unittest unittest_hello.TestHelloUnitTest

```

- test fo some method
```
$ python -m unittest [script].[test_case].[method]

ex)
python -m unittest unittest_hello.TestHelloUnitTest.test_add
```

## list of assersion

- https://docs.python.org/3/library/unittest.html#assert-methods
- important
```
assertEqual(a, b)
```

# githook

- setup
```
ln -s $(dir=`pwd`; echo ${dir}/.git_template/hooks) .git/hooks
```

- or set template on git/config
```
git config init.templatedir ~/.git_template/
```
