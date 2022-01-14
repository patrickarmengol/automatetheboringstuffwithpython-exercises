
sample_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    num_items = 0
    print('inventory:')
    for item, count in inventory.items():
        print(f'{count} {item}')
        num_items += count
    print(f'total number of items: {num_items}')

def pickup_loot(loot, inventory):
    print('picking up:')
    for item in loot:
        print(item)
        inventory.setdefault(item, 0)
        inventory[item] += 1


display_inventory(sample_inventory)
pickup_loot(dragon_loot, sample_inventory)
display_inventory(sample_inventory)
