def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature ===")
    
    temp1 = '25'
    print(f"Input data is '{temp1}'")
    try:
        val = input_temperature(temp1)
        print(f"Temperature is now {val}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
        
    temp2 = 'abc'
    print(f"Input data is '{temp2}'")
    try:
        val = input_temperature(temp2)
        print(f"Temperature is now {val}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
        
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()