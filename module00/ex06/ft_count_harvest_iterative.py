def ft_count_harvest_iterative():
    days_harvests = int(input("Days until harvest: "))
    for i in range(1, days_harvests + 1):
        print(f"Day {i}")
    print("Harvest time!")