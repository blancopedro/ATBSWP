dogNames = []

while True:
    print("Enter the name of your dog" + str(len(dogNames) + 1)) + "Or enter nothing to stop):")
    name = input()
    if name == "":
        break
    dogNames = dogNames + [name]

