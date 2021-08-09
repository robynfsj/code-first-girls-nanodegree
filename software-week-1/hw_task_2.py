"""CFG Nanodegree Software Specialisation Homework 1 Task 2 – Students"""


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# TASK
# ----
#
# Write a base class to represent a student. Below is a starter code.
# Feel free to add any more new features to your class.
# As a minimum a student has a name and age and a unique ID.
#
# Create a new subclass from student to represent a concrete student doing a
# specialisation, for example:
# Software Student and Data Science student.
#
# Create new methods that manage student's subjects (add/remove new subject and
# its grade to the dict).
# Create a method to view all subjects taken by a student.
# Create a method (and a new variable) to get student's overall mark (use
# average).
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# WRITE A BASE CLASS TO REPRESENT A STUDENT
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


# NOTE: I decided to remove subjects from the Student base class as it doesn't
#       work for all student types. For example, an A-level student would take
#       several subjects but a university student usually takes one subject.
#       Also a Nanodegree student doesn't really take subjects that have a
#       grade - we have assessments and grades. So having a dictionary of
#       subjects and grades doesn't make sense in the base class. These details
#       are specific to the type of student.


class Student:
    """A base class to represent a student"""

    def __init__(self, fname, lname, age, institution, s_id):
        """Initialise the class Student

        :param fname: student's first name
        :type fname: str
        :param lname: student's last name
        :type lname: str
        :param age: student's age
        :type age: int
        :param institution: student's institution
        :type institution: str
        :param id: student's student ID reference
        :type id: str
        """
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.age = age  # it would make more sense if this was DOB but the task specifies a student has to have an age
        self.institution = institution.title()
        self.s_id = s_id

    def view_student_details(self):
        """Print out data held on a student

        :return: print out of student details
        """
        print(f"–––––––––––––––\n"
              f"STUDENT DETAILS\n"
              f"–––––––––––––––\n"
              f"First Name: {self.fname}\n"
              f"Last Name: {self.lname}\n"
              f"Age: {self.age}\n"
              f"Institution: {self.institution}\n"
              f"Student ID: {self.s_id}\n")


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# WRITE A SUBCLASS TO REPRESENT A NANODEGREE STUDENT
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


