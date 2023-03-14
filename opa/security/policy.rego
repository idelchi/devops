package access

default allow = false

# Define the roles that have access to the resource
roles := ["admin", "manager"]

# Allow access if
#  - the role is "admin" or "manager"
#  - the username is provided
allow {
    roles[_] = input.role
    input.username != ""
}
