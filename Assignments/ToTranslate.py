# Translate from c++ to python
def menu():

    print("Menu of Options: ")
    print("1: Tell me a joke ") 
    print("2: Show my to-do list ")
    print("3: Add to my to-do list  ")
    print("4: Check from my to-do list")
    print("5: Exit")

#function to tell a joke
def  tell_jokes():
    print("\nWhat did the Ice Man say to the Bird Boy?\n Stay COOL!!!")

#function to print out the to do list
def show_to_do_list():

    f = open("./Assignments/To-Do-list.txt","r")

    content=f.read()
    print(content)
    
    f.close()

#Function to add more things to the list
def add_to_do_list():
    
    f = open("./Assignments/To-Do-list.txt","a")
    add = input(" ")
    f.write(add)
    print("Added to the list.")
    f.close()

def check_from_list(index):
    f = open("./Assignments/To-Do-list.txt","r")
    lines = f.readlines()

    with open("./Assignments/To-Do-list.txt","w") as writer:
        for i, line in enumerate(lines):
            if i != index:
                writer.write(line.strip() + "\n")

                print(line.strip())



while True:
    menu()

    try:
        choice = int(input("What would you like to do?"))
    except ValueError:
        print("Input an integer.")

    if choice == 1:
        print("Disclaimer!! This joke will crack your Rib")
        tell_jokes()
    elif choice== 2:
        print("Below is your to do list")
        show_to_do_list()

    elif choice == 3:
        add_to_do_list()

    elif choice == 4:
        print("Enter the index you want to search from.")
        try:
            index = int(input())
            check_from_list(index)
        except ValueError:
            print( "The input is not an interger.")
        

    elif choice ==5:
        print("Exited the program!!")
        break
    else:
        print("Enter the correct values")
