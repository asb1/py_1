#!/usr/bin/python
class Parent : #define parent class
    parentAttr=100
    def __init__(self):
        print "Calling parent connstructor"

    def parentMethod(self):
        print "Calling parent method"

    def setAttr(self, attr):
        Parent.parentAttr =attr

    def getAttr(self):
        print "Parent Atrribute :", Parent.parentAttr


class Child(Parent): #define child class
    def __init__(self):
        print "Calling child constructor"

    def childMethod(self):
        print 'Calling child method'


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
# instance of child
# child calls its method
# calls parent's method
# again call parent's method
# again call parent's method