def reassign_dict(d):
    d = {"name": "Shikha", "age": 20}
    print("Inside function:", d)

student = {"name": "Rahul"}

print("Before:", student)

reassign_dict(student)

print("After:", student)