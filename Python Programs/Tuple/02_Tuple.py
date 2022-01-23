data = (10,20,30,40);

print("Original data :",data);

data = list(data);

data.append(50);

data = tuple(data);

print("Updated data :",data);