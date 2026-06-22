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
