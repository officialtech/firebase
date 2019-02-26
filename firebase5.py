from firebase.firebase import FirebaseApplication

o = FirebaseApplication("https://officialtech-team.firebaseio.com/")

s_name = input("name ")
s_id = input("id ")
s_contact = int(input("contact "))

r = o.get("student", s_name)
if r == None:
    o.put("student",s_id, {"name": "me_jb","salary": "1234000.00"})
    print(s_id, "is created!")

else:
    print(s_id, "is not available")

#m = o.put("student", "student_details", {"s1":"avi", "s2": "bro", "s3": "chan"})
#print(m)

