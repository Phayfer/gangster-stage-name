import random
import re

regularNames = []
stageNames = []

# pre defined list of names to generate the random name
listRandomName = ["Gargoyle", "Vampire", "Monster", "Bloody", "Zombie", "Spike", "Demon", "Dragon"]

# function to generate the random name using a pre defined list
def generateRandomName():
    # get the length of the random names
    length = len(listRandomName)

    # random choose a name from the randomList name
    return listRandomName[random.randint(0, length - 1)]


# create a variable to store the user want to generate
totStageName = 0

# counter
count = 1

try:
    # getting how many stage names the user want to generate
    # trying to convert the input to int and assign the value to totStageName
    totStageName = int(input("How many stage names do you want to create? "))
except:
    # if the user insert a invalid input, print a message to the user
    print("invalid input, please try again!")

# start the loop checking the counter
while count <= totStageName:

    # get the regular name input and assign to the variable
    regularName = input("Please digit " + str(count) + "o. name: ")

    # validation to refuse numbers in the regular name
    # example got from:
    # https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
    if re.search(r'\d', regularName):
        print("Numbers are not allowed")
        continue

    # split forename and surname into a list
    splitRegularName = regularName.split(" ")

    # validate if the user input contains at least one forename and one surname
    if len(splitRegularName) < 2:
        print("Please type name and surname!")
        continue

    # store the regular name in the list
    regularNames.append(regularName)

    # increment the counter
    count = count + 1

    # generate the stageName
    stageName = regularName[0].upper() + ". " + generateRandomName() + " " + splitRegularName[1].upper() \
                + " " + splitRegularName[0].lower() + " " + generateRandomName()

    # store the generated stage name
    stageNames.append(stageName)

    # print the stage name
    print("Regular name:", regularName)
    print("Generated stage name:", stageName)

    print("end")


