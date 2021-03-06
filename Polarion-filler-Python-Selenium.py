import time

import datetime
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/gaglueck/AppData/Local/chromedriver.exe')  # Optional argument, if not specified will search path.

questiontestcasenumber = "Hanyas tesztesetet szeretned kitolteni?"
questiontestrun = "Be van allitva a megfelelo testrun?"
count1 = 1
count2 = 2



def test():
    
    driver.get('http://www.google.com')
    
    q = driver.find_element(By.NAME, 'q')
    q.send_keys('webdriver')
    q.submit()
    
    

print (driver.title)
    
def acquireusername(*j_username):   
    with open("login.txt") as f:
        lines = [line.rstrip('\n') for line in f]
        j_username = lines[0]
        return j_username
          
def acquirepassword(*j_password):
    with open("login.txt") as g:
        lines = [line.rstrip('\n') for line in g]
        j_password = lines[1]
        return j_password
    
        ## Just login
def justlogin():                        
#!/usr/bin/python
    print('Elindult a login')
    
    
    driver.maximize_window()
    
    ''''x = int (input ('Kerlek add meg, hogy mely teszteseteket szeretned megnyitni Polarionban: '))'''
    
    time.sleep(2) # Let the user actually see something!
    driver.find_element_by_name('j_username').send_keys(acquireusername())
    driver.find_element_by_name('j_password').send_keys(acquirepassword())
    driver.find_element_by_name('rememberme').click()
    driver.find_element_by_name('submit').click()
        
    class element_has_css_class(object):

        def __init__(self, locator, css_class):
          self.locator = locator
          self.css_class = css_class
        
        def __call__(self, driver):
          element = driver.find_element(*self.locator)   # Finding the referenced element
          if self.css_class in element.get_attribute("class"):
              return element
          else:
              return False
      
    # Wait until an element with class 'myCSSClass' is visible
    wait = WebDriverWait(driver, 25)
    element = wait.until(element_has_css_class((By.CLASS_NAME, "polarion-ExecuteTest-resultArea"), "polarion-ExecuteTest-resultArea"))
    
    print('Belepes kesz')


##Textfield filler

def textfieldfiller():
    f = len(driver.find_elements_by_class_name("polarion-ExecuteTest-resultArea"));
    fRange = range(f);
    print('Szovegdobozok szama: {}'.format(f))
    
    index = 3
    
    while index != f+1:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/table/tbody/tr/td/div/table/tbody/tr[1]/td/div/div/table/tbody/tr[2]/td/div/div[2]/div/table/tbody/tr[5]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[' + str(index) + ']/td[7]/table/tbody/tr[1]/td/textarea').clear()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/table/tbody/tr/td/div/table/tbody/tr[1]/td/div/div/table/tbody/tr[2]/td/div/div[2]/div/table/tbody/tr[5]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[' + str(index) + ']/td[7]/table/tbody/tr[1]/td/textarea').send_keys('Passed') 
        index = index + 1  # This is the same as count = count + 1
    
    print('Szovegdobozok kitoltve')


        ##Fill verdict textbox
        
    driver.find_element_by_class_name("polarion-WatermarkTextArea").clear()
    
    current_time = time.strftime(r"%d.%m.%Y", time.localtime())
    driver.find_element_by_class_name("polarion-WatermarkTextArea").send_keys(current_time) 
             
    return;

        ##Greentick pusher
        
        
def greentickpusher():
    f = len(driver.find_elements_by_class_name("polarion-ExecuteTest-resultArea"));
    
    print('Zold pipak szama: {}'.format(f))
    
    index = 2
    
    while index != f+2:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/table/tbody/tr/td/div/table/tbody/tr[1]/td/div/div/table/tbody/tr[2]/td/div/div[2]/div/table/tbody/tr[5]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[' + str(index) + ']/td[8]/table/tbody/tr/td[3]/div/table/tbody/tr/td/div/img').click()
        index = index + 1  # This is the same as count = count + 1
    
    print('Zold pipak megnyomva')
    
    return;

def query_questiontestcasenumber(questiontestcasenumber):
      
        while True:    
            try:
                sys.stdout.write(questiontestcasenumber)
                choice = input().lower()
                int(choice)
            except ValueError:
                print("Nem szamot adtal meg.")
            else:
            #successfully parsed! 
            
                if int(choice) < 10000:      
                    print("A megadott tesztesetszam tul alacsony")
                elif int(choice) > 30000:
                    print("A megadott tesztesetszam tul magas")    
                else:
                    return choice
           
def query_questiontestrun_yes_no(questiontestrun, default="yes"):
    
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    
    while True:
        sys.stdout.write(questiontestrun + prompt)
        choiceTestr = input().lower()
        if default is not None and choiceTestr == '':
            continue
        elif choiceTestr == 'n':
            print ("Kerlek allitsd be a megfelelo testrunt")
            continue
        elif choiceTestr == 'y':
            print ("Koszi.")
            return valid[choiceTestr]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                         "(or 'y' or 'n').\n")
            
                
def main():
    
    test()
    '''print ("Kerlek adj meg egy ervenyes tesztesetszamot es ellenorizd, hogy VPN-n vagy-e.")
    q = query_questiontestcasenumber(questiontestcasenumber)
    website = 'https://seu40.gdc-bln03.t-systems.com/polarion/#/project/SKYWAYS/workitem?id=Satellic-' + str(q)
    driver.get(website);
    
    justlogin()
    
    query_questiontestrun_yes_no(questiontestrun)
        
    textfieldfiller()
    greentickpusher()
        
    return;'''

main()

#"/polarion/icons/default/enums/testrun_status_passed.png"
#//img[contains(@src,'passed.png')]