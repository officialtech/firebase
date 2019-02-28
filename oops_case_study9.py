
from firebase.firebase import FirebaseApplication
fb = FirebaseApplication("https://officialtech-team.firebaseio.com/")


class Student:

    core_python = 3000
    adv_python = 3500

    def __init__(jb):
        print("Core Python fee is", Student.core_python)
        print("Advance Python fee is", Student.adv_python)
        jb.rollno = int(input("Roll No: "))
        jb.name = input("Name: ")
        jb.course = int(input("course: 0 for Core Python\n1 for Advance Python\n"))
        jb._lst = [jb.core(), jb.advance()]
        jb.fee = jb._lst[jb.course]
        jb.select = ['core python', 'advance python']

    def core(self):
        self.msg = "You have choosen Core Python"
        self.total_core = round(Student.core_python * 12.3 // 100 + Student.core_python)
        return self.msg, "Total fee including Tax:", self.total_core

    def advance(self):
        self.msg = "You have choosen Advance Python"
        self.total_advance = round(Student.adv_python * 12.3 // 100 + Student.adv_python)
        return self.msg, "Total fee including Tax:", self.total_advance

    def show(self):
        print(50 * "*")
        print("Name ", self.name)
        print("Roll Number ", self.rollno)
        print(self.fee)
        print(50 * "*")


s1 = Student()
s1.show()

dictonary = {"name": s1.name,
             "roll no": s1.rollno,
            "course": s1.select[s1.course],
            "total fee": s1.fee   }

fb.put("student", "details", dictonary)


