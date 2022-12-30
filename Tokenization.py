import re
string= input ("Enter the String :")
print("Original String : " + str(string)) #original string
res = [sub.split() for sub in string] # tokenization string
print("After tokeniznation the String: " + str(res))
