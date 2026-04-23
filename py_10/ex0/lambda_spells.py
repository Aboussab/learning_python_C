def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {"max_power": max(mages, key=lambda x: x["power"])["power"],
            "min_power": min(mages, key=lambda x: x["power"])["power"],
            "avg_power":
            round(sum(list(map(lambda x: x["power"], mages))) / len(mages), 2)
            }


def main() -> None:
    artifacts = [{'name': 'Light Prism', 'power': 94, 'type': 'armor'},
                 {'name': 'Crystal Orb', 'power': 110, 'type': 'armor'},
                 {'name': 'Wind Cloak', 'power': 67, 'type': 'focus'},
                 {'name': 'Ice Wand', 'power': 81, 'type': 'accessory'}
                 ]
    mages = [{'name': 'Storm', 'power': 82, 'element': 'fire'},
             {'name': 'River', 'power': 58, 'element': 'ice'},
             {'name': 'Sage', 'power': 52, 'element': 'light'},
             {'name': 'Luna', 'power': 92, 'element': 'fire'},
             {'name': 'River', 'power': 82, 'element': 'water'}
             ]
    spells = ['heal', 'tsunami', 'darkness', 'shield']
    try:
        print("Testing artifact sorter...")
        sorted_artifacts = artifact_sorter(artifacts)
        print(f"{sorted_artifacts[0]['name']} \
({sorted_artifacts[0]['power']} power) comes before \
{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")
        print("\nTesting power filter...")
        print(f"those are biger then 90: {power_filter(artifacts, 90)}")
        print(f"those are biger then 60: {power_filter(artifacts, 60)}")
        print("\nTesting mage stats...")
        print(mage_stats(mages))
        print("\nTesting spell transformer...")
        transformed = spell_transformer(spells)
        print(" ".join(transformed))
    except Exception:
        print("somthings went wrong!!!!")


if __name__ == "__main__":
    main()
