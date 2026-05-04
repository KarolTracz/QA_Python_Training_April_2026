from typing import List

bounties = [
    {'target': 'Grogu',          'status': 'active',    'reward': 25000},
    {'target': 'Boba Fett',      'status': 'claimed',   'reward': 75000},
    {'target': 'Cara Dune',      'status': 'active',    'reward': 8000},
    {'target': 'Moff Gideon',    'status': 'active',    'reward': 50000},
    {'target': 'Dr. Pershing',   'status': 'completed', 'reward': 12000},
]


def hot_bounties(bounties: List[dict], min_reward: int) -> List[dict]:
    return_list = []
    for i in bounties:
        if i['status'] == 'active' and i['reward'] >= min_reward:
            return_list.append(i)

    return sorted(return_list, key=lambda x:x['reward'], reverse=True)

print(hot_bounties([{"target":"Grogu","status":"active","reward":25000},{"target":"Boba Fett","status":"claimed","reward":75000},{"target":"Moff Gideon","status":"active","reward":50000}], 10000)[0]["target"])

print(hot_bounties([
    {"target":"Grogu","status":"active","reward":25000},
    {"target":"Boba Fett","status":"claimed","reward":75000},
    {"target":"Moff Gideon","status":"active","reward":50000}],
    10000))
# [{'target': 'Moff Gideon', ...reward: 50000},
#  {'target': 'Grogu', ...reward: 25000}]