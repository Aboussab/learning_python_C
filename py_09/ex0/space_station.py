from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200, default=None)


def main() -> None:
    try:
        print("-" * 50)
        print("Valid station created:")
        valid_space = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=None
        )
        print(f"ID: {valid_space.station_id}")
        print(f"Name: {valid_space.name}")
        print(f"Crew: {valid_space.crew_size} people")
        print(f"Power: {valid_space.power_level}%")
        print(f"Oxygen: {valid_space.oxygen_level}%")
        status = "Operational" if valid_space.is_operational else "Not\
 Operational"
        print(f"Status: {status}")
        print()
        print("-" * 50)
        print("Expected validation error:")

        invalid_space = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=22,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=None
        )
        print(f"ID: {invalid_space.station_id}")
        print(f"Name: {invalid_space.name}")
        print(f"Crew: {invalid_space.crew_size} people")
        print(f"Power: {invalid_space.power_level}%")
        print(f"Oxygen: {invalid_space.oxygen_level}%")
        instatus = "Operational" if invalid_space.is_operational else "Not\
Operational"
        print(f"Status: {instatus}")
    except ValidationError as e:
        print(e.errors()[0]['msg'])


main()
