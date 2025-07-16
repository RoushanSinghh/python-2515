import random

# Generate a random 4-digit OTP as a string
correct_otp = str(random.randint(1000, 9999))
print(f"Generated OTP (for testing): {correct_otp}")
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter 4-digit OTP: ")

    if not user_input.isdigit() or len(user_input) != 4:
        print("OTP Must be 4 digit number only")
        continue  # Does not count as a wrong attempt

    if user_input == correct_otp:
        print("Correct OTP - Success")
        break
    else:
        attempts += 1
        if attempts == max_attempts:
            print("Maximum attempts done, try after 24 Hours")
        else:
            print(f"Incorrect OTP. You have {max_attempts - attempts} attempt(s) left.")
