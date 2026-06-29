"""
Student Record Management System
=================================
A menu-driven Python application that manages student records using:
- CSV file for basic student info (reg number, name, course, year, grade)
- JSON file for detailed student info (address, contact, program)
- Log file to record all actions and errors
- Custom exceptions for meaningful error messages
"""

import csv         # For reading/writing CSV files
import json        # For reading/writing JSON files
import logging     # For recording actions and errors to a log file
import os          # For checking if files exist
from datetime import datetime  # For timestamps in logs


# ─────────────────────────────────────────────
# STEP 1: Set up logging
# ─────────────────────────────────────────────
# This creates (or appends to) a file called student_system.log
# Every action and error will be recorded there automatically.

logging.basicConfig(
    filename="student_system.log",         # Log file name
    level=logging.INFO,                    # Record INFO and above (INFO, WARNING, ERROR)
    format="%(asctime)s | %(levelname)s | %(message)s",  # Timestamp | Level | Message
    datefmt="%Y-%m-%d %H:%M:%S"           # Human-readable date format
)

# ─────────────────────────────────────────────
# STEP 2: File names (constants)
# ─────────────────────────────────────────────
CSV_FILE  = "students.csv"   # Stores: reg_number, name, course, year, grade
JSON_FILE = "students.json"  # Stores: reg_number, address, contact, program


# ─────────────────────────────────────────────
# STEP 3: Custom Exceptions
# ─────────────────────────────────────────────
# A custom exception is just a class that inherits from Exception.
# We use them to give friendlier, more specific error messages.

class StudentNotFoundError(Exception):
    """Raised when a student with a given reg number does not exist."""
    pass

class DuplicateStudentError(Exception):
    """Raised when trying to add a student whose reg number already exists."""
    pass

class InvalidInputError(Exception):
    """Raised when the user enters invalid or empty input."""
    pass


# ─────────────────────────────────────────────
# STEP 4: Helper functions for CSV
# ─────────────────────────────────────────────

def load_csv():
    """
    Reads all student records from the CSV file.
    Returns a list of dictionaries, one per student.
    Example: [{"reg_number": "2023/CS/001", "name": "Alice", ...}, ...]
    If the file doesn't exist yet, returns an empty list.
    """
    students = []
    if not os.path.exists(CSV_FILE):
        return students  # No file yet — that's okay, return empty list

    try:
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)  # Reads rows as dictionaries using header row
            for row in reader:
                students.append(row)
    except Exception as e:
        logging.error(f"Failed to read CSV file: {e}")
        print(f"  [Error] Could not read {CSV_FILE}: {e}")

    return students


def save_csv(students):
    """
    Writes the full list of student records back to the CSV file.
    Overwrites the file completely (this is normal for CSV management).
    """
    fieldnames = ["reg_number", "name", "course", "year", "grade"]
    try:
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()      # Writes the column names on the first row
            writer.writerows(students)  # Writes all student rows
    except Exception as e:
        logging.error(f"Failed to write CSV file: {e}")
        print(f"  [Error] Could not save to {CSV_FILE}: {e}")


# ─────────────────────────────────────────────
# STEP 5: Helper functions for JSON
# ─────────────────────────────────────────────

def load_json():
    """
    Reads all detailed student records from the JSON file.
    Returns a dictionary keyed by reg_number.
    Example: {"2023/CS/001": {"address": "...", "contact": "...", "program": "..."}}
    """
    details = {}
    if not os.path.exists(JSON_FILE):
        return details  # No file yet

    try:
        with open(JSON_FILE, mode="r") as file:
            details = json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f"JSON file is corrupted: {e}")
        print(f"  [Error] {JSON_FILE} appears corrupted: {e}")
    except Exception as e:
        logging.error(f"Failed to read JSON file: {e}")
        print(f"  [Error] Could not read {JSON_FILE}: {e}")

    return details


