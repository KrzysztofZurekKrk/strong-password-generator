import random
import array
import sys
 
#input length of the generated password
try:
    pass_length = int(input("Please provide required length of password: "))
    if pass_length < 0:
        sys.exit("Wrong input. Make sure to use positive numbers")
except ValueError:
    sys.exit("Wrong input. Make sure to use numbers")

#declare arrays of the characters used for password creation
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lowercase_char = ['a', 'b', 'c', 'd', 'e', 
                'f', 'g', 'h', 'i', 'j', 
                'k', 'l', 'm', 'n', 'o', 
                'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 
                'z']
 
uppercase_char = ['A', 'B', 'C', 'D', 'E', 
                    'F', 'G', 'H', 'I', 'J', 
                    'K', 'L', 'M', 'N', 'O', 
                    'P', 'Q', 'R', 'S', 'T', 
                    'U', 'V', 'W', 'X', 'Y', 
                    'Z']
 
symbols = ['@', '#', '$', '%', 
            '=', ':', '?', '.', 
            '/', '|', '~', '>',
            '*', '(', ')', '<',
            ';', '^', '+']
 
#combines all the character arrays above to form one array
combined_list = digits + uppercase_char + lowercase_char + symbols

#randomly select characters
i = 1
password = ""
while i <= pass_length:
    password = password + random.choice(combined_list)
    i += 1

#print out password
print(password)