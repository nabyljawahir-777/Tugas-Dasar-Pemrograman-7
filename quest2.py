for x in range (5):
    for y in range (5):
        if (y == 2):
            print ("0", end= " ")
        else:
            print ("x", end= " ")
    print()
print()
for x in range (5):
    for y in range (5):
        if ( y == 2 ):
            print ("0", end= " ")
        elif ( x == 0 or y == 0 ):
            print ("x", end= " ")
        elif ( x == 4 or y == 4):
            print("x", end= " ")
        else:
            print("0", end= " ")
    print()