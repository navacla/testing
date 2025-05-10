# This program prints Hello, world!

greeting : str = 'Hello, world!' 

print(greeting)

pie_list = ['Banana', 'Blueberry', 'Peacan', 'Orange']

for name in pie_list:
    if len(name) < 6:
        print(name)
else:
        print("Name too long")
