#List
#Sequential
#Indexed
#Data is mutable
#List is mutable
#Allow duplicates
#Heterogeneous

Data = [11,21,51,101,111];

print("Data using while loop");
i = 0;

while(i < len(Data)):
    print(Data[i]);
    i = i + 1;
    
print("Data using for loop");

for i in range(len(Data)):
    print(Data[i]);