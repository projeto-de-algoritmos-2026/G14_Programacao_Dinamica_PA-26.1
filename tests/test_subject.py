import unittest

from src.subject import Subject


class SubjectTest(unittest.TestCase):

    def test_creates_valid_subject(self):
        subject = Subject(
            "PO",
            3,
            10,
            8,
            4,
        )

        self.assertEqual(subject.name, "PO")
        self.assertEqual(subject.time, 3)

    def test_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            Subject("", 2, 8, 5, 3)

    def test_negative_time_raises_error(self):
        with self.assertRaises(ValueError):
            Subject("PO", 0, 8, 5, 3)

    def test_invalid_importance(self):
        with self.assertRaises(ValueError):
            Subject("PO", 2, 15, 5, 3)

    def test_invalid_difficulty(self):
        with self.assertRaises(ValueError):
            Subject("PO", 2, 8, 12, 3)

    def test_invalid_mastery(self):
        with self.assertRaises(ValueError):
            Subject("PO", 2, 8, 5, 11)


if __name__ == "__main__":
    unittest.main()