def save_json(details):
    """
    Writes the full details dictionary back to the JSON file.
    indent=4 makes the file human-readable (pretty printed).
    """
    try:
        with open(JSON_FILE, mode="w") as file:
            json.dump(details, file, indent=4)
    except Exception as e:
        logging.error(f"Failed to write JSON file: {e}")
        print(f"  [Error] Could not save to {JSON_FILE}: {e}")


# ─────────────────────────────────────────────
# STEP 6: Input validation helper
# ─────────────────────────────────────────────

def get_input(prompt, required=True):
    """
    Asks the user for input with the given prompt.
    If required=True, it keeps asking until the user types something.
    Strips whitespace from both ends of the input.
    """
    while True:
        value = input(prompt).strip()
        if required and not value:
            print("  [!] This field cannot be empty. Please try again.")
        else:
            return value


# ─────────────────────────────────────────────
# STEP 7: Core Features
# ─────────────────────────────────────────────

def add_student():
    """
    Adds a new student to both the CSV and JSON files.
    Steps:
      1. Collect basic info → save to CSV
      2. Collect detailed info → save to JSON
    Raises DuplicateStudentError if reg number already exists.
    """
    print("\n  ── Add New Student ──")

    try:
        # --- Collect basic info ---
        reg_number = get_input("  Registration Number (e.g. 2024/CS/001): ").upper()
        name       = get_input("  Full Name: ").title()  # .title() capitalizes each word
        course     = get_input("  Course (e.g. Computer Science): ").title()
        year       = get_input("  Year of Study (1–5): ")
        grade      = get_input("  Grade/GPA (e.g. 4.0 or A): ")

        # Validate year is a number between 1 and 5
        if not year.isdigit() or not (1 <= int(year) <= 5):
            raise InvalidInputError("Year of study must be a number between 1 and 5.")

        # --- Check for duplicates ---
        students = load_csv()
        for student in students:
            if student["reg_number"] == reg_number:
                raise DuplicateStudentError(
                    f"A student with reg number '{reg_number}' already exists."
                )

        # --- Save basic info to CSV ---
        students.append({
            "reg_number": reg_number,
            "name":       name,
            "course":     course,
            "year":       year,
            "grade":      grade
        })
        save_csv(students)

        # --- Collect detailed info ---
        print("\n  Now enter additional details:")
        address  = get_input("  Home Address: ")
        contact  = get_input("  Phone / Email: ")
        program  = get_input("  Program Type (e.g. Full-time / Part-time): ").title()

        # --- Save detailed info to JSON ---
        details = load_json()
        details[reg_number] = {
            "address": address,
            "contact": contact,
            "program": program
        }
        save_json(details)

        logging.info(f"Added student: {reg_number} | {name}")
        print(f"\n  ✔ Student '{name}' added successfully!")

    except DuplicateStudentError as e:
        logging.warning(f"Duplicate add attempt: {e}")
        print(f"\n  [!] {e}")

    except InvalidInputError as e:
        logging.warning(f"Invalid input during add: {e}")
        print(f"\n  [!] Invalid input: {e}")

    except Exception as e:
        logging.error(f"Unexpected error in add_student: {e}")
        print(f"\n  [Error] Something went wrong: {e}")

    finally:
        # 'finally' always runs — good for cleanup or closing messages
        print("  ── End of Add Student ──")


def view_all_students():
    """
    Displays all students from the CSV file in a simple table format.
    """
    print("\n  ── All Students ──")

    try:
        students = load_csv()

        if not students:
            print("  No student records found yet.")
            logging.info("Viewed all students: file is empty.")
            return

        # Print a simple header row
        print(f"\n  {'No.':<5} {'Reg Number':<20} {'Name':<25} {'Course':<22} {'Year':<6} {'Grade'}")
        print("  " + "-" * 90)

        for i, s in enumerate(students, start=1):
            print(
                f"  {i:<5} {s['reg_number']:<20} {s['name']:<25} "
                f"{s['course']:<22} {s['year']:<6} {s['grade']}"
            )

        print(f"\n  Total students: {len(students)}")
        logging.info(f"Viewed all students: {len(students)} records displayed.")

    except Exception as e:
        logging.error(f"Error in view_all_students: {e}")
        print(f"\n  [Error] Could not load students: {e}")

    finally:
        print("  ── End of View All ──")


