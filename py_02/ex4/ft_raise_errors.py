def check_plant_health(plant_name, water_level, sunlight_hours):
    """this is a fct that :
    Validates plant name (not empty)
    • Validates water level (1-10 range)
    • Validates sunlight hours (2-12 range)
    • Raises ValueError with descriptive messages for invalid inputs
    • Returns success message for valid inputs
    """
    try:
        if not plant_name:
            raise ValueError("Error: Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError("Error: Water level 15 is too high (max 10)")
        elif water_level <= 0:
            raise ValueError("Error: Water level 15 is too low (min 1)")
        if 2 > sunlight_hours:
            raise ValueError("Error: Sunlight hours 0 is too low (min 2")
        elif sunlight_hours > 12:
            raise ValueError("Error: Sunlight hours 0 is too high (max 12")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(e)


def test_plant_checks():
    """this is a fct that :
    • Tests good values (should succeed)
    • Tests bad plant name, water level, and sunlight hours
    • Catches and handles each error appropriately"""
    print("\nTesting good values...")
    check_plant_health("tomato", 5, 6)

    print("\nTesting empty plant name...")
    check_plant_health(None, 5, 6)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 6)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 1)

    print("\nAll error raising tests completed!")


print("=== Garden Plant Health Checker ===")
test_plant_checks()
