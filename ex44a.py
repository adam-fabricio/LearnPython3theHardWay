"""
Inherance versus Composition.
a. inherance
"""


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

"""Child herda a função implicit da classe pai."""
