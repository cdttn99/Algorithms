def feedDog(hunger_levels, biscuit_sizes):
    satisfied_dogs = 0
    hunger_levels.sort()
    biscuit_sizes.sort()

    for i in range(len(hunger_levels)):
        for j in range(len(biscuit_sizes)):
            if biscuit_sizes[j] >= hunger_levels[i]:
                satisfied_dogs += 1
                biscuit_sizes[j] = -1  # Mark this biscuit as used
                break
    return satisfied_dogs

print(feedDog([2,1],[1,3,2]))