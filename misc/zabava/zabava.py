
def total_noise(building_size):
    """The sum of the noise of all parties held in this building.
    args:
      building_size: the total number of students who will move into this
                     building
    """
    return building_size * (building_size + 1) / 2


def noise_with_clearouts(building_size, n_clearouts):
    """The sum of the noise from the parties in this building, given that
    management clears it out n_clearouts times."""
    if n_clearouts == 0:
        return total_noise(building_size)

    # clearing a building out after party i is like 'splitting' the building
    # into two buildings, one with size i and one with size n-i.
    # the optimal way to do this is to 'split' the building into equal sized
    # sections
    n_splits = n_clearouts + 1
    remainder = building_size % n_splits
    split_size = building_size / n_splits
    return (remainder * total_noise(split_size + 1) +
            (n_splits - remainder) * total_noise(split_size))


def noise_reduction(building_size, nth_clearout):
    """The reduction in noise achieved by clearing this building out n times,
    compared to clearing it out n-1 times."""
    return (noise_with_clearouts(building_size, nth_clearout - 1) -
            noise_with_clearouts(building_size, nth_clearout))


def solve(building_sizes, total_clearouts):
    """Given the sizes of each building, and the total number of times you can
    clear a building out, find the minimum possible sum of the noise of all
    parties held in all buildings."""
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
