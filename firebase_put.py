from firebase.firebase import FirebaseApplication # calling one Class only
fire = FirebaseApplication("url")
dictonary = {"merchant":{"employee":{"admin":{"101":{"username": "rooh", "password": "rp808"},
                                               "102":{"username":"off944", "password": "tech944"}},"stocker":{
        "1001":{"username":"techque", "password":"techno123"},"1002":{"username":"ac", "password": "kc123"}
    }}}}
f = fire.put("root", "parent", dictonary)
print(f)


