def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name is None:
            raise Exception("Error: Plant name cannot be empty!")
        if water_level > 10:
            raise Exception("Error: Water level 15 is too high (max 10)")
        elif water_level <= 0:
            raise Exception("Error: Water level 15 is too low (min 1)")
        if 2 > sunlight_hours:
            raise Exception("Error: Sunlight hours 0 is too low (min 2")
        elif sunlight_hours > 12:
            raise Exception("Error: Sunlight hours 0 is too high (max 12")
        print(f"Plant '{plant_name}' is healthy!")
    except Exception as e:
        print(e)


def test_plant_checks():
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
