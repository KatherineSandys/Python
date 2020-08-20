"""
Program to auto fill in time sheets

Ideas
-Add Task Number to Questions
-Add Project number to the Questions
-Change order of questions.
-Questions on a form instead of indiviual
-Save the pervious answers to a file
-load those pervious answers when starting program so you can just skip items with the correct answer
-Look at the screen to make sure the right box is up before clicking.  Sometimes the computer is slower then the delays allow.


"""

import pyautogui, sys
import time


#DEFULTS
year = 2020
hours = 8
task_number = '386'
projectID = 'INP-1528'


#get month
month = pyautogui.prompt(text='Enter what month you want(1-12): ', title='Month' , default='')
#month = int(input("Enter what month you want(1-12): "))
#day that the month starts on
start = int(pyautogui.prompt(text="Enter the day to start with: ", title="Starting Day"))
#get how many days
days = int(pyautogui.prompt(text="Enter the number of days to fill in: ", title='Days'))
#get the task number
#task_number = pyautogui.prompt(text="Enter the task number: ", title='Task #')
#get the projectID
#projectID = pyautogui.prompt(text="Enter the project ID: ", title='Project ID')


time.sleep(5) #time to get back to screen

#repeat for the number of days in the month
for nextday in range(start, (start+days)):
    pyautogui.moveTo(16,185) # opens new tracking
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(230,275) #click on place to fill date
    time.sleep(.1)
    pyautogui.click()
    time.sleep(.1)

    #set date - month + "/" + 1 + "/" + year
    pyautogui.write(str(month) +"/"+ str(nextday) +"/"+ str(year))
    pyautogui.press('tab')
    time.sleep(.1)

    pyautogui.moveTo(214,481) #click on place to create new task
    pyautogui.click()
    time.sleep(1)

    #set the task number
    pyautogui.write(task_number)
    time.sleep(.1)

    #tab to get to hours- 6 times
    for i in range(0, 4):
        pyautogui.press('tab')
        time.sleep(0.5)

    #set the hours- 8
    pyautogui.write('8')
    time.sleep(.1)

    #tab to get to project ID - 3 times
    for i in range(0, 2):
        pyautogui.press('tab')
        time.sleep(0.5)

    #set project ID
    pyautogui.write(projectID)
    time.sleep(.1)

    #to save changes - 2 times
    pyautogui.moveTo(51,189) #click on place to save
    time.sleep(.1)
    pyautogui.click()
    time.sleep(.1)
    pyautogui.click()



    #aprove part

    time.sleep(2)
    pyautogui.moveTo(280,189) #click to unlock
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(110,450) #click to signoff
    pyautogui.click()
    time.sleep(.5)

    pyautogui.moveTo(520,620) #click to Vote Now
    pyautogui.click()
    time.sleep(2)

    pyautogui.moveTo(1235,445) #click to Complete check box
    pyautogui.click()
    time.sleep(.1)

    pyautogui.moveTo(750,660) #click to Vote
    pyautogui.click()
    time.sleep(.1)
    pyautogui.write('c')
    pyautogui.press('enter')
    time.sleep(.1)

    pyautogui.moveTo(860,815) #click to Complete
    pyautogui.click()
    time.sleep(5)

pyautogui.alert(text = 'Done!', title='Complete')
