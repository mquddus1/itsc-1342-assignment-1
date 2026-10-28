# Mohammed Abdul Quddus - Assignment 1

def verify_access(username, password, clearance_level):
    if username != "soc_admin" or password != "S3cur3_P@ss":
        return "INTRUSION_DETECTED"
    elif clearance_level >= 5:
        return "ROOT_ACCESS_GRANTED"
    elif clearance_level == 3 or clearance_level == 4:
        return "ANALYST_ACCESS_GRANTED"
    else:
        return "INSUFFICIENT_CLEARANCE"
