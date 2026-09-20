"""
report_card_system.py
======================
The `ReportCardSystem` class. This replaces the old master `students`
dict plus the free-standing analytics functions (pass_fail_summary,
top_scorers, subject_average, etc). Now they're all methods that
operate on `self.students` — the collection this object owns.
"""

from student import Student


class ReportCardSystem:
    """Owns a collection of Student objects and provides class-wide analytics."""

    system_count = 0   # class attribute: shared counter across ALL ReportCardSystem instances

    def __init__(self):
        self.students = {}   # student_id (int) -> Student object, owned by THIS system
        ReportCardSystem.system_count += 1

    # ---- managing students ----

    def add_student(self, student_id, name):
        """Create and store a new Student. Returns False if ID already used."""
        if student_id in self.students:
            return False
        self.students[student_id] = Student(student_id, name)
        return True

    def get_student(self, student_id):
        """Look up a Student by ID, or None if not found."""
        return self.students.get(student_id)

    def add_marks(self, student_id, subject, marks):
        """Record marks for an existing student. Returns False if student not found."""
        student = self.get_student(student_id)
        if student is None:
            return False
        student.add_marks(subject, marks)
        return True

    # ---- reporting ----

    def report_card(self, student_id):
        """Return one student's report card text, or None if not found."""
        student = self.get_student(student_id)
        if student is None:
            return None
        return student.report_card()

    def all_report_cards(self):
        """Return a list of report card strings for every student."""
        return [student.report_card() for student in self.students.values()]

    def pass_fail_summary(self):
        """Return (passed_names, failed_names) lists."""
        passed = [s.name for s in self.students.values() if s.has_passed()]
        failed = [s.name for s in self.students.values() if not s.has_passed()]
        return passed, failed

    def top_scorers(self, n=3):
        """Return the top n students as a list of Student objects, highest average first."""
        ranked = sorted(self.students.values(), key=lambda s: s.average(), reverse=True)
        return ranked[:n]

    def subject_average(self, subject):
        """Return the class average for one subject, or None if nobody has marks in it."""
        subject = subject.strip().title()
        marks = [s.scores[subject] for s in self.students.values() if subject in s.scores]
        if not marks:
            return None
        return sum(marks) / len(marks)

    # ---- class method: reads the shared class attribute above ----

    @classmethod
    def active_systems(cls):
        """How many ReportCardSystem objects have been created (class-wide)."""
        return cls.system_count