def search_student():
    """
    Searches for a student by their registration number.
    Displays both CSV (basic) and JSON (detailed) info if found.
    Raises StudentNotFoundError if not found.
    """
    print("\n  ── Search Student ──")

    try:
        reg_number = get_input("  Enter Registration Number to search: ").upper()

        students = load_csv()
        found = None

        for student in students:
            if student["reg_number"] == reg_number:
                found = student
                break

        if not found:
            raise StudentNotFoundError(
                f"No student found with registration number '{reg_number}'."
            )

        # Display basic info
        print("\n  ── Basic Info (from CSV) ──")
        print(f"  Reg Number : {found['reg_number']}")
        print(f"  Name       : {found['name']}")
        print(f"  Course     : {found['course']}")
        print(f"  Year       : {found['year']}")
        print(f"  Grade      : {found['grade']}")

        # Display detailed info from JSON if it exists
        details = load_json()
        if reg_number in details:
            d = details[reg_number]
            print("\n  ── Additional Details (from JSON) ──")
            print(f"  Address    : {d.get('address', 'N/A')}")
            print(f"  Contact    : {d.get('contact', 'N/A')}")
            print(f"  Program    : {d.get('program', 'N/A')}")
        else:
            print("\n  (No additional details found in JSON.)")

        logging.info(f"Searched for student: {reg_number} — found.")

    except StudentNotFoundError as e:
        logging.warning(f"Search failed: {e}")
        print(f"\n  [!] {e}")

    except Exception as e:
        logging.error(f"Unexpected error in search_student: {e}")
        print(f"\n  [Error] Something went wrong: {e}")

    finally:
        print("  ── End of Search ──")


def update_student():
    """
    Updates a student's details in both CSV and JSON.
    The user can press Enter to skip any field (keep the old value).
    Raises StudentNotFoundError if reg number doesn't exist.
    """
    print("\n  ── Update Student ──")
    print("  (Press Enter to keep the current value for any field.)")

    try:
        reg_number = get_input("  Enter Registration Number to update: ").upper()

        students = load_csv()
        student_index = None

        for i, s in enumerate(students):
            if s["reg_number"] == reg_number:
                student_index = i
                break

        if student_index is None:
            raise StudentNotFoundError(
                f"No student found with registration number '{reg_number}'."
            )

        # Show current values to help the user decide what to change
        s = students[student_index]
        print(f"\n  Current values for {s['name']}:")
        print(f"    Name   : {s['name']}")
        print(f"    Course : {s['course']}")
        print(f"    Year   : {s['year']}")
        print(f"    Grade  : {s['grade']}")

        # Collect new values — empty input means "keep the old value"
        new_name   = get_input(f"  New Name [{s['name']}]: ", required=False) or s["name"]
        new_course = get_input(f"  New Course [{s['course']}]: ", required=False) or s["course"]
        new_year   = get_input(f"  New Year [{s['year']}]: ", required=False) or s["year"]
        new_grade  = get_input(f"  New Grade [{s['grade']}]: ", required=False) or s["grade"]

        # Validate year if changed
        if not new_year.isdigit() or not (1 <= int(new_year) <= 5):
            raise InvalidInputError("Year of study must be a number between 1 and 5.")

        # Apply updates to CSV data
        students[student_index].update({
            "name":   new_name.title(),
            "course": new_course.title(),
            "year":   new_year,
            "grade":  new_grade
        })
        save_csv(students)

        # Update JSON details if they exist
        details = load_json()
        if reg_number in details:
            d = details[reg_number]
            print(f"\n  Current additional details:")
            print(f"    Address : {d.get('address', 'N/A')}")
            print(f"    Contact : {d.get('contact', 'N/A')}")
            print(f"    Program : {d.get('program', 'N/A')}")

            new_address = get_input(f"  New Address [{d.get('address','N/A')}]: ", required=False) or d.get("address", "")
            new_contact = get_input(f"  New Contact [{d.get('contact','N/A')}]: ", required=False) or d.get("contact", "")
            new_program = get_input(f"  New Program [{d.get('program','N/A')}]: ", required=False) or d.get("program", "")

            details[reg_number] = {
                "address": new_address,
                "contact": new_contact,
                "program": new_program.title()
            }
            save_json(details)

        logging.info(f"Updated student: {reg_number}")
        print(f"\n  ✔ Student '{reg_number}' updated successfully!")

    except StudentNotFoundError as e:
        logging.warning(f"Update failed: {e}")
        print(f"\n  [!] {e}")

    except InvalidInputError as e:
        logging.warning(f"Invalid input during update: {e}")
        print(f"\n  [!] Invalid input: {e}")

    except Exception as e:
        logging.error(f"Unexpected error in update_student: {e}")
        print(f"\n  [Error] Something went wrong: {e}")

    finally:
        print("  ── End of Update ──")


