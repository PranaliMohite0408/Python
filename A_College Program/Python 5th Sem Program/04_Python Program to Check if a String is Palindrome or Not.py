#Write a Program to Check if a String is Palindrome or Not

def isPalindrome(s):
    #Run Loop from 0 to len/2
    for i in range(0,int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return false
        return True
#main Function
s = "abcda"
ans = isPalindrome(s)
if(ans):
    print("Yes")
else:
    print("No")
