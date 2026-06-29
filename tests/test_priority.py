import unittest

from src.priority import calculate_priority, subject_priority
from src.subject import Subject


class PriorityTest(unittest.TestCase):
    def test_calculates_priority_from_importance_difficulty_and_mastery(self):
        self.assertEqual(calculate_priority(9, 8, 3), 14)

    def test_calculates_subject_priority(self):
        subject = Subject(
            name="Knapsack",
            time=3,
            importance=10,
            difficulty=8,
            mastery=4,
        )

        self.assertEqual(subject_priority(subject), 14)


if __name__ == "__main__":
    unittest.main()
