# all

from firebase.firebase import FirebaseApplication
object = FirebaseApplication("https://officialtech-team.firebaseio.com/")

di = {
    "better_half":"asmita",
      "child1": "misha mishra",
      "child2":"riyan mishra",
      "girl_fr":"rose",
      "affair":"kusu", "ex":"simran",
      }

#_put = object.put("amar", 'mishra', di)
#print(_put)

_get = object.get("amar", None)
print(_get)

#if _get == None:
#    print("Data not Found!")

#else:
#    print(_get)


_delete = object.delete("root/parent/merchant/employee/admin/101", None)
if _delete == None:
    print("Not found!")

else:
    print(_delete, "deleted!")
