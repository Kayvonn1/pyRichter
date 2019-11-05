#Python Richter Scale Calculation
#Your first and last name:dd;d;d;d
#Your ID:lslsd

#Requirements Version 1:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
# display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)

#Additional Requirements Version 2:
# ask the user to 'Enter the Richter scale value or -99 to end: '
#   if richter = -99, end the program

# make sure richter scale value is greater than 0
#   if not, print "Value must be greater than 0"
#   and make them enter another value


# Test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6
domore = True 
while domore == True:
        richter = float(input("Enter Ricther Scale Value or -99 to end"))
        
                
        if richter == -99:
                domore = False
                
        elif richter <= 0:
                print ("Value must be greater than 0")
                
        if richter >= 8.0:
                print ("Most structures fall")

        elif richter >=7.0:
                print ("Many buildings destroyed")
                
        elif richter >= 6.0:
                print ("Many buldings considerably damged, some collapse")

        elif richter >= 4.5:
                print ("Damage to poorly constructed buldings")

        elif richter >= 0:
                print ("No destruction of buildings")
                
      
                

