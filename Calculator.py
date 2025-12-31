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