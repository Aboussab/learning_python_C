def ft_count_harvest_iterative():
    i = 1
    x = int(input("Days until harvest: "))

    for x in range(1, x + 1):
        print("Day", i)
        i += 1
    print("Harvest time!")
