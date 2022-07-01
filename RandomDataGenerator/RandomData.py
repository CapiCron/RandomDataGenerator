#Imports
#--------------------------
import random
#--------------------------
#Data Sets
#--------------------------
#Names
def nameCollection():
    #Opens file
    f = open("Names.txt","r")
    #Create array of names
    namesArray = []
    #loop through file to add names
    for x in f:
        #Add names to the list and remove trailing newlines etc.
        namesArray.append(x.rstrip())
    #Close the file
    f.close()
    return namesArray
namesArray = nameCollection()
#Surnames
def surnamenameCollection():
    #Opens file
    f = open("Surnames.txt","r")
    #Create array of names
    surnamesArray = []
    #loop through file to add names
    for x in f:
        #Add names to the list and remove trailing newlines etc.
        surnamesArray.append(x.rstrip())
    #Close the file
    f.close()
    return surnamesArray
surnamesArray = surnamenameCollection()
#StreetNames
def streetNameCollection():
    #Opens file
    f = open("StreetNames.txt","r")
    #Create array of names
    streetArray = []
    #loop through file to add names
    for x in f:
        #Add names to the list and remove trailing newlines etc.
        streetArray.append(x.rstrip())
    #Close the file
    f.close()
    return streetArray
streetArray = streetNameCollection()
#DialCodes
def dialCodes():
    dialCodeCell =["071","072","073","074","081","082","083","084","011","012","010","021","013","022"]

    return dialCodeCell
def createNumber():
    temp = ""
    i=0
    while i < 7:
        temp += str(random.randint(0,9))
        i += 1

    return temp[:3]+'-'+temp[3:]
#--------------------------
dialCodesArray = dialCodes()
#Generate a person
def createPerson():
    #Name
    varName = namesArray[random.randrange(0,len(namesArray)-1)]
    #Surname
    varSurname = surnamesArray[random.randrange(0,len(surnamesArray)-1)]
    #Street
    varStreet = streetArray[random.randrange(0,len(streetArray)-1)]
    #Number-Dial
    varDial = dialCodesArray[random.randrange(0,len(dialCodesArray)-1)]
    varFullNumber = varDial +'-'+ createNumber()

    print("Name:",varName)
    print("Surame:",varSurname)
    print("Street:", random.randrange(1,200) ,varStreet)
    print("Number:",varFullNumber)

createPerson()