The translation1.py is the file that contains the function I intend to add to the Twitter class,so that , when the user want the search results in translated form,it can be provided using the translator function, without using the google translate api.

Update the .travis.yml  with

```
before install:

-pip install translate
```
 for installing the module <b>translate</b>.
 
 
 It can also be added to other classes as well,as per requirement .
 
An example for the use case is shown in example1.py
