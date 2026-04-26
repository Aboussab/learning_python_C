def ft_plant_age():
    print("Enter plant age in days:", end=" ")
    x = int(input())
    if (x < 60):
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
