from firebase.firebase import FirebaseApplication
me = FirebaseApplication("url of your database")
var_name = me.get("url", "name what you want to get")
print(var_name)





