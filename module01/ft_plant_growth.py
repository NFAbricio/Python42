class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age_days = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age_days} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self._age_days += 1

if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    plant.show()
    
    start_height = plant.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()
        
    growth = round(plant.height - start_height, 1)
    print(f"Growth this week: {growth}cm")