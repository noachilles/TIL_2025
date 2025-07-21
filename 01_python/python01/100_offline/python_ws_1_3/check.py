def check_adults(user):
    if user["age"] >= 18:
        return True
    return False

def check_active(user): 
    if user["is_active"]:
        return True
    return False

def check_adults_active(user):
    if user["age"] >= 18 and user["is_active"]:
        return True
    return False