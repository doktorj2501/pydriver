# pydriver
#My Selenium Webdriver library in python!
#Tests are configured to use selenium grid and nosetests you can pass variables in through the nosetests ini, which is a simple json object,
#OR through the command line. You can spin up a selenium grid very quickly with Docker; there are many guides on this.
#The pageobj and pagescript files are an include and a script that calls the include. The idea is to make a driver object with all of a page's
#elements, and expected text, plus it has a built-in linkchecker!
