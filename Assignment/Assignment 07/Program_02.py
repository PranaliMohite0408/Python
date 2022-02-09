"""
Write a recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5
"""
def Pattern(i):
    if(i<6):
        print(i)
        i = i+1
        Pattern(i)

def main():
    Pattern(1)

if __name__ == "__main__":
    main()