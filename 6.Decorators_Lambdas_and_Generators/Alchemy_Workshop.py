from typing import Iterator, Optional
import types, inspect # Please keep this for tests

def distill(ingredients) -> Iterator[str]:
    for i in ingredients:
        if i is None:
            continue
        else:
            yield i

print(list(distill(['Nightshade', None, 'Eye of Newt', None, 'Dragon Scale'])))