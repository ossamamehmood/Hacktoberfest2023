"""
 Write a menu driven program to perform
various list operations, such as:
• Append an element
• Insert an element
• Append a list to the given list
• Modify an existing element
• Delete an existing element from its position
• Delete an existing element with a given value
• Sort the list in ascending order
• Sort the list in descending order
• Display the list."""
l=[]
print("List functions to manage a list of number's ")
print("1. append an element\n2. insert an element\n3. append a list to a given list\n4. modify an existing element\n5. Delete an existing element from its position\n6. Delete an existing element with a given value\n7. Sort the list in ascending order\n8. Sort the list in decending order\n9. display the list\n10.exit")
while True:
  ch=int(input("enter your choice"))
  if ch==1:
    b=int(input("enter the number"))
    l.append(b)
    print(l)
    b=None
  elif ch==2:
    b=int(input("enter the number"))
    c=int(input("enter the position to insert",b))
    l.insert(c,b)
    print(l)
    b=c=None
  elif ch==3:
    a=[]
    n=int(input("enter the number of elements u want to enter"))
    for i in range(n):
      b=int(input("enter the number"))
      a.append(b)
    l.append(a)
    print(l)
    a=n=b=None
  elif ch==4:
    ind=[x for x in range(len(l))]
    for i in range(len(l)):
      a=ind[i]
      b=l[i]
      print("|{:^5}|{:^5}|".format(int(a),int(b)))
    a=int(input("enter the index of the element u want to modify"))
    b=int(input("new value to be inserted to the index",a))
    l.pop(a)
    l.insert(b,a)
    print(l)
    a=x=b=i=None
  elif ch==5:
    ind=[x for x in range(len(l))]
    for i in range(len(l)):
      a=ind[i]
      b=l[i]
      print("|{:^5}|{:^5}|".format(int(a),int(b)))
    a=int(input("enter the index of the element u want to delete"))
    l.pop(a)
    print(l)
    a=b=i=None
  elif ch==6:
    a=int(input("enter the value of the element u want to delete"))
    l.remove(a)
    print(l)
    a=None
  elif ch==7:
    l.sort()
    print(l)
  elif ch==8:
    l.sort(reverse=True)
  elif ch==9:
    print(l)
    print("list with index")
    print("---------------")
    ind=[x for x in range(len(l))]
    for i in range(len(l)):
      a=ind[i]
      b=l[i]
      print("|{:^5}|{:^5}|".format(int(a),int(b)))
  else:
    break
