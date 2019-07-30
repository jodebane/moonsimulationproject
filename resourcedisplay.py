#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joseph Foley
#
# Created:     25/06/2019
# Copyright:   (c) Joseph Foley 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
###

###display of resources for moon base
class resourcebar():
    def __init__(self, population, energy, cash, territory):
        self.population = population
        self.energy = energy
        self.cash = cash
        self.territory = territory
#returns resource quantities
    def getpop(self):
        return self.population
    def getenergy(self):
        return self.energy
    def getcash(self):
        return self.cash
    def getterritory(self):
        return self.territory
##adds resources to resource bar
    def addpop(self,newpop):
        self.population = ((self.population)+newpop)
        return self.population
    def addenergy(self,newenergy):
        self.energy=((self.energy)+newenergy)
        return self.energy
    def addcash(self,newcash):
        self.cash=((self.cash)+newcash)
        return self.cash
    def addterritory(self, newterr):
        self.territory = ((self.territory)+newterr)
        return self.territory

    def deletepop(self,lesspop):
        self.population=((self.population)-lesspop)
        return self.population

    def deletenergy(self,lessenergy):
        self.energy=((self.energy)-lessenergy)
        return self.energy

    def deletecash(self,lesscash):
        self.cash=((self.cash)-lesscash)
        return self.cash

    def deleteterritory(self,lessterr):
        self.territory=((self.territory)-lessterr)
        return self.territory




    def printresources(self):
        print(self.population, " citizens")
        print(self.energy, " hygawatts")
        print(self.cash, " $")
        print(self.territory, " sqkm")


##p1 resources is default starting resources on the first turn
p1resources = resourcebar(10,5,10,6)

def currentresourcebar():

    return p1resources



def newcash(n):
    currentresourcebar().addcash(n)


def newpop(n):
    currentresourcebar().addpop(n)








