len=int(input("Enter the length of array: "))
list=[]
for i in range(len):
  a=int(input("Enter element:"))
  list.append(a)
print(list)
if len<4:
  print(f"Only {len} elements")
elif len==4:
  mul=1
  for i in list:
    a=list[i]
    mul=a*mul
else:
  list.sort(reverse=True)
  mul=1
  for i in range(0,4):
    a=list[i]
    mul=a*mul
print(f"The list has {len} elements.The maximal product of quadruplet is {mul}")