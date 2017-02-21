def total_noise(building_size):
    return building_size * (building_size + 1) / 2

def noise_with_clearouts(building_size, n_clearouts):
    if n_clearouts == 0:
        return total_noise(building_size)

    n_splits = n_clearouts + 1
    remainder = building_size % n_splits
    split_size = building_size / n_splits
    return (remainder * total_noise(split_size + 1) +
            (n_splits - remainder) * total_noise(split_size))

def noise_reduction(building_size, nth_clearout):
    return (noise_with_clearouts(building_size, nth_clearout - 1) -
            noise_with_clearouts(building_size, nth_clearout))

def solve(building_sizes, total_clearouts):
    clearouts_used = [0 for _ in range(len(building_sizes))]
    for _ in range(total_clearouts):
        max_reduction = float('-inf')
        max_index = 0
        for i, size in enumerate(building_sizes):
            reduction = noise_reduction(size, clearouts_used[i] + 1)
            if reduction > max_reduction:
                max_reduction = reduction
                max_index = i
        clearouts_used[max_index] += 1

    return sum(noise_with_clearouts(building_sizes[i], clearouts_used[i])
               for i in range(len(clearouts_used)))

n_parties, n_buildings, total_clearouts = (int(x) for x in raw_input().split())
building_sizes = [0 for _ in range(n_buildings)]
for _ in range(n_parties):
    building_index = int(raw_input()) - 1
    building_sizes[building_index] += 1

print solve(building_sizes, total_clearouts)
