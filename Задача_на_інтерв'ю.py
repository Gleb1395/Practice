def deep_lake(hight: list) -> list:
    lakes = []
    while len(hight) > 0:
        if len(hight) == 1:
            break
        hight.insert(0, 0)
        hight_copy = hight[:]
        lake = []
        for index, value in enumerate(hight[1:], start=1):
            if hight_copy[index - 1] < value > hight_copy[index + 1]:
                for i in range(index, len(hight_copy)):
                    if hight_copy[i] <= value:
                        lake.append(hight_copy[i])
                    elif hight_copy[i] >= value:
                        lakes.append(lake)
                        lake = []
                        hight = hight[i:]
                        break
                if lake:
                    if lake[0] != lake[-1]:
                        lake = []
                        hight = hight[i:]
                        break
                else:
                    break
    min_num = min(min(sublist) for sublist in lakes)
    for sublist in lakes:
        if min_num in sublist:
            return sublist[0]

print(deep_lake([
    1, 2, 5, 6, 1, 2,
    2, 3, 1, 1, 5, 6,
    7, 5, 5,0, 7, 8, 2,
]))
