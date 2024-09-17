'''Class Human 
Has properties(features) and methods (activities) '''
class Human:
    
    # Constructor to initialize name and occupation attributes
    def __init__(self, na, work):
        self.name = na  # 'name' stores the person's name
        self.occupation = work  # 'occupation' stores the person's job or role

    # Method to print the type of work based on the person's occupation
    def type_of_work(self):
        # Check if the occupation is "Student"
        if self.occupation == "Student":
            print(self.name, "Goes to Morehouse college")
        # Check if the occupation is "Tennis"
        elif self.occupation == "Tenis":
            print(self.name, "You play tennis")
        # Default case for any other occupation
        else:
            print(self.name, self.occupation)

    # Method to print a running activity (for Adidas)
    def runs(self):
        print(self.name, "For Adidas")

# Create an instance of the Human class with the name 'Brian' and occupation 'Student'
tom = Human('Brian', 'Student')
tom.type_of_work()  # Call the method to print the type of work
tom.runs()  # Call the method to print running activity

print("\n")  # Print a newline for clarity

# Create another instance of the Human class with the name 'Aniaba' and occupation 'Student'
Aniaba = Human('Aniaba', 'Student')
Aniaba.type_of_work()  # Call the method to print the type of work
Aniaba.runs()  # Call the method to print running activity
