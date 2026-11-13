class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = None
        self.set_mark(mark)

    def set_mark(self, mark):
        # Validates marks between 0 and 100
        if not (0 <= mark <= 100):
            raise ValueError(f"Invalid mark for {self.name}: {mark}. Must be 0-100.")
        self.mark = mark

    def grade(self):
        # Assigns a grade based on the mark
        if self.mark >= 90: return 'A'
        elif self.mark >= 80: return 'B'
        elif self.mark >= 70: return 'C'
        elif self.mark >= 60: return 'D'
        else: return 'F'

def process_student_files(input_filename, output_filename):
    # Try and except around the parts that can fail
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                try:
                    name, mark_str = line.strip().split(',')
                    student = Student(name, int(mark_str))
                    outfile.write(f"{student.name} scored {student.mark} (Grade: {student.grade()})\n")
                except ValueError as ve:
                    print(f"Skipping invalid data '{line.strip()}': {ve}")
        print("File processing complete.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage (assuming 'students_input.txt' exists with format "Name,Mark"):
# process_student_files('students_input.txt', 'students_output.txt')
