from input_large import seeds as seeds
from input_large import maps as maps

# print(seeds)
# print(maps)


def fast(seeds, maps):
    locations = []

    for pair in seeds:
        remain = [pair]
        result = []

        for _map in maps:
            # print(f"map: {_map}")
            while remain:
                cur = remain.pop()  # cur = x-y
                for dest, src, rng in _map:  # src-(src+rng-1) = a-b
                    # print(dest, src, rng)
                    if (
                        cur[1] < src or src + rng <= cur[0]
                    ):  # no overlap, x-y-a-b or a-b-x-y
                        continue
                    elif src <= cur[0] <= cur[1] < src + rng:  # a-x-y-b
                        offset = cur[0] - src
                        result.append((dest + offset, dest + offset + cur[1] - cur[0]))
                        break
                    elif cur[0] < src <= cur[1] < src + rng:  # x-a-y-b
                        offset = cur[1] - src
                        result.append((dest, dest + offset))
                        remain.append((cur[0], src - 1))
                        break
                    elif src <= cur[0] < src + rng <= cur[1]:  # a-x-b-y
                        offset = cur[0] - src
                        result.append((dest + offset, dest + rng - 1))
                        remain.append((src + rng, cur[1]))
                        break
                    elif cur[0] < src <= src + rng <= cur[1]:  # x-a-b-y
                        result.append((dest, dest + rng - 1))
                        remain.append((cur[0], src - 1))
                        remain.append((src + rng, cur[1]))
                        break
                else:  # didn't match any source range
                    result.append(cur)
            remain = result
            result = []
        locations.extend(remain)

    # print(locations)
    return min(i[0] for i in locations)


ans = fast(seeds, maps)
print(f"The answer is {ans}")
