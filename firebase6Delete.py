# deleting

from firebase.firebase import FirebaseApplication

f = FirebaseApplication("https://officialtech-team.firebaseio.com/")

f.delete("root/parent/merchant/employee/", "admin")
