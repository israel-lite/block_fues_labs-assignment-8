import datetime

# today = datetime.date.today()
# print(f"Today's date is: {today}")

class AttendanceRegister:
    def __init__(self):
        self.attendance = {}

    def register_student(self, name):
        if name not in self.attendance:
            self.attendance[name] = {
                present_days: [],
                absent_days: []
            }
        else:
            return "Student already registered"
        

student1 = AttendanceRegister()

print(student1)