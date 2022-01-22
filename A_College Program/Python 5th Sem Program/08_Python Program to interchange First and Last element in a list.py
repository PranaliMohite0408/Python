#Program to Interchange First and last element in a list
#Using temporary variable
mylist=[5,6,7,9,10]
size=len(mylist)
temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp
print("List after swapping:",mylist)
