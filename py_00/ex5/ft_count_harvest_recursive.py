def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))

    def repeat(i):
        if (i == x + 1):
            return
        print("Day", i)
        repeat(i + 1)
    repeat(1)
    print("Harvest time!")
