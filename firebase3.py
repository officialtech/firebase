from firebase import firebase
o_v = firebase.FirebaseApplication("https://officialtech-team.firebaseio.com/")

dictonary = {
    "name": "ram",
    "class": "eng",
    "roll_no": "19",
    "s_id": "r19",
    "contact": "1001010"
}

putting = o_v.put("url","name",dictonary)

print(o_v.get("url", "name"))
