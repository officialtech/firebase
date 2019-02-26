from firebase.firebase import FirebaseApplication

object = FirebaseApplication("https://officialtech-team.firebaseio.com/")

getted = object.get("student/student_details", None)

if getted == None:
    print("Data Not found!")

else:
    object.delete("student", "student_details")
    print("data deleted!")
