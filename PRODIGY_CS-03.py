import re

def assess_password_strength(password):
    # Initialize strength score and feedback
    strength_score = 0
    feedback = []

    # Check for length (minimum 8 characters)
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for presence of uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for presence of lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for presence of numbers
    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for presence of special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Provide feedback based on strength score
    if strength_score == 5:
        return "Password strength: Strong", feedback
    elif 3 <= strength_score < 5:
        return "Password strength: Medium", feedback
    else:
        return "Password strength: Weak", feedback

# Example usage
password = input("Enter a password: ")
strength, feedback = assess_password_strength(password)
print(strength)
for fb in feedback:
    print(fb)
