e_id = int(input("Employee ID: "))
e_name = input("Employee Name: ")
e_salary = float(input("Employee Salary: "))
e_contact = int(input("Employee Contact Number: "))

from firebase.firebase import FirebaseApplication
obj = FirebaseApplication("https://officialtech-team.firebaseio.com/")

_dict = {
    "Name": e_name,
    "ID": e_id,
    "Salary": e_salary,
    "Contact": e_contact
}

putting = obj.put("employee_details", "group-a", _dict)
print(obj.get("group-a", None))

