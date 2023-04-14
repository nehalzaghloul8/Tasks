list=[1,2,3,4,5,6]
m=len(list)
dict={}
def hash_function(l,m):
    for v in list:  
        f=v%m
        dict[v]=f 
    return dict
print(hash_function(list,m))