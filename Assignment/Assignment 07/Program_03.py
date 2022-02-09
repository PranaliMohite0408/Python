"""
Write a recursive program which display below pattern.
Input : 5
Output : 5 4 3 2 1
"""
def Pattern(i):
    if(i >= 1):
       print(i)
       i = i-1
       Pattern(i)

def main():
    Pattern(5)

if __name__ == "__main__":
    main()