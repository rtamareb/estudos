 #Even or Odd
#print ("Exemple #1")
# number = int(input("Type any positive number "))

# def even_or_odd(number):
#    rest = number % 2
#    if rest == 0:
#        evenodd = "Even/Par"
#        return evenodd
#    else:
#        evenodd = "Odd/Ímpar"
#        return evenodd
   
# result = even_or_odd (number)
# print (f"The number is {result}") 
# print ("")

# print ("Exemple #2")
# number = int(input("Type any positive number "))

# def even_or_odd(number):
# 	return 'Odd/Ímpar' if number % 2 else 'Even/Par'

# result = even_or_odd(number)
# print (f"The typed number is {result}")
# print ("")

print ("Exemple #3")
number = int(input("Type any positive number "))

def even_or_odd(number):
	return 'Even/Par' if number % 2 == 0 else 'Odd/Ímpar'

result = even_or_odd(number)
print (f"The typed number is {result}")
print ("")