# Author: Alex Dammann
# Date: 6/17/2022

end = 1
while end == 1:
        FirstName = input ("First Name? ")
        if FirstName == ("ZZZ"):
            break
        else:
            LastName = input ("Last Name? ")
            if LastName == ("ZZZ"):
                break
            else:
                GPA = float(input("GPA? "))
                if GPA >= 4.0:
                    print ("Top of the Class! Hard work really pays off! Congratulations!")
                elif GPA >= 3.5:
                    print ("You have made the Deans List! Congrats!")
                elif GPA >= 3.25:
                    print ("You have made the Honor Roll! Congrats!")
                elif GPA >= 3.0:
                    print ("Almost to Honor Roll! Keep Trying!")
                elif GPA >= 2.5:
                    print ("Average C student isnt bad but can be better!")
                else:
                    print ("I would study more if I were you...")
