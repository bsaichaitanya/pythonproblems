def addToInventory(inventory, addedItems):
    # your code goes here
    for x in addedItems:
    	inventory.setdefault(x,0)
    	inventory[x] = inventory[x] + 1
    return inventory
def displayInventory(inv):
	for k,v in inv.items():
		print(k,v)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

#print(inv)