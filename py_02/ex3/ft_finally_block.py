def water_plants(plant_list):
    """here we have a fct that  clean up after itself,
    even if an error happens its open the watrings syst
    and waters each plant if an error happned its close the systeme"""
    try:
        print("Opening watering system")
        for x in plant_list:
            if not x:
                int("abc")
            print(f"Watering {x}")
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system():
    """this is a fct that :
    • Tests normal operation (no errors)
    • Tests error scenario (None in plant list)
    • Shows cleanup happens in both cases
    """
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)

    print("\nTesting with error...")
    plants = ["tomato", "lettuce", ""]
    water_plants(plants)

    print("\nCleanup always happens, even with errors!")


test_watering_system()
