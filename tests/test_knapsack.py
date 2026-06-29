import unittest

from src.knapsack import plan_studies
from src.subject import Subject


class KnapsackTest(unittest.TestCase):
    def test_selects_optimal_subjects_within_available_time(self):
        subjects = [
            Subject("A", time=2, importance=8, difficulty=5, mastery=3),
            Subject("B", time=3, importance=10, difficulty=7, mastery=3),
            Subject("C", time=4, importance=10, difficulty=8, mastery=2),
        ]

        result = plan_studies(subjects, available_time=5)

        self.assertEqual(result.max_score, 24)
        self.assertEqual(result.time_used, 5)
        self.assertEqual([subject.name for subject in result.selected_subjects], ["A", "B"])
        self.assertEqual([subject.name for subject in result.rejected_subjects], ["C"])

    def test_returns_empty_plan_when_no_time_is_available(self):
        subjects = [
            Subject("Knapsack", time=2, importance=10, difficulty=8, mastery=4),
        ]

        result = plan_studies(subjects, available_time=0)

        self.assertEqual(result.max_score, 0)
        self.assertEqual(result.time_used, 0)
        self.assertEqual(result.selected_subjects, [])
        self.assertEqual(result.rejected_subjects, subjects)

    def test_exposes_dynamic_programming_table(self):
        subjects = [
            Subject("A", time=2, importance=8, difficulty=5, mastery=3),
            Subject("B", time=3, importance=10, difficulty=7, mastery=3),
        ]

        result = plan_studies(subjects, available_time=5)

        self.assertEqual(len(result.dp_table), 3)
        self.assertEqual(len(result.dp_table[0]), 6)
        self.assertEqual(result.dp_table[-1][-1], result.max_score)


if __name__ == "__main__":
    unittest.main()
