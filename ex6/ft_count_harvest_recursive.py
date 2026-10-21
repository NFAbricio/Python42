def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive(count, total):
        if count > total:
            print("Harvest time!")
            return
        print(f"Day {count}")
        recursive(count + 1, total)

    recursive(1, days)