def delete_student():
    """
    Deletes a student's record from both the CSV and JSON files.
    Asks for confirmation before deleting (to prevent accidents).
    Raises StudentNotFoundError if reg number doesn't exist.
    """
    print("\n  ── Delete Student ──")

    try:
        reg_number = get_input("  Enter Registration Number to delete: ").upper()

        students = load_csv()
        original_count = len(students)

        # Filter out the student we want to delete
        updated_students = [s for s in students if s["reg_number"] != reg_number]

        if len(updated_students) == original_count:
            # Nothing was removed — student wasn't found
            raise StudentNotFoundError(
                f"No student found with registration number '{reg_number}'."
            )

        # Safety confirmation before deleting
        confirm = get_input(
            f"  Are you sure you want to delete '{reg_number}'? (yes/no): "
        ).lower()

        if confirm != "yes":
            print("  Deletion cancelled.")
            logging.info(f"Deletion cancelled by user for: {reg_number}")
            return

        # Save updated CSV without the deleted student
        save_csv(updated_students)

        # Remove from JSON too
        details = load_json()
        if reg_number in details:
            del details[reg_number]
            save_json(details)

        logging.info(f"Deleted student: {reg_number}")
        print(f"\n  ✔ Student '{reg_number}' deleted successfully.")

    except StudentNotFoundError as e:
        logging.warning(f"Delete failed: {e}")
        print(f"\n  [!] {e}")

    except Exception as e:
        logging.error(f"Unexpected error in delete_student: {e}")
        print(f"\n  [Error] Something went wrong: {e}")

    finally:
        print("  ── End of Delete ──")


# ─────────────────────────────────────────────
# STEP 8: Main Menu
# ─────────────────────────────────────────────

def display_menu():
    """Prints the main menu to the terminal."""
    print("\n" + "=" * 45)
    print("    STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 45)
    print("  1. Add a New Student")
    print("  2. View All Students")
    print("  3. Search for a Student")
    print("  4. Update Student Details")
    print("  5. Delete a Student Record")
    print("  6. Exit")
    print("=" * 45)


def main():
    """
    The entry point of the program.
    Shows the menu in a loop until the user chooses to exit.
    """
    logging.info("=== Student Management System started ===")
    print("\n  Welcome to the Student Record Management System!")

    while True:
        display_menu()

        try:
            choice = get_input("  Enter your choice (1–6): ")

            if choice == "1":
                add_student()
            elif choice == "2":
                view_all_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                update_student()
            elif choice == "5":
                delete_student()
            elif choice == "6":
                logging.info("=== Student Management System exited ===")
                print("\n  Goodbye! All actions have been logged to student_system.log.\n")
                break
            else:
                # The user typed something other than 1–6
                raise InvalidInputError("Please enter a number between 1 and 6.")

        except InvalidInputError as e:
            logging.warning(f"Invalid menu choice: {e}")
            print(f"\n  [!] {e}")

        except KeyboardInterrupt:
            # Handles Ctrl+C gracefully
            logging.info("Session interrupted by user (Ctrl+C).")
            print("\n\n  Session interrupted. Goodbye!")
            break


# ─────────────────────────────────────────────
# Run the program
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()