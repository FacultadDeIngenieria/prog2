# School

## Instructions
 
### We are going to create a system to manage `Courses`, `Students` and exam scores

### 1. Classes

You will have to define the following Classes:

```python
class Student:
    student_id: int
    name: str
```

```python
class Course:
    course_id: str
    description: str
```    

### 2. Add string conversion (Through __repr__) to the classes

```python
> student1 = Student(1023, "Jack Black")
> student1
1023-Jack Black

> course1 = Course("SR101", "School of Rock")
> course2
SR101-School of Rock

```

### 3. Add `@staticmethods` to get Courses and Students by id 

```python
> Course.get_course("SR101")
SR101-School of Rock

> Student.get_student(1023)
1023-Jack Black
```

### 4. Implement a method in `Course` to `enroll` a `Student` by `student_id`.

`def enroll(self, student_id: int)`

Add the fields:
* `students: Set[Student]` to `Course`
* `courses: Set[Course]` to `Student`

```python
> course1 = Course("CS101", "Introduction to Programming")
> course2 = Course("SR101", "School of Rock")
> student1 = Student(1023, "Jack Black")
> student2 = Student(2011, "Robin Williams")
> student3 = Student(4321, "Steve Carell")

> course1.enroll(1023)
> course1.enroll(2011)
> course2.enroll(1023)
> course1.enroll(4321)

> course1.students
{1023-Jack Black, 2011-Robin Williams}

> student1.courses
{CS101-Introduction to Programming, SR101-School of Rock}
```

### 5. Implement a Method to add an exam score to a `Course` for a given `student_id`

`def add_exam(self, student_id: int, score: int)`

The score should be between `0` and `100`

The data should be stored in a dictionary field:

`exams: Dict[Student, List[int]]` mapping Student -> List of scores

```python
> course1.add_exam(1023, 20)
> course1.add_exam(1023, 40)
> course1.add_exam(2011, 80)
> course1.add_exam(4321, 70)
> course2.add_exam(1023, 100)
> course1.exams
{1023-Jack Black: [20, 40], 2011-Robin Williams: [80], 4321-Steve Carell: [70]}
```

### 6. Implement methods to access the scores

To get the scores for a given `Student` in a `Course`

`def get_scores(self: Course, student_id: int) -> List[int]`

To get the scores af all courses in a `Student`

`def get_scores(self: Student) -> Dict[Course, List[int]]`

```python
> course1.get_scores(1023)
[20, 40]

> student1.get_scores()
{CS101-Introduction to Programming: [20, 40], SR101-School of Rock: [100]} 
```
