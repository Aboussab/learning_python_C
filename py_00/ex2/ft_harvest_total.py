def ft_harvest_total():
    i = 1
    sum = 0
    while i < 4:
        print("Day", i, "harvest:", end=" ")
        sum += int(input())
        i += 1
    print("Total harvest:", sum)
