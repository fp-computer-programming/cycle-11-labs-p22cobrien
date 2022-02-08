# Author: CMOB 2/8/2022

my_file = open("cycle-11-labs-p22cobrien/alma_mater.txt", "r")

while True:
     line = my_file.readline()
     if len(line) == 0:
           break
     print (line, end="")
     print("")
my_file.close()