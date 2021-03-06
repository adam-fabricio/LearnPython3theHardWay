"""Exercise 42 - IS-A, Objects, and Classes."""


## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ##Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    
    def __init__(self, name):
        # Person has-a name
        self.name = name
        # Person has-a pet of some kind
        self.pet = None


## Employee is=a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employe has-a name. hmm  what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary


## Fish is-a object
class Fish(object):
    pass


## Salmon is-a fish
class Salmon(Fish):
    pass


## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a satan pet, satan is-a Cat.
mary.pet = satan

## frank is-a Employee, named Frank and salary of 120000
frank = Employee("Frank", 120000)

## frank has-a rover pet, rover is a Dog.
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon

## harry is-a Halibut
harry = Halibut()
