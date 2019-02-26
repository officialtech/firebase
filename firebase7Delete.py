
from firebase import firebase
o = firebase.FirebaseApplication("https://officialtech-team.firebaseio.com/")

# putting
p = o.put("brand_new", "parent_new", {"_id":1010, "cat": 'gen', "count": 1})
print("Created!", p)

# getting
g = o.get("brand_new/parent_new", None)
print("Fetched result!", g)

#deleting
d = o.delete("new/", "jb")
print("Deleted", d)