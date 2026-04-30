from typing import List
from collections import Counter

def monster_sightings(log: str, threshold: int) -> List[str]:
    input_list: list = [i.lower() for i in log.split()]
    counter = Counter(input_list)
    return sorted([k  for k, v in counter.items() if v > threshold])

print(monster_sightings("Drowner drowner Nekker drowner", 1)) # ['drowner']
print(monster_sightings("Werewolf Werewolf Ghoul werewolf", 2)) # ['werewolf']
print(monster_sightings("Striga striga STRIGA kikimora", 3))  # []
print(monster_sightings("", 0))  # [])