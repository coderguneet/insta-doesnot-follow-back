f= open("followers.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
f1 = open("following.txt", "r", encoding="utf-8")
lines1 = f1.readlines()
f1.close()

non_followers = [i for i in lines1 if i not in lines]
for i in non_followers:
    if non_followers:
        print(i)
if len(non_followers)==0:
    print("everyone you follow , follows you back 🗿🗿🗿🗿")