import re
import ast
string= input ("Enter the String :")
print("Original String : " + str(string)) #Original string
res = [sub.split() for sub in string] #tokenization string
print("After tokeniznation the String: " + str(res))
code = ast.parse("print (a+ (b*c))") 
print(ast.dump(code)) #print ast
