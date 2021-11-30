#dictionary



students = [
    {"name": "Mark", "age": 15, "course": "Secundary School"},
    {"name": "Mary", "age": 10, "course": "Primary School"},
    {"name": "John", "age": 15, "course": "secundary School"}
]

total_age = 0

for student in students:
        total_age += student["age"]
        student["age"] = 0
    
print(f"{total_age} years in total")


