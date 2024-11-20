# Define the URL for user registration and user check
url="http://localhost:8000/users/register/"
check_url="http://localhost:8000/users/check/"

# Function to generate a random password
generate_password() {
    local password_length=12  # Ensure this meets your backend requirements
    while true; do
        password=$(tr -dc 'A-Za-z0-9_!@#$%^&*()-+=' < /dev/urandom | head -c "$password_length")
        if [[ ${#password} -ge 8 ]]; then  # Example check for minimum length
            echo "$password"
            return
        fi
    done
}

# Function to check if a user exists
user_exists() {
    local username="$1"
    exists_response=$(curl -X GET "$check_url?username=$username" -s)
    echo "$exists_response" | jq -e '.exists' > /dev/null 2>&1
    return $?
}

# Function to register a user
register_user() {
    local username="$1"  # This should only be the email address
    local password="$2"
    local response=$(curl -X POST "$url" \
        -d "username=$username&password1=$password&password2=$password" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -s)

    echo "$response"
}

# Function for logging
log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> user_creation.log
}

# Read the CSV file and loop through each line (skip the header)
tail -n +2 users.csv | while IFS=',' read -r username password; do
    username=$(echo "$username" | xargs)  # Trim whitespace
    password=$(echo "$password" | xargs)  # Trim whitespace for password

    # Ensure username is a valid email and not concatenated with passwords
    if [[ ! "$username" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$ ]]; then
        log "Invalid username format: $username. Skipping..."
        echo "Invalid username format: $username. Skipping..."
        continue
    fi

    if user_exists "$username"; then
        log "User already exists: $username. Skipping..."
        echo "User already exists: $username. Skipping..."
        continue
    fi

    # Register the user with a newly generated password
    password=$(generate_password)

    # Register the user and capture the response
    response=$(register_user "$username" "$password")

    # Print the server's response
    log "Response for $username: $response"
    echo "Response for $username: $response"

    # Check HTTP response status and content
    if echo "$response" | jq -e '.error' > /dev/null 2>&1; then
        log "Failed to register user: $username"
        echo "Failed to register user: $username"
    else
        log "Successfully registered user: $username"
        echo "Successfully registered user: $username"
    fi
done

echo "User creation completed."
