def check_temperature(temp_str: str) -> int | None:
    try:
        tmpe = int(temp_str)
        if 0 <= tmpe <= 40:
            print(f"Temperature {tmpe}°C is perfect for plants!")
            return tmpe
        elif tmpe < 0:
            print(f"Error: {tmpe}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Error: {tmpe}°C is too hot for plants (max 40°C)")
            return None
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    tmp_test = input("Testing temperature: ")
    check_temperature(tmp_test)
    tmp_test = input("Testing temperature: ")
    check_temperature(tmp_test)
    tmp_test = input("Testing temperature:")
    check_temperature(tmp_test)
    tmp_test = input("Testing temperature:")
    check_temperature(tmp_test)
    print("All tests completed - program didn't crash!")


print("=== Garden Temperature Checker ===")
test_temperature_input()
