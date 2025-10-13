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


    # --- New functions for stretch task ---

def forget(person1, person2):
    """Remove the connection between two people if it exists."""
    if person2 in my_group[person1]["relations"]:
        del my_group[person1]["relations"][person2]
    if person1 in my_group[person2]["relations"]:
        del my_group[person2]["relations"][person1]


def add_person(name, age=None, job=None, relations=None):
    """Add a new person to the group."""
    if relations is None:
        relations = {}
    my_group[name] = {
        "age": age,
        "job": job,
        "relations": relations
    }


def average_age():
    """Return the mean age of all people in the group."""
    ages = [info["age"] for info in my_group.values() if info["age"] is not None]
    return sum(ages) / len(ages) if ages else None
