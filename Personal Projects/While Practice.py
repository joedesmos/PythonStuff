def eraser():
    marker = False
    while marker == False:
        try:
            questio_n = float(input("Type a number."))
            marker == True
        except ValueError:
            print ("That tis' not a number.")
    return marker
