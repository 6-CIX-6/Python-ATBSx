# fantasyGameInventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print('   ' + str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total) + '\n')


def addToInventory(inventory, addedItems):
    print('You looted:' + str(addedItems) + '\n')
    # for i in range(len(addedItems)):
    #     j = addedItems[i]
    #     if j in inventory:
    #         inventory[j] += 1
    #     else:
    #         inventory.setdefault(j, 1)
    # # print(tempInv)  # test conversion of list to dict
    # return inventory

    # Mel's way... much faster
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

displayInventory(inv)
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

# displayInventory(stuff)