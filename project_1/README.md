# Student Report Card & Grade Analyzer

A medium-level, console-based mini project built in pure Python (no external
libraries). It simulates a simple school system: you add students, enter
their marks subject by subject, and the program generates report cards and
class-wide analytics.

It's designed as a single learning exercise that touches every core Python
fundamental: `print()`, `if/else` (including nested conditions), `for` and
`while` loops, lists, list comprehension, slicing, and dictionaries — with
docstrings on every function and exception handling around all user input.

---

## 1. What the project does

Run the script and you get a menu:

```
========================================
   STUDENT REPORT CARD & GRADE ANALYZER
========================================
1. Add Student
2. Add Marks
3. View One Report Card
4. View All Report Cards
5. Pass / Fail Summary
6. Top Scorers
7. Subject-wise Class Average
8. Exit
========================================
```

| Option | What it does |
|---|---|
| 1. Add Student | Registers a new student with an ID and name |
| 2. Add Marks | Records marks for a subject against an existing student |
| 3. View One Report Card | Prints one student's subject-wise marks, average, and grade |
| 4. View All Report Cards | Loops through every student and prints their report card |
| 5. Pass / Fail Summary | Splits students into "passed" and "failed" lists (40% cut-off) |
| 6. Top Scorers | Shows the top 3 students ranked by average marks |
| 7. Subject-wise Class Average | Calculates the class average for one subject across all students |
| 8. Exit | Stops the program |

The menu keeps reappearing until you choose **Exit** — that repetition is
driven by a `while` loop in `main()`.

---

## 2. Data model — why a dictionary of dictionaries

Everything is stored in one dictionary, `students`:

```python
students = {
    1: {
        "name": "Raju",
        "scores": {"Math": 90, "Science": 85, "English": 78}
    },
    2: {
        "name": "Meera",
        "scores": {"Math": 60, "Science": 55, "English": 70}
    }
}
```

- **Outer dictionary key** → student ID (an `int`). Dictionaries give
  instant lookup by ID (`students[student_id]`) instead of scanning a list.
- **Outer dictionary value** → another dictionary holding `"name"` and
  `"scores"`.
- **`"scores"`** → itself a dictionary mapping `subject name -> marks`.
  Using a dictionary here (instead of a list) means each mark is tied to
  its subject by name, so `"Math"` always means `Math`, no matter what
  order subjects were entered in.

This nested-dictionary shape is the backbone the rest of the program reads
and writes to.

---

## 3. Concept-by-concept walkthrough

### `print()` statements
Used throughout for menus, confirmations, and the formatted report card
(`f"{subject:<15}: {marks:>6.2f}"` — left-aligns the subject name and
right-aligns the marks to two decimal places).

### `if / else` and nested `if / else`
`calculate_grade(percentage)` is the clearest example. It first checks the
pass/fail boundary (`>= 40`), then **nests** further `if/else` blocks
inside the "passed" branch to narrow the exact grade band:

```
>= 40%  → keep narrowing
    >= 90 → A+
    else  → keep narrowing
        >= 75 → A
        else  → keep narrowing
            >= 60 → B
            else  → keep narrowing
                >= 50 → C
                else  → D
< 40%   → F
```

Each `else` opens a new, more specific question — that's what makes it
"nested" rather than a flat `elif` chain, and it mirrors how a real grading
policy is often described ("if they passed, then check if they got a
distinction, and if not, check the next band...").

### `for` loops
- `display_all_reports()` loops over every student ID in `students`.
- `generate_report_card()` loops over `student["scores"].items()` to print
  each subject line.
- `top_scorers()` uses `enumerate(top_n, start=1)` to number the ranking.

### `while` loop
`main()` wraps the whole menu in `while running:`. The loop only stops when
the user picks option 8, which sets `running = False`. This is what makes
the program feel like an interactive app instead of a script that runs
once and exits.

### Lists
- `list(scores.values())` inside `compute_average()` turns the marks into
  a plain list so `sum()` and `len()` can work on it.
- `top_scorers()` and `subject_average()` build lists of tuples like
  `[("Raju", 87.5), ("Meera", 57.5)]` before sorting/filtering them.

### List comprehension
Three places use it instead of manual loops with `.append()`:

```python
averages = [(s["name"], compute_average(s["scores"])) for s in students.values()]
passed   = [name for name, avg in averages if avg >= 40]
marks_for_subject = [s["scores"][subject] for s in students.values() if subject in s["scores"]]
```

The last one is a comprehension **with a condition** — it only pulls a
mark into the list if that student actually has a score for that subject,
which avoids a `KeyError` for students who haven't been graded in it yet.

### Slicing
`top_scorers()` sorts all students by average (highest first) and then
uses `ranked[:n]` to slice off just the top `n` (default 3). Slicing is
what turns "everyone, sorted" into "just the top few" without writing a
manual loop with a counter.

### Dictionaries
Beyond the main `students` structure, dictionaries are used for:
- `student["scores"]` — subject → marks
- Rebuilding a fresh, empty `"scores": {}` dictionary whenever a new
  student is added

### Docstrings
Every function has a docstring following the NumPy-style format
(`Parameters`, `Returns`, `Raises`) explaining what it does, what it takes
in, and what it hands back. The module itself also has a top-of-file
docstring describing the whole project and its data model.

### Exception handling
Nothing in the menu loop can crash the program from bad input:

| Situation | Exception caught | Where |
|---|---|---|
| Non-numeric menu choice | `ValueError` | `main()` |
| Non-numeric student ID / marks | `ValueError` | `add_student()`, `add_marks()`, option 3 in `main()` |
| Marks entered for a student ID that doesn't exist | `KeyError` | `add_marks()` |
| Viewing/printing a report card for an unknown ID | `KeyError` | `generate_report_card()` |
| Asking for a subject average when nobody has that subject yet | `ZeroDivisionError` | `subject_average()` |

Each `except` block prints a friendly message and returns control to the
menu instead of letting the program terminate with a traceback.

---

## 4. How to run it

```bash
python3 report_card_system.py
```

Follow the on-screen menu. A typical first run:

1. Choose `1` → add a student (e.g., ID `1`, name `Raju`)
2. Choose `2` → add marks for that student (e.g., subject `Math`, marks `90`)
3. Repeat step 2 for more subjects, and steps 1–2 for more students
4. Choose `4` to see everyone's report card
5. Choose `5`, `6`, or `7` to see the class analytics
6. Choose `8` to exit

---

## 5. Possible extensions (if you want to go further later)

- Persist `students` to a JSON file so data survives between runs
- Add a "remove student" or "edit marks" option
- Add input validation for duplicate subjects per student (currently a
  second entry just overwrites the first, which is intentional but worth
  knowing)
- Wrap `students` and its functions into a `Student`/`School` class to
  practice OOP on top of the same logic