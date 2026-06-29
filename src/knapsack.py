from dataclasses import dataclass

from src.priority import subject_priority
from src.subject import Subject


@dataclass(frozen=True)
class StudyPlanResult:
    max_score: int
    time_used: int
    selected_subjects: list[Subject]
    rejected_subjects: list[Subject]
    dp_table: list[list[int]]


def plan_studies(subjects: list[Subject], available_time: int) -> StudyPlanResult:
    if available_time < 0:
        raise ValueError("Available time cannot be negative.")

    total_subjects = len(subjects)
    dp_table = [[0 for _ in range(available_time + 1)] for _ in range(total_subjects + 1)]

    for item_index in range(1, total_subjects + 1):
        subject = subjects[item_index - 1]
        subject_value = subject_priority(subject)

        for time_limit in range(available_time + 1):
            best_without_subject = dp_table[item_index - 1][time_limit]

            if subject.time > time_limit:
                dp_table[item_index][time_limit] = best_without_subject
                continue

            best_with_subject = (
                subject_value + dp_table[item_index - 1][time_limit - subject.time]
            )
            dp_table[item_index][time_limit] = max(
                best_without_subject,
                best_with_subject,
            )

    selected_subjects = _reconstruct_selected_subjects(subjects, available_time, dp_table)
    selected_set = set(selected_subjects)
    rejected_subjects = [subject for subject in subjects if subject not in selected_set]
    time_used = sum(subject.time for subject in selected_subjects)

    return StudyPlanResult(
        max_score=dp_table[total_subjects][available_time],
        time_used=time_used,
        selected_subjects=selected_subjects,
        rejected_subjects=rejected_subjects,
        dp_table=dp_table,
    )


def _reconstruct_selected_subjects(
    subjects: list[Subject],
    available_time: int,
    dp_table: list[list[int]],
) -> list[Subject]:
    selected_subjects: list[Subject] = []
    remaining_time = available_time

    for item_index in range(len(subjects), 0, -1):
        current_score = dp_table[item_index][remaining_time]
        previous_score = dp_table[item_index - 1][remaining_time]

        if current_score == previous_score:
            continue

        subject = subjects[item_index - 1]
        selected_subjects.append(subject)
        remaining_time -= subject.time

    selected_subjects.reverse()
    return selected_subjects
