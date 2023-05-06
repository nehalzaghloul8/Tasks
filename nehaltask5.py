from binarytree import Node,build

values = [1,2,3,4,5,6,7]
root = build(values)
print(root)

choice = int(input("Inter your choice (1: Add element, 2: Delete element): "))

if choice == 1:
    value = int(input("Add value : "))
    node = Node(value)
    root.insert(node)
    print(root)
    
elif choice == 2:
    value = int(input("Delete value: "))
    node = root.search(value)
    root.delete(node)
    print(root)
    
else:
    print("wrong choice")