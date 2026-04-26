from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def custom_validation(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with AC")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("physical contact must be verified")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("strong signal must include a received message")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 30)
    alien = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        duration_minutes=45,
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        witness_count=5,
        signal_strength=8.5,
        message_received="Greetings from Zeta Reticuli"
    )
    print("Valid contact report:")

    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type}")
    print(f"Location: {alien.location}")
    print(f"Signal: {alien.signal_strength}/10")
    print(f"Duration: {alien.duration_minutes} minutes")
    print(f"Witnesses: {alien.witness_count}")
    print(f"Message: '{alien.message_received}'")
    print()
    print("=" * 30)
    print("Expected validation error:")
    try:
        in_alien = AlienContact(
            contact_id="AC_2024_001",
            duration_minutes=45,
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            witness_count=2,
            signal_strength=8.5,
            message_received="Greetings from Zeta Reticuli"
        )

        print(f"ID: {in_alien.contact_id}")
        print(f"Type: {in_alien.contact_type}")
        print(f"Location: {in_alien.location}")
        print(f"Signal: {in_alien.signal_strength}/10")
        print(f"Duration: {in_alien.duration_minutes} minutes")
        print(f"Witnesses: {in_alien.witness_count}")
        print(f"Message: '{in_alien.message_received}'")
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
