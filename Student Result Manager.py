class StudentResultManager:
    def __init__(self):
        # Initialize an empty dictionary to store student data
        self.students = {}

    def add_student(self, id, name):
        # Add a new student to the dictionary with given name and id
        # Initialize the score as an empty list
        self.students[id] = {"Name": name, "Scores": []}

    def add_score(self, id, score):
        # Add a score (float) to a student's list of scores based on their ID
        if id in self.students:
            self.students[id]["Scores"].append(score)
        else:
            print("Student with ID {} not found.".format(id))

    #def list_students():

        

    def calculate_grade(self, id):
        # Calculate the average score for a student based on their ID
        if id in self.students:
            scores = self.students[id]["Scores"]
            if scores:
                average_score = sum(scores) / len(scores)
                if average_score >= 90:
                    return "A"
                elif average_score >= 80:
                    return "B"
                elif average_score >= 70:
                    return "C"
                elif average_score >= 60:
                    return "D"
                else:
                    return "F"
            else:
                return "No Scores Available"
        else:
            return "Student with ID {} not found.".format(id)


# Create an instance of the StudentResultManager
manager = StudentResultManager()

# Menu for user interaction
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Add Score")
    print("3. Calculate Grade")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        manager.add_student(id, name)
        print("Student added successfully!")

    elif choice == "2":
        id = int(input("Enter Student ID: "))
        score = float(input("Enter Score: "))
        manager.add_score(id, score)
        print("Score added successfully!")

    elif choice == "3":
        id = int(input("Enter Student ID: "))
        grade = manager.calculate_grade(id)
        print("Student Grade:", grade)

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
