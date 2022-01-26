data = {"A":10, "B":20, "C":30, "C":40, 50:"D"};

print("Data is :",data);

print("Type is :",type(data));

print("Length is :",len(data));

#print(data[0]); #We can't access with index

print(data["A"]);

for keys in data:
    print(keys,data[keys]);