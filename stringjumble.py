"""
stringjumble.py
Author: CuPyrtch
Credit: None

Assignment: String Jumble

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

input1 = input("Please enter a string of text (the bigger the better): ")

print("You entered \"" + input1 + "\". Now jumble it:")

length = len(input1)
output = ""
for i in range(length-1, -1, -1):
    output = output + input1[i]
print(output)

output = ""
begin = length-1
end = length
for i in range(length-1, -1, -1):
    if input1[i] == " ":
        begin = i+1
        output = output + input1[begin:end] + " "
        end = i
    elif i == 0:
        begin = i
        output = output + input1[begin:end]
print(output)

output = ""
begin = 0
end = 0
for i in range(0, length):
    if input1[i] == " ":
        end = i-1
        for j in range(end, begin-1, -1):
            output = output + input1[j]
        output = output + " "
        begin = i+1
    elif i == length-1:
        end = i
        for j in range(end, begin-1, -1):
            output = output + input1[j]
print(output)