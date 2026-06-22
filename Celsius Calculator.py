
import time


name = input("Today we will be converting Fahrenheit to celsius. Lets start by getting to know your name.")
print ("Nice to meet you "+name+", my name is joe desmos.")
fahrenheit = int(input("Type in any degree of Fahrenheit."))
celsius = ((fahrenheit-32)*(5/9))
print("calculating....")
time.sleep(1.25)
print ("Here is your fahrenheit degree in celsius:", celsius)
