#list
# we use ([])
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles)
#print(bicycles[0]) ----------------> index

#message = f"hey this is my {bicycles[0].title()}"
#print(message)

#changing Adding Removing

#modify element in list 
#bicycles[1]='honda' 
#print(bicycles)

#adding element in list

#bicycles.append('honda')
#bicycles.append('cbr')
#print(bicycles)

#inserting elements into a list

#bicycles.insert(2, 'cbr') ------> inserting using index 
#print(bicycles)

#removing element of the list

#del bicycles[0]
#print(bicycles)

#removing a list using pop() method

#poped_motorcycles = bicycles.pop(0)
#print(poped_motorcycles )

#print(f"hey this is my {poped_motorcycles}")

#Removing Iteam by value
#bicycles.remove('trek')
#print(bicycles)


#sorting the list sort() and also reverce order

#bicycles.sort()
#rint(bicycles)

#bicycles.sort(reverse=True)
#print(bicycles)

#sorted list temp with the function sorted()
#print(sorted(bicycles))

#printing list reverce order

#bicycles.reverse()
#print(bicycles)

print(len(bicycles))