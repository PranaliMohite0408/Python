#List
#Sequential
#Indexed
#Data is mutable
#List is mutable
#Allow duplicates
#Heterogeneous


Data = [11,21,51,101,3.14];

print("Datatype is",type(Data));                #list
print("Length of list is",len(Data));           #4
print("Actual Data is",Data);                   #[11,21,51,101]


print("Data from 0th index :",Data[0]);         #11
print("Data from 3rd index :",Data[3]);         #101


Data[0] = 12;
print("New Data is",Data[0]);                   #12


Data.append(111);
print(Data);                                    #[12,21,51,101,111]


Data.insert(2,51);
print(Data);                                    #[12,21,50,51,101,111]


