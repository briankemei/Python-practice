# Creating a class 
'''
Define a class
Create objects 

'''
class Person:
    counter =0 #This a class attribute shared 
    
    #Method that initializes the object attributes
    def __init__(self, name, age): # Define instance attributes 
        self.name= name
        self.age = age
    # Creating of instance methods
    def greet(self):
        return f"Hello {self.name}, you have said your age is {self.age}."



#Class inheritance passing the class person as a paremeter
class Student(Person):
    #passees the attributes of the person class and class attributes.
    def __init__(self,name,age,classification):

        super().__init__(name,age)#allows a child class to access attributes of the parent class
        self.classification = classification
        
    #Method to know someones name age and year of studies
    def greet(self):
        return super().greet() + f"My classification is {self.classification}"


morehouse = Student("Brian",24,"Junior")
print(morehouse.greet())

class track(Student):
    def __init__(self,name,age,classification,event):
        super().__init__(name,age,classification)
        self.event =event

        # method to display event participation
    def track_event(self):
        # Concatination to return 
        return super().greet() + f". My event is {self.event}"

athlete = track('Brian',25,'junior','5000M')
print(athlete.track_event())