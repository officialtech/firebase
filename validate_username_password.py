

user_nm = input("Username: ")
pass_wd = input("Password: ")

print("Please wait...")
from firebase.firebase import FirebaseApplication
s = FirebaseApplication("https://officialtech-team.firebaseio.com/")

#s.put("https://officialtech-team.firebaseio.com/", "users", {"username": 'jinchao', "password": '12345'})#name, data


u = s.get("https://officialtech-team.firebaseio.com/users", "username")

p = s.get("https://officialtech-team.firebaseio.com/users", "password")



if user_nm == u and pass_wd == p:
    print("Thank-you\nCorrect Credientials!")
elif pass_wd != p and user_nm != u:
    print("Invalid username and password")
elif user_nm != u:
    print("Invalid username")
elif pass_wd != p:
    print("Password Incorrect")
else:
    print("Please Try Again...")

