student_names = {'Atul': 90,'Alice': 85, 'Anu': 97 }
user_input=input("Enter the student's name: ")
try:
    #print(f"{user_input}'s marks: {student_names[user_input]}")
    print(user_input + "'s marks: " + str(student_names[user_input]))
except KeyError:
    print("Student not found")