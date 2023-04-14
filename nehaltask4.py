list=[3,2,9,11,7]
m=len(list)
dict={}
def hash_func(l,m):
    for v in list:  
        f=v%m
        dict[v]=f 
    return dict

hash_func(list,m)
def adding():
    key=int(input("Inter the key:"))
    value=int(input("Inter the value:"))
    dict[key]=value
    return dict
def updating():    
    key=int(input('Inter the key:'))
    dict[key]=int(input("Inter the new value:"))
    return dict
def deleting():
    key=int(input("Inter the key:"))
    del dict[key]
    return dict
def searching():
    key=int(input("Inter the key:"))
    return dict[key]
def printing():
    for key in dict:
        print(key,':',dict[key])

print("choose 1 for hash table\nchoose 2 for adding \nchoose 3 to update\nchoose 4 to delete \nchoose 5 to search \nchoose 6 to print")
choice=int(input("Inter your choice:"))
if choice==1:
    print(hash_func(list,m))
elif choice==2:
    print(adding())
elif choice==3:
    print(updating())
elif choice==4:
    print(deleting())
elif choice==5:
    print(searching())
elif choice==6:
    printing()
else:
    print("invalid choice")