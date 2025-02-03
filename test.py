x = 10  # Global variable

def change_x():
    global x  # Declare x as global

# change_x()
print(x)  # Output: 20
