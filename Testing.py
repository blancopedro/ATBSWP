email = False
for i in "pedro.blanco@outlook.com":
    if (i == "@"):
        email = True

if email == True:
    print("Email is OK")
else:
    print("Email is wrong")