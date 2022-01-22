class Demo:
    def __init__(self):
        print("\nInside Constructor...")
        
    def __del__(self):
        print("\nInside Destructor...")

def main():
    print("\nInside Main...")
    
    obj = Demo()
    
    print("\nEnd Main")
        
if __name__ == "__main__":
    main()
    print("\nEnd Application... ")