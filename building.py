#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joseph Foley
#
# Created:     13/07/2019
# Copyright:   (c) Joseph Foley 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##building class
class building():
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.initfunction = []
        self.perturnfunction = []
#allows initial functions to be added to building objects
    def addinitfunction(self, effectstring):
        self.initfunction.append(effectstring)
#allows per turn effects to be adedd to building objects
    def addperturnfunction(self,effectstring):
        self.perturnfunction.append(effectstring)
    def printname(self):
        print(self.name)
    def printcost(self):
        print(self.cost)
    def printinitfunction(self):
        print(self.initfunction)
    def printperturnfunction(self):
        print(self.perturnfunction)
##    def printinfo(self)
    def printall(self):
        self.printname()
        self.printcost()
        self.printinitfunction()
        self.printperturnfunction()


