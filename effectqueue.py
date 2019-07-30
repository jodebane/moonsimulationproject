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

class effectqueue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def printqueue(self):
        print(self.items)


    def dequeue(self):
        return self.items.pop()

    def length(self):
        return len(self.items)

turnqueue = effectqueue()

def addpopulation(popint):
    turnqueue.enqueue(str(popint)+ " citizens")

def addenergy(enint):
    turnqueue.enqueue(str(enint)+ " hygawatts")

def addcash(cashint):
    turnqueue.enqueue(str(cashint)+ " $")
def addterritory(terrint):
    turnqueue.enqueue(str(terrint)+ " sqkm")