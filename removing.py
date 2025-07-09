# Remove First and Last Character
# Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.
#
#Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.
# In a s = ["k", "z", "x", "b", "t"]:
#    "k" is position 0 or -5
#    "z" is position 1 or -4
#    "x" is position 2 or -3
#    "b" is position 3 or -2
#    "t" is position 4 or -1
#  
# s[1:-1] means position 1 (or -2) until 4(or -1 ==> not including -1) from where b 1 is a Python slice that returns a substring starting from the second character (index 1) up to, but not including, the last character (index -1). This effectively removes the first and last characters of the string.
# print ('')
# print ("Example #1")
# print ("Removing first and last character")
# def remove_first_last_char(text):
#     if len(text) > 2:
#         return text[1:-1]
#     else:
#         print ("The word must have 3 or more characters")
#         quit()

# text = input("Type any word with 3 or more characters: ")
# new_text = remove_first_last_char(text)
# print ("") 
# print (f"The original word {text} after function is {new_text}") 

print ("")
print ("Example #2")
print ("Removing last character")
def remove_last_char(text):
    if len(text) > 2:
        return text[:-1]
    else:
        print ("The word must have 3 or more characters")
     

text= input("Type any word with 3 or more characters: ")
new_text = remove_last_char(text)
print ("") 
print (f"The original word {text} after function is {new_text}") 

print ("")
print ("Example #3")
print ("Removing first character")
def remove_first_char(text):
    if len(text) > 2:
        return text[1:]
    else:
        print ("The word must have 3 or more characters")
        quit

text= input("Type any word with 3 or more characters: ")
new_text = remove_first_char(text)
print ("") 
print (f"The original word {text} after function is {new_text}") 

