#alien_0 = {'color': 'green', 'points': 5}

#print(alien_0['color'])
#print(alien_0['points'])

#print(alien_0)

#alien_0["cars"] = 'Polo'
#alien_0["bike"] = 'cbr'

#print(alien_0)

#Starting with an empty dict

#cars ={}

#cars["cars"] = 'Polo'
#cars["bike"] = 'cbr'

#print(cars)

#Modify values in a dict

#alien = {'bike':'cbr','cars': 'bmw'}

#print(f"this is my bike {alien['bike']}")
#print(f"this my {alien['cars']}")

#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print(f"orginal position: {alien_0['x_position']}")

#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2 
#else:
#    x_increment = 3 

#alien_0['x_position'] = alien_0['x_position'] + x_increment

#print(f"new position: {alien_0['x_position']}")


#Removing Key value :

#asset = {'car':'polo','bike':'cbr'}
#del asset['car']
#print(asset)

#favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}

#languages = favorite_languages['phil'].title()
#print(f"my fav lang {languages}")

#using get() to access the values

#Looping all key values

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

#for key, value in user_0.items(): 
#    print(f"\nKey: {key}")
#    print(f"values {value}")

for name in user_0.values():
    print(name)
    if name in user_0:
        print(f"username: {name}")