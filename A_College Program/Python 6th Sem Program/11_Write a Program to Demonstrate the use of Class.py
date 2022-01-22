class Person:
    "This is a Person class"
    name = 'Pranali'

    def greet(self):
        print("Hello",self.name)

#object instantiation
p= Person()
#name as output
print("Output from Variable :")
print(p.name)

#Output From Function
print("\nOutput From Function :")
p.greet()
