from firebase.firebase import FirebaseApplication
f = FirebaseApplication("https://officialtech-team.firebaseio.com/")
_id = int(input("ID: "))

result = f.get("_id", None)
print(result)