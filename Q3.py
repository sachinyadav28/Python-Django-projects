#Write a Python program that accepts a sentence and calculates the number of letters
#and digits.
#Suppose the following input is supplied to the program:
#>> hello world! 123
#Then, the output should be:
#>> LETTERS 10
#DIGITS 3


z=input("Type letters and digits!! ")
l=0
d=0
for y in z:
    if y.isdigit():
        d = d + 1
    else:
        l=l + 1

print(f"LETTERS  {l}")
print(f"DIGITS  {d}") 
