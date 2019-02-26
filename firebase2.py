from firebase import firebase # calling all classes of firebase module
f = firebase.FirebaseApplication("https://officialtech-team.firebaseio.com/")
res = f.put("new", "jb", {"101":"me", "102":"you"})
