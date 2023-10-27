my={
    3:1,
    1:3,
    2:4
}
for s in my.values():
    s1=s
    break
print("The minimum number is:",end="")
for d in my.values():
    if(d<=s1):
        s1=d
print(s1)
print("The maximum number is:",end="")
for d in my.values():
    if(d>s1):
        s1=d
print(s1)
        
