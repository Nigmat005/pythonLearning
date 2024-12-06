str="welcom"
print(id(str))

str2=str+"to Python"
print(id(str2))
print("===========================================")
strA="welcom"
strB="welcom"
print("===========================================")
print(id(strA))
print(id(strB))
check= True if strA.__eq__(strB) else False
print(check)
strA="WelcomPython"
print(id(strA)==id(strB))
print("===========================================")

print((strA+" ")*10)

# Slicing
str="Python"
print(str[1:3])

print(str[1:-1]) # ytho -1 means remove last char
print(str[1:-2]) # ytho -2 means remove last two char


# Example 5: ord() and chr()

print(ord("A"))  # ord will return ASCII Number

print(chr(65)) # chr() will return character represented by ASCII Number


# Example6: max() mix() len()

print(max("abc")) # will return c bcoz max will return max element by ASCII
print(min("abc"))
print(len("Welcome"))

# Example7: in not in operators
s="Welcome"
print("come" in s)
print("come" not in s)


# Example8: String comparsion
# Example9: testing String
s="Python Learning"
print("==================Testing String=========================")
print(s.isalnum())
print(s.isalpha())
print("2023".isdigit())
print("2023A".isalnum())
print(s.isidentifier())
print("class".isidentifier())
print(s.islower())
print(s.isupper())
print(s.isspace())
print(" ".isspace())



# Example 10: Searching for subString

print("==================Searching for subString=========================")
print(s.endswith("thon"))
print(s.startswith("Python"))
print(s.find("ython"))
print(s.index("ython"))
print(s.find("Java"))
print(s.count("n"))

# Example 11: Converting String
print("==================Converting String=========================")
# s="Python Learning"
print(s.capitalize())
print("python LEARNING".capitalize())
print("Hello World".swapcase())
print("Hello World".replace("Hello","Sup").swapcase())


# Example 12: Reverse a String
print("==================Reversing  String=========================")
# Method 1
rev_str=""
for i in s:
    rev_str=i+rev_str
print("reversed String is: ",rev_str)


print("==================Method 2=========================")
# s="Python Learning"
# method 2
print(s[::-1]) # from rear to front each one
print(s[::-2])  # from rear to front each two
print(s[3:8])
print(s[3::8])
print(s[3::2])

print("==================Test=========================")
# print("Welcome"[0:7])
# print("Welcome"[0:-1])
# print("Welcome"[0:-2])
# print("Welcome"[0:7:2])
# print("Welcome"[0::2])
# print("Welcome"[3::-2])
s="Welcome";
print("Welcome"[-1::-1])
print("Welcome"[7:0:-1])
print("Welcome"[7:2:-1])
print("Welcome"[5:0:-1])
print("Welcome"[5:0:-2])