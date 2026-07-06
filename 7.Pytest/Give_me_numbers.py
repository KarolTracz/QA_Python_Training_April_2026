def test_me(start:int = 333, end:int = 7553):
    results: list[int] = []
    for i in range(start, end+1):
        if i % 5 == 0:
            continue
        else:
            if i % 7 == 0 and i % 13 == 0:
                results.append(i)
    return results

print(test_me())
