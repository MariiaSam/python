
from item import Item

item = Item('MyItem', 750)

print(item.info())

item.name = "OtherName"

print(item.name)

print(item.info())
print(item.__dict__)