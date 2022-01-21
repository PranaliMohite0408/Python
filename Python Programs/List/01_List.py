data = [10,20,30,40];

print(data[-1]);                #40

print(data);                    #[10,20,30,40]

data.insert(-1,50);

print(data);                    #[10,20,30,50,40]

data.insert(len(data),50);

print(data);                    #[10,20,30,40,50]