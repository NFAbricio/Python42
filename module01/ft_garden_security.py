class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative\nHeight update rejected")
        else:
            self._height = height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative\nAge update rejected")
        else:
            self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    p = Plant("Rose", 15.0, 10)
    print(f"Plant created: {p._name}: {p.get_height():.1f}cm, {p.get_age()} days old")
    
    print("Height updated: -25cm")
    p.set_height(-25)
    print("Age updated: -30 days")
    p.set_age(-30)
    
    print("Current state: ", end="")
    p.show()