class CFGNanoStudent(Student):
    """A subclass of Student to represent a Code First Girls Nanodegree student"""

    def __init__(self, fname, lname, age, institution, s_id, specialisation):
        """Initialise the CFGNanoStudent subclass

        :param fname: student's first name
        :type fname: str
        :param lname: student's last name
        :type lname: str
        :param age: student's age
        :type age: int
        :param institution: student's institution
        :type institution: str
        :param s_id: students student ID
        :type s_id: str
        :param specialisation: Nanodegree specialisation – software or data
        :type specialisation: str
        """
        super().__init__(fname, lname, age, institution, s_id)
        self.course = "Nanodegree"
        self.specialisation = specialisation.capitalize()
        self.modules = set()
        self.grades = {"Foundation Theory": None,
                       "Specialisation Theory": None,
                       "Foundation Exam": None,
                       "Specialisation Exam": None,
                       "Homework": None,
                       "Project": None}
        self.final_result = None

    def view_student_details(self):
        """Print out data held on a CFG Nanodegree student.

        Overrides Student.view_student_details(self).

        :return: print out of student details
        """
        print(f"\n–––––––––––––––\n"
              f"STUDENT DETAILS\n"
              f"–––––––––––––––\n"
              f"First Name: {self.fname}\n"
              f"Last Name: {self.lname}\n"
              f"Age: {self.age}\n"
              f"Institution: {self.institution}\n"
              f"Student ID: {self.s_id}\n"
              f"Course: {self.course}\n"
              f"Specialisation: {self.specialisation}\n"
              f"Modules: {', '.join(self.modules)}\n"
              f"Final Result: {self.final_result}\n")

    def module_reg(self, module_name):
        """Register student on a module

        :param module_name: name of module
        :type module_name: str
        :return: adds named module to student's modules set
        """
        self.modules.add(module_name)
        print(f"{self.fname} {self.lname} has been successfully registered on "
              f"{module_name}.")

    def module_dereg(self, module_name):
        """De-register student for a module

        :param module_name: name of module
        :type module_name: str
        :return: removes named module from student's modules set
        """
        self.modules.discard(module_name)
        print(f"{self.fname} {self.lname} is no longer registered on "
              f"{module_name}.")

    def add_grade(self, assessment, grade):
        """Add a grade for the specified assessment

        :param assessment: name of assessment, must be one of:
                           "Foundation Theory"
                           "Specialisation Theory"
                           "Foundation Exam"
                           "Specialisation Exam"
                           "Homework"
                           "Project"
        :type assessment: str
        :param grade: grade achieved in assessment (%)
        :type grade: int
        :return: grade is added as a value to the specified assessment key in
                 the student's grades dict
        """
        assessment = assessment.title()
        try:
            self.grades[assessment] = grade
        except KeyError:
            print("Assessment type not found.")
        else:
            print(f"Mark successfully entered on the student's record.")

    def weighted_grade(self):
        """Calculates the Nanodegree student's final weighted grade

        :return: grade (%) assigned to self.final_result
        """
        # Assessment weightings
        w_foundation_theory = 5
        w_specialisation_theory = 5
        w_foundation_exam = 20
        w_specialisation_exam = 20
        w_homework = 10
        w_project = 40

        # Student's results
        r_foundation_theory = self.grades["Foundation Theory"]
        r_specialisation_theory = self.grades["Specialisation Theory"]
        r_foundation_exam = self.grades["Foundation Exam"]
        r_specialisation_exam = self.grades["Specialisation Exam"]
        r_homework = self.grades["Homework"]
        r_project = self.grades["Project"]

        # Calculate weighted grade
        weighted_grade = (
                                 (w_foundation_theory * r_foundation_theory) +
                                 (w_specialisation_theory * r_specialisation_theory) +
                                 (w_foundation_exam * r_foundation_exam) +
                                 (w_specialisation_exam * r_specialisation_exam) +
                                 (w_homework * r_homework) +
                                 (w_project * r_project)
                         ) / 100

        self.final_result = weighted_grade
        print(f"Nanodegree Final Grade: {int(weighted_grade)} %")


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# EXAMPLES OF CODE IN ACTION
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# Examples of base class Student
e_evans = Student('elen',
                  'evans',
                  26,
                  "code first girls",
                  394827)

s_williams = Student('sioned',
                     'williams',
                     23,
                     "lancaster university",
                     394144)

e_evans.view_student_details()
s_williams.view_student_details()


# Example Nanodegree student
e_jones = CFGNanoStudent('eleri',
                         'jones',
                         27,
                         "Code First Girls",
                         294839,
                         "software")

# Register Eleri on modules
e_jones.module_reg("Python Foundation")
e_jones.module_reg("Software Specialisation")
e_jones.view_student_details()

# Eleri was mistakenly registered on Python Foundation. She should have been
# registered on Python Refresher and SQL Foundation.
e_jones.module_dereg("Python Foundation")
e_jones.module_reg("Python Refresher")
e_jones.module_reg("SQL Foundation")
e_jones.view_student_details()

# Add grades and calculate final grade
e_jones.add_grade("Foundation Theory", 78)
e_jones.add_grade("Specialisation Theory", 82)
e_jones.add_grade("Foundation Exam", 67)
e_jones.add_grade("Specialisation Exam", 71)
e_jones.add_grade("Homework", 94)
e_jones.add_grade("Project", 76)
e_jones.weighted_grade()
e_jones.view_student_details()


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# DOCUMENTING CLASSES AND METHODS
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Not part of the assessment but wanted to play with documenting my methods.
# This is helpful when reading through the code and you can also print the
# __doc__ method. The docstring also opens as a pop up when you hover over the
# method name in PyCharm. There are different docstring formats. These use the
# reStructured Text format, which is the official Python documentation
# standard. Others include Google docstrings, NumPy/SciPy docstrings and
# Epytext.

print(Student.__doc__)
print(CFGNanoStudent.__doc__)
print(CFGNanoStudent.view_student_details.__doc__)
