# Importing the necessary libraries
import sys
import clipboard
import json

#Initializing the json filename
SAVED_DATA = "clipboard.json"

#Function to add the clipboard data into the json file
def saveItems(filePath, data):
    with open(filePath, "w") as f:
        json.dump(data, f)

#Function to load the data from the clipboard json file 
def loadItems(filePath):
    try:
        with open(filePath, "r") as f:
            data = json.load(f)
            return data
    except:
            return {}

#Checking for the number of arguments
if len(sys.argv) == 2:
    #Assigning the argument value to a variable
    command = sys.argv[1]
    #Calling the loadItems() to get the data from json file
    data = loadItems(SAVED_DATA)
    #Checking if the command is 'save'
    if command == 'save':
       key = input("Enter a key: ")
       data[key] = clipboard.paste() 
       saveItems(SAVED_DATA, data)
    #Checking if the command is 'load'
    elif command == 'load':
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
        else:
            print("Key does not exist")
    #Checking if the command is 'list'
    elif command == 'list':
        print(data)

    else:
        print("Unknown command")
        
else:
    print("Please pass exactly one command")
