NhsNumberValidation
===================

This package will help validate NHS numbers in python. 


### Installation

Installation of this package is as simple as downloading the source code and running:

```python
    python setup.py install
```


### Usage

Once imported the validate method can recieve nhs numbers in the format.
 - 'xxxxxxxxxx' (10 numeric characters as a string)
 - or, with a combination of spaces or hypens. (xxx-xxx-xxxx, xxx xxx xxxx)

```python
    from nsh import validate

    try:
        if validate('11111'):
            print 'Valid'
        else:
            print 'invalid'
    except ValueError as e:
        print 'Value error means NHS number was not in the format xxxxxxxxxx'
```
