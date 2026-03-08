def water_plants(plant_list):
    try:
        print("Opening watering system")
        for x in plant_list:
            if (x == "None"):
                int("abc")
            print(f"Watering {x}")
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system():
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)

    print("\nTesting with error...")
    plants = ["tomato", "lettuce", "None"]
    water_plants(plants)

    print("\nCleanup always happens, even with errors!")


test_watering_system()
