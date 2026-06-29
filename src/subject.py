from dataclasses import dataclass


@dataclass(frozen=True)
class Subject:
    name: str
    time: int
    importance: int
    difficulty: int
    mastery: int

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Subject name cannot be empty.")

        if self.time <= 0:
            raise ValueError("Study time must be greater than zero.")

        for field_name, value in (
            ("importance", self.importance),
            ("difficulty", self.difficulty),
            ("mastery", self.mastery),
        ):
            if not 0 <= value <= 10:
                raise ValueError(f"{field_name} must be between 0 and 10.")
