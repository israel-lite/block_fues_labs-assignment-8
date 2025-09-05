import datetime

class AttendanceRegister:
    def __init__(self):
        self.attendance = {}

    def register_student(self, name):
        if name not in self.attendance:
            self.attendance[name] = {"present_days": [], "absent_days": []}
        else:
            print("Student already registered")

    
    def mark_present(self, name):
        today = str(datetime.date.today())
        if name in self.attendance:
            if today not in self.attendance[name]["present_days"]:
                self.attendance[name]["present_days"].append(today)
                if today in self.attendance[name]["absent_days"]:
                    self.attendance[name]["absent_days"].remove(today)
            else:
                print(f"{name} is already marked present today.")
        else:
            print(f"{name} is not registered.")
        
    def mark_absent(self, name):
        today = str(datetime.date.today())
        if name in self.attendance:
            if today not in self.attendance[name]["absent_days"]:
                self.attendance[name]["absent_days"].append(today)
                if today in self.attendance[name]["present_days"]:
                    self.attendance[name]["present_days"].remove(today)
            else:
                print(f"{name} is already marked absent today.")
        else:
            print(f"{name} is not registered.")

record = AttendanceRegister()

record.register_student("John")

record.register_student("Mary")
print(record.attendance)

record.mark_absent("John")
print(record.attendance)