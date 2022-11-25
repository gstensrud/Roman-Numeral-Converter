print ("\n\t\t Number to Roman Numeral Converter!")
try:
    userNumber = int(input ("\n\t\t Please enter a number between 1 and 39999: ").strip())
    goodNumber = True
   
except:
    print ("********NOT A NUMBER...YOU MUST ENTER A WHOLE NUMBER**********")
    goodNumber = False

newNumber = str(userNumber).zfill(4)
thousands = int(newNumber[0])
hundreds = int(newNumber[1])
tens = int(newNumber[2])
ones = int(newNumber[3])
print ("\t Thousands Place: {}, Hundreds Place: {}, Tens Place: {}, Ones Place:{}".format(thousands, hundreds, tens, ones))
print ("\t\t The user entered: {}".format(userNumber))

if ones == 0:
    numeralOnes = ""
elif ones < 4:
    numeralOnes = ones * "X"
elif ones == 4:
    numeralOnes = "I"
elif ones == 5:
    numeralOnes = "V"
elif ones < 9:
    numeralOnes = "V" + (ones - 5) * "I"
elif ones == 9:
    numeralOnes = "IX"


if tens == 0:
    numeralTens = ""
elif tens < 4:
    numeralTens = tens * "X"
elif tens == 4:
    numeralTens = "XL"
elif tens == 5:
    numeralTens = "L"
elif tens < 9:
    numeralTens = "L" + (tens - 5) * "X"
elif tens == 9:
    numeralTens = "XC"

if hundreds == 0:
    numeralHundreds = ""
elif hundreds < 4:
    numeralHundreds = hundreds * "C"
elif hundreds == 4:
    numeralHundreds = "CD"
elif hundreds == 5:
    numeralHundreds = "D"
elif hundreds < 9:
    numeralHundreds = "D" + (hundreds - 5) * "C"
elif hundreds == 9:
    numeralHundreds = "CM"

if thousands == 0:
    numeralThousands = ""
elif thousands < 4:
    numeralThousands = thousands * "M"

romanNumeral = numeralThousands, numeralHundreds, numeralTens, numeralOnes

print ("\n\n\t You entered {} as a number.".format(userNumber))
print ("\n\t\t That number changed into Roman Numerals is:" +
       "\n\t\t\t\t {}{}{}{}.".format(romanNumeral))




































    
