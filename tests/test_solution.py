# [Your Full Name] - Assignment 1 Unit Tests
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
from solution import verify_access

# Test 1: Wrong username
assert verify_access("hacker", "S3cur3_P@ss", 5) == "INTRUSION_DETECTED", "Failed wrong username check"

# Test 2: Wrong password
assert verify_access("soc_admin", "wrong123", 5) == "INTRUSION_DETECTED", "Failed wrong password check"

# Test 3: Valid login, Level 5 clearance
assert verify_access("soc_admin", "S3cur3_P@ss", 5) == "ROOT_ACCESS_GRANTED", "Failed Level 5 check"

# Test 4: Valid login, Level 3 clearance
assert verify_access("soc_admin", "S3cur3_P@ss", 3) == "ANALYST_ACCESS_GRANTED", "Failed Level 3 check"

# Test 5: Valid login, Level 1 clearance
assert verify_access("soc_admin", "S3cur3_P@ss", 1) == "INSUFFICIENT_CLEARANCE", "Failed Level 1 check"

print("ALL UNIT TESTS PASSED - ASSIGNMENT 1")
