from inventory import displayInventory


def addToInventory(inventory, addItems):
	for item in addItems:
		if item in inv.keys():
			inv[item] += 1
		else:
			inv.setdefault(item, 0)
			inv[item] += 1
	return inv
	
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(inv)
displayInventory(inv)
