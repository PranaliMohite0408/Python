#Write a python Program to find out ways to remove i'th character form string in python

test_str = "GeeksforGeeks"
print("The Original Stirng is :" + test_str)

new_str = ""

for i in range(len(test_str)):
    if i !=2:
        new_str = new_str + test_str[i]
print("The String After Removal of i'th character:" + new_str)

        
