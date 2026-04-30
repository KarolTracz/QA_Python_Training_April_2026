from typing import Any, List

def loot_all(dungeon: Any) -> List[str]:
    returned_list: list = []

    for i in dungeon:
        if isinstance(i, str):
            returned_list.append(i)
        if isinstance(i, list):
            temp_list: list = loot_all(i)
            for j in temp_list:
                returned_list.append(j)
        else:
            pass

    return returned_list

print(loot_all(['Torch', ['Gold Coin', 'Rusty Sword']])) # ['Torch', 'Gold Coin', 'Rusty Sword']
print(loot_all([['Dragon Egg', ['Legendary Armor', ['Estus Flask']]], 'Bonfire Ash']))  # ['Dragon Egg', 'Legendary Armor', 'Estus Flask', 'Bonfire Ash']
print(loot_all([]))  # []
print(loot_all(['Tarnished Medal']))  # ['Tarnished Medal']
