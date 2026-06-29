from src.subject import Subject


def calculate_priority(importance: int, difficulty: int, mastery: int) -> int:
    return importance + difficulty - mastery


def subject_priority(subject: Subject) -> int:
    return calculate_priority(
        importance=subject.importance,
        difficulty=subject.difficulty,
        mastery=subject.mastery,
    )
