import os
directory = input("Enter directory path and name: ")
try:       
    # creating a folder named data 
    if not os.path.exists(directory): 
        os.mkdir(directory)
    print("Directory created\n")
except OSError: 
    print ('Error: Creating directory of data') 
