print("Hello world")
#"print" is a function, "Hello World" is an argument/parameter
#the whole thing is a statement

name = "Ian"
#This is also a statement, but "name" is a variable which contains "Ian", in this case, "Ian" is an expression
if name == "Ian":
    print("Hello World")
    print("How are you?")
# this is a conditional statement that creates a block, this block contains two string statements.

#Functions:

print() #shows the value of an argument on the terminal
input() #asks the user to introduce a value, it is a string by default
int() #converts suitable expressions into integers
float() #converts suitable expressions into floating-point numbers
str() #converts suitable expressions into string values
type() #shows the type of a variable on the terminal  
len() #creates a numerical value from the lenght of an expression

from math import sqrt
print(sqrt(2))