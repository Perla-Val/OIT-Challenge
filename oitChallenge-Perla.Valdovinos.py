# By: Perla Valdovinos
# this is for the OIT code challenge. This program changes decimals to Roman Numerals
# this project took 2 hours to compleate 
# I was trying to make a function that would compare the roman numerals and produce the equation, it did not work
#this program is ran by the terminal, I did not have nough time to compleate it this week
#if i had more time I would have figured out the function for both and it was going to be a question type thing
#thank you for the opportunity and I hope to hear back from you

class Roman:
    if roman== "I":
        roman= 1 
    if roman =="V":
        roman= 5
    if roman == 'X':
        roman= 10
    if roman == 'L':
        roman= 50
    if roman == 'C':
        roman= 100
    if roman == 'D':
        roman= 500
    if roman == 'M':
        roman= 1000

    def __init__(self, str):
        num = 0
        i = 0
 
    while (i < len(str)):
 
        # Getting value first sym
        s1 = value(str[i])
 
        if (i + 1 < len(str)):
 
            
            s2 = value(str[i + 1])
 
            # Comparing both values
            if (s1 >= s2):
 
                # is symb 1 is grater than symb 2?
                num = num + s1
                i = i + 1
                
            else:
 
            
                num = num + s2 - s1
                i = i + 2
                
        else:
            num = num + s1
            i = i + 1
            
        return num
 
            
        



#will u need to conver decimals to roman numerals or roman numerals ro decimals?
start= input("If you would like to convert a Roman Numer to a Decimal enter 1 or if you would like to convert a Decimal to a Roman Numeral enter 2 ")
# declare roman variables 

#if roman to decimal
if start== "1" :
    #ask how many numers
    roman= input("Please enter the Roman Numeral: ")

elif :


 
    
print(Roman.__init__(roman))
    

#else decimal to roman 

#ask if they would like to enter new number, switch, or end?