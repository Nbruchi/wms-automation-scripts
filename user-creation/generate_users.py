import random
import string

# A larger list of common first names (around 300)
first_names = [
    "aaron", "mike", "peter", "john", "jane", "sarah", "laura", "emma", "oliver", "liam", "sophia", "noah", "ava",
    "elijah", "lucas", "benjamin", "james", "henry", "amelia", "harper", "daniel", "matthew", "grace", "charlotte",
    "jacob", "ethan", "alexander", "logan", "zoe", "isabella", "hannah", "jackson", "mason", "sebastian", "aidan",
    "nicholas", "alex", "anthony", "dylan", "ryan", "nathan", "caleb", "evan", "lily", "ellie", "madison", "chloe",
    "emma", "olivia", "mia", "nora", "ella", "scarlett", "avery", "sophie", "eva", "lillian", "mila", "penelope",
    "grayson", "owen", "isaac", "levi", "carter", "gabriel", "andrew", "joshua", "samuel", "william", "theodore",
    "simon", "george", "lucy", "hazel", "violet", "leo", "max", "nathaniel", "xavier", "tyler", "adam", "christopher",
    "zoey", "stella", "samantha", "kayla", "bella", "brooke", "paisley", "addison", "riley", "aurora", "rebecca",
    "allison", "ruby", "lucas", "kevin", "brandon", "ian", "jesse", "eric", "julia", "elena", "morgan", "lola",
    "natalie", "sophie", "melissa", "tiffany", "cameron", "logan", "luke", "harry", "margaret", "phoebe", "clara",
    "zoe", "amelie", "sophia", "daisy", "eleanor", "ivy", "isla", "emily", "molly", "rosie", "willow", "eliza",
    "madeline", "felix", "vincent", "thomas", "arthur", "jeremy", "emmett", "charlie", "elliot", "liam", "jameson",
    "charles", "henry", "reed", "ellis", "rowan", "tristan", "kylie", "naomi", "faith", "victoria", "elsie", "rachel",
    "lucia", "martha", "fiona", "joseph", "kenneth", "leo", "conor", "jack", "leo", "blake", "harvey", "david",
    "barbara", "donald", "betty", "ronald", "patricia", "nancy", "brian", "ashley", "dennis", "gordon", "michael",
    "steven", "timothy", "robert", "josephine", "edward", "fredrick", "victor", "michael", "kenneth", "gregory",
    "donald", "walter", "george", "paul", "thomas", "claire", "louis", "jackson", "otis", "ryder", "sawyer", "julian",
    "cody", "frank", "clark", "jay", "keith", "neal", "spencer", "jeff", "terry", "ronnie", "brad", "marcus", "otto",
    "dave", "elmer", "walt", "bruce", "rex", "fred", "wesley", "norman", "leo", "mario", "harvey", "pat", "otto",
    "travis", "lance", "wayne", "russell", "clyde", "oscar", "chester", "alvin", "bobby", "craig", "vance", "glenn",
    "stuart", "clint", "ernie", "burt", "alex", "chuck", "howard", "clay", "art", "elliott", "drew", "graham", "rex",
    "gus", "ralph", "jim", "ted", "ross", "don", "hugh", "glen", "dean", "bill", "cliff", "dale", "leslie", "lyle",
    "sherman", "vernon", "arnold", "johnny", "willie", "eugene", "dean", "rex", "benny", "elroy", "russ", "albert",
    "chad", "greg", "randy", "lance", "ken", "brody", "dale", "buck", "clay", "grady", "roy", "scott", "harley", "les",
    "percy", "clark", "dane", "hank", "earl", "bert", "archie"
]

def generate_username():
    first_name = random.choice(first_names)
    number = random.randint(1, 9999)  # Optional number to ensure uniqueness
    return f"{first_name}{number}"

# Function to generate a random email
def generate_email():
    username = generate_username()
    domain = random.choice(["gmail.com", "outlook.com", "yahoo.com", "protonmail.com", "icloud.com"])
    return f"{username}@{domain}"

# Function to generate a valid password
def generate_password(username):
    special_chars = "!@#$%^&*()"
    while True:
        password_length = random.randint(12, 16)  # Ensure minimum length of 12
        password = ''.join(random.choices(string.ascii_letters + string.digits + special_chars, k=password_length))

        # Check password validity
        if (len(password) >= 12 and                             # Minimum length check
            any(c.islower() for c in password) and            # At least one lowercase
            any(c.isupper() for c in password) and            # At least one uppercase
            any(c.isdigit() for c in password) and            # At least one digit
            any(c in special_chars for c in password) and     # At least one special character
            username.split('@')[0] not in password):          # Username check
            return password

# Generate 200 unique users
users_set = set()  # To track unique usernames
with open("users.csv", "w") as file:
    file.write("username,password,password_confirmation\n")
    while len(users_set) < 200:
        email = generate_email()
        username = email.split('@')[0]  # Extract username part from email
        if username not in users_set:  # Ensure uniqueness
            password = generate_password(email)
            file.write(f"{email},{password},{password}\n")
            users_set.add(username)  # Add the unique username to the set

print("Generated 200 users in 'users.csv'")