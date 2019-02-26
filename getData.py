from firebase.firebase import FirebaseApplication

a = FirebaseApplication("https://officialtech-team.firebaseio.com/")
#b = input("Get data of ID ")

#print(a.get("new", None))
#print(a.get("root/parent/", None))
#print(a.get("url/name", None))
#print(a.get("root/parent/merchant/", None))
#print(a.get("root/parent/merchant/employee/", None))
#print(a.get("root/parent/merchant/employee/admin", None))

jin = a.get("root/parent/merchant/employee/stocker/", None)

if jin == None:
    print("Sorry Data Not Found!")

else:
    print(jin)