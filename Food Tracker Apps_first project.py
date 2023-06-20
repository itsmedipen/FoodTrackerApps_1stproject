print("_" * 30)
print("Food Tracker Apps")
print("-" * 30)

print()
print("It's Saturday. Can I eat cake and ice-cream?")

weekdays = ["Sun", "Mon", "Tues", "Wednes", "Thurs", "Fri"]

answers = []

for i in weekdays:
    print(f"Did you eat healthy in {i}day?")
    answer = input("'Y' or 'N':")
    if answer == 'Y':
        answers.append(answer)

print()
print("Calculating the answers....!")

if len(answers) == 6:
    print("Yes, You can eat the cake and ice-cream.")

elif len(answers) == 5:
    print("Lay off the ice-cream.")

else:
    print("The cake is the lies so is the ice-cream.")
