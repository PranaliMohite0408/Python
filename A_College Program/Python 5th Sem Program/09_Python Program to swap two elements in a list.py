#Write a Python Program to swap two elements in list

mylist=[10,20,30,40]
def swap(arr,item1,item2):
    index1 = mylist.index(item1)
    index2 = mylist.index(item2)
    arr[index1],arr[index2]=arr[index2],arr[index1]
swap(mylist,10,30)
print(mylist)
