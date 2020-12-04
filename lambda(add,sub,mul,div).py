#using lambda(add,sub,mul,div)
v=lambda a:a*a
print(v(3))
v=lambda a:a+a
print(v(3))
v=lambda a:a-a
print(v(3))
v=lambda a:a/a
print(v(3))
#using two (x,y)=(add,sub,mul,div)
z=lambda x,y:x-y
print(z(6,1))
z=lambda x,y:x+y
print(z(6,1))
z=lambda x,y:x*y
print(z(6,1))
z=lambda x,y:x/y
print(z(6,1))
#using (x,y,z)=(add,sub,mul,div)
x=lambda x,y,z:x+y-z
print(x(31,1,5))
#even num using [filter]
l=[1,3,4,5,6,3]
print(list(filter(lambda x:x%2==0,l)))
#odd num using [filter]
l=[1,3,4,5,6,3]
print(list(filter(lambda x:x%2==1,l)))
#mapping [add,sub,multiply,division]
l=[11,33,44,55,66,77,88,99]
print(list(map(lambda x:x+2,l)))
l=[11,33,44,55,66,77,88,99]
print(list(map(lambda x:x-2,l)))
l=[11,33,44,55,66,77,88,99]
print(list(map(lambda x:x*2,l)))
l=[11,33,44,55,66,77,88,99]
print(list(map(lambda x:x/2,l)))