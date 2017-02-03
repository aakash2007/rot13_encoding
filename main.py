from encode import *

s = input("Enter Your String: ")

s2 = "".join([d.get(c,c) for c in c])

print("Encoded String: " + s2)