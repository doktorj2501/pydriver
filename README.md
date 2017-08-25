# pydriver                                      
#My Selenium Webdriver library in python2.7!                                    
#Tests are configured to use selenium grid and nosetests modules                                   
#Working knowledge of python, webdriver, and nosetests essential                                  
#You can pass variables in through the nosetests ini, which is a simple json object,                             
#OR through the command line, eg:                                                          
# nosetests test-subsites.py -s --tc-file noseconfig.ini --tc=browsers.browser:CHROME --tc=test_DNs.test_DN:yoursite.com                                            
#If using the ini, for security reasons you                                                                                           
#might want to keep the ini out of the repo, and let it live on the CI server instead                            
#Nosetests with xunit also makes a nice graph in Jenkins =)                                 
#You can spin up a selenium grid very quickly with Docker; there are many guides on this.                                   
#The pageobj and pagescript files are an include and a script that calls the include.                                               
#The idea is to make a driver object with all of a page's elements, and expected text,                                                   
#plus it has a built-in linkchecker, login/logout, simple but expandable post content function,                                            
#and even search test functionality!                                                       
#much proprietary functionality could be added to this suite,                                               
#but this is a decent foundation.                                                           
