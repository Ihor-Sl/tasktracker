from login import USERS


def signup(username, password):
    if username in USERS:
        return False
    USERS[username] = password
    return True
