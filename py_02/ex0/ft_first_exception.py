def check_temperature(temp_str):
    """
    Validates a temperature reading for agricultural safety.

    Attempts to convert the input string to an integer and checks if it fails
    within the safe range for plants (0°C to 40°C). Handles invalid numbers.

    Args:
        temp_str : The temperature input to validate.

    Returns:
        int: The valid temperature if it is between 0 and 40.
        None: If the input is not a number or is out of the safe range.
    """
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
    """this fct take an input and test our check_temperature fct"""
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
