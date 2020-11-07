def is_triangle(stick1,stick2,stick3):
    """If checks if there exist any triangle 
    with sides of length stick1, stick2,stick3."""
    sticks=[stick1,stick2,stick3]
    for i in sticks:
        if i > sum(sticks)-i:
            print("No")
            return True

    print("Yes")

def read_from_user():
    """It asks the user for tree values and a
    pass them as parameters to is_trignle."""
    stick1=int(input("Stick 1:"))
    stick2=int(input("Stick 2:"))
    stick3=int(input("Stick 3:"))
    is_triangle(stick1,stick2,stick3)

if(__name__=="__main__"):   
    read_from_user()



