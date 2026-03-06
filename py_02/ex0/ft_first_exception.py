def check_temperature(temp_str: str) -> None:
    try:
        tmpe = int(temp_str)
        if 0 <= tmpe <= 40:
            print(f"Temperature {tmpe}°C is perfect for plants!")
        elif tmpe < 0:
            print(f"Error: {tmpe}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {tmpe}°C is too hot for plants (max 40°C)")
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    tmp_test = input("Testing temperature: ")
    check_temperature(tmp_test)
    tmp_test = input("Testing temperature: ")
    check_temperature(tmp_test)
    tmp_test = input("Testing temperature:")
    check_temperature(tmp_test)
    tmp_test = input("Testing temperature:")
    check_temperature(tmp_test)
    print("All tests completed - program didn't crash!")


test_temperature_input()
