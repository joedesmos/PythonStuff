<<<<<<< HEAD
import time


def loop_thing():
    grr = False
    while grr == False:
        try:
            what_mode = (input("Would you like to Add, Subtract, Divide, or Multiply."))
            if what_mode in ["add", "ADD", "Add"]:
                grr = True
            else:
                raise ValueError
            if what_mode in ["subtract", "SUBTRACT", "Subtract"]:
                grr = True
            else:
                raise ValueError
            if what_mode in ["divide", "DIVIDE", "Divide"]:
                grr = True
            else:
                raise ValueError
            if what_mode in ["multiply", "MULTIPLY", "Multiply"]:
                grr = True
            else:
                raise ValueError
        except ValueError:
            print("Please type one of the options >:(")
    return what_mode
what_mode = loop_thing()
def loop_thing_one():
    grr = False
    while grr == False:
        try:
            add_first_number = float(input("Please input your first number: "))
            grr = True
        except ValueError:
            print("Please type a number >:(")
        return add_first_number
add_first_number = loop_thing_one()

def loop_thing_two():
    grr = False
    while grr == False:
        try:
            add_second_number = float(input("Please input your second number: "))
            grr = True
        except ValueError:
            print("Please type a number >:(")
    return add_second_number
add_seond_number = loop_thing_two()

print("Calculating...")
time.sleep(1)
add_answer = print(add_first_number + add_seond_number)
time.sleep(0.5)
print("Thanks for using the cool calcuator 🗿")
=======
#Calculator Program
#Made by Ryland DeSantis

#Lists

addlist = ['add', 'a']
subtractlist = ['subtract', 's', 'sub']
multiplylist = ['multiply', 'm', 'mult']
dividelist = ['divide', 'd']

#Variables

input1 = 0
input2 = 0
calculator = True

#Functions

def add(input1, input2):print(input1 + input2)
def subtract(input1, input2):print(input1 - input2)
def multiply(input1, input2):print(input1 * input2)
def divide(input1, input2):print(input1 / input2)

def reset():
    input1 = 0
    input2 = 0
    calculator = True

#Program

while calculator:
    reset()
    choice = input('\nWould you like to add, subtract, multiply, or divide?: ').lower()
    try:

        if choice in addlist:
            print('\nYou chose to add.')
            input1 = float(input('First Number: '))
            input2 = float(input('Second Number: '))
            add(input1, input2)
        if choice in subtractlist:
            print('\nYou chose to subtract.')
            input1 = float(input('First Number: '))
            input2 = float(input('Second Number: '))
            subtract(input1, input2)
        if choice in multiplylist:
            print('\nYou chose to multiply.')
            input1 = float(input('First Number: '))
            input2 = float(input('Second Number: '))
            multiply(input1, input2)
        if choice in dividelist:
            print('\nYou chose to divide.')
            input1 = float(input('First Number: '))
            input2 = float(input('Second Number: '))
            divide(input1, input2)
        else:
            continue

    except ValueError:
        print('\nPlease type an option.')
        continue
>>>>>>> 9cbdaad851527510025703ce34f9d9c53f7087ce
