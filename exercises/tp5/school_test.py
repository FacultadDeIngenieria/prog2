import unittest

from school import (Student, Course)

course1 = Course("CS101", "Introduction to Programming")
course2 = Course("SR101", "School of Rock")

student1 = Student(1023, "Jack Black")
student2 = Student(2011, "Robin Williams")
student3 = Student(4321, "Steve Carell")


class SchoolTest(unittest.TestCase):

    def test_create_course(self):
        self.assertEqual("Introduction to Programming", course1.description)
        self.assertEqual("School of Rock", course2.description)

    def test_create_student(self):
        self.assertEqual("Jack Black", student1.name)
        self.assertEqual("Robin Williams", student2.name)

    def test_str(self):
        self.assertEqual("SR101-School of Rock", str(course2))
        self.assertEqual("1023-Jack Black", str(student1))

    def test_get_student(self):
        self.assertEqual(student2, Student.get_student(2011))

    def test_get_course(self):
        self.assertEqual(course2, Course.get_course("SR101"))

    def test_add_student(self):
        course1.enroll(1023)
        course2.enroll(1023)
        course2.enroll(2011)
        self.assertSetEqual({student1, student2}, course2.students)
        self.assertSetEqual({course1, course2}, student1.courses)

    def test_exams(self):
        # Add Students to courses
        course1.enroll(1023)
        course1.enroll(2011)
        course1.enroll(4321)
        course2.enroll(1023)

        # Check Scores are empty
        self.assertListEqual([], course1.get_scores(1023))
        self.assertListEqual([], course1.get_scores(2011))
        self.assertListEqual([], course1.get_scores(4321))
        self.assertListEqual([], course2.get_scores(1023))

        # Add some exams
        course1.add_exam(1023, 20)
        course1.add_exam(1023, 40)
        course1.add_exam(2011, 80)
        course1.add_exam(4321, 70)
        course2.add_exam(1023, 100)

        # Check scores
        self.assertListEqual([20, 40], course1.get_scores(1023))
        self.assertListEqual([80], course1.get_scores(2011))
        self.assertListEqual([70], course1.get_scores(4321))

        # Check Exams by student

        self.assertDictEqual({course1: [20, 40], course2: [100]}, student1.get_scores())
        self.assertDictEqual({course1: [80]}, student2.get_scores())
        self.assertDictEqual({course1: [70]}, student3.get_scores())
