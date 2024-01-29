from input_small import seeds
from input_small import maps

print(seeds)
print(maps)


def slow(seeds, maps):
    locations = []
    count = 0
    for seed_range in seeds:
        for curr in range(seed_range[0], seed_range[0] + seed_range[1], 1):
            start = curr
            for _map in maps:
                for dest, src, rng in _map:
                    count += 1
                    # print(count)
                    if src <= curr < src + rng:
                        idx = curr - src
                        curr = dest + idx
                        break
            locations.append(curr)
            print(f"seed {start} => location {curr}")
    return min(locations)


ans = slow(seeds, maps)
print(f"The answer is: {ans}")
