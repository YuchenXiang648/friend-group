"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "yuchen": {
        "age": 22,
        "job": "student",
        "connections": {
            "friend": ["yuqi"],
            "partner": ["yuqi"]
        }
    },
    "yuqi": {
        "age": 21,
        "job": "student",
        "connections": {
            "friend": ["yuchen"],
            "partner": ["yuchen"]
        }
    }
}

# Print out the structure in a readable way
for name, info in my_group.items():
    print(f"{name} ({info['age']} years old, {info['job']}):")
    for relation, people in info["connections"].items():
        print(f"  {relation} -> {', '.join(people)}")
    print()