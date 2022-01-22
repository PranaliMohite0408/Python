#Python Program to check if a substring is present in given string

def check(string,sub_str):
    if(string.find(sub_str)==-1):
        print("No")
    else:
        print("Yes")
        
#Drive Code
string = "Geeks for Geeks"
sub_str = "Geek"
check(string,sub_str)
