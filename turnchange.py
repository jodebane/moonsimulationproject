#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joseph Foley
#
# Created:     18/07/2019
# Copyright:   (c) Joseph Foley 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import resourcedisplay
import effectqueue


#returns a number based on string given by resource update
def returnresourceint(effectint):
    return int(effectint)

#returns a resource type based on resource update string
def returnresourcestr(effectstr):
    return str(effectstr)

#chooses an option from resourcedisplay module



##dictionary of selection of resourceupdate

resourceupdatekeys = {


}

#converts update string to a function to update resource display
def effect2display(effectstring):
    effectlist=effectstring.split()
    print(returnresourceint(effectlist[0]))
    print(returnresourcestr(effectlist[1]))
    ##choosing which resourcedisplayfunction to use
    resourceqty = returnresourceint(effectlist[0])
    resourcetype = returnresourcestr(effectlist[1])
    if resourcetype == 'citizens':
        resourcedisplay.p1resources.addpop(resourceqty)
    if resourcetype == 'hygawatts':
        resourcedisplay.p1resources.addenergy(resourceqty)
    if resourcetype == '$':
        resourcedisplay.p1resources.addcash(resourceqty)
    if resourcetype == "sqkm":
        resourcedisplay.p1resources.addterritory(resourceqty)

##effectqueue dequeue



##testing the turnchange mechanism with number of effects added to turnqueue
def testcase():

    effectqueue.addcash(10)
    effectqueue.addpopulation(10)
    effectqueue.addenergy(5)
    effectqueue.addterritory(5)


def turnchange(turnnum):
    resourcedisplay.p1resources.printresources()
    turnnum = turnnum + 1;
    print("resources for turn" + str(turnnum))
    testcase()
    while effectqueue.turnqueue.length() > 0:
        effect2display(effectqueue.turnqueue.dequeue())
    resourcedisplay.p1resources.printresources()


