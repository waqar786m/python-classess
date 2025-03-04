# Function with user input
def greet(name: str) -> str:
    return f"Welcome, {name}!"

user_name = input("Enter your name: ")
print(greet(user_name))

# -------------------------------

# Data Types

# string
username: str = "Waqar"

# integer
user_age: int = 21

# float
user_height: float = 5.5

# boolean
is_developer: bool = True

# list
skills: list = ["Python", "Next.js", "Typescript"]

# tuple
location: tuple = ("Karachi", "Pakistan")

# dictionary
user: dict = {"name": "Waqar", "age": 21, "skills": skills}

# set
unique_ids: set = {101, 102, 103}

# Display all values
print(username, user_age, user_height, is_developer, skills, location, user, unique_ids)
