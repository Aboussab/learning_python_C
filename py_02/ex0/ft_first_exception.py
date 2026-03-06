def check_temperature(temp_str: str) -> None:
    try:
        tmpe = int(temp_str)
        if tmpe >= 0 & tmpe <= 40:
            print(f"Temperature {tmpe}°C is perfect for plants!")
        else:
            print(f"Error: {tmpe}°C is too hot for plants (max 40°C)")
    except tmpe:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    tmp_test = input("zuilles entre ")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("50")


test_temperature_input()