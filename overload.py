import pynput
from time import sleep
from pynput.keyboard import Key, Controller

#set keyboard
keyboard = Controller()

#get user input on how long to sleep for
TSleep = float(input("Enter how long between each enter click in milliseconds: "))
TSleep = TSleep * 0.001 #getting to milliseconds for sleep to use
#get how long program should run for
run = float(input("How long do you want to run this program for in minutes: "))
run = run * 60 #getting to seconds

#figure out how many times to loop
loop = run / TSleep

sleep(5)
print("GO")

for x in range(0, int(loop)):
    keyboard.press(Key.enter)
    sleep(TSleep / 2)
    keyboard.release(Key.enter)
    sleep(TSleep / 2)

print("END")
