import re

def check_password_strength(password):
    """Check and display the strength of a password"""
    missing = []

    # Check for uppercase, lowercase, digits, and symbols
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    if not has_upper:
        missing.append("uppercase letter")
    if not has_lower:
        missing.append("lowercase letter")
    if not has_digit:
        missing.append("number")
    if not has_symbol:
        missing.append("symbol")

    # Evaluate strength
    if len(password) < 6:
        strength = "❌ Weak (Too Short)"
    elif all([has_upper, has_lower, has_digit, has_symbol]) and len(password) >= 8:
        strength = "✅ Strong"
    elif sum([has_upper, has_lower, has_digit, has_symbol]) >= 3:
        strength = "⚠️ Medium"
    else:
        strength = "❌ Weak"

    print(f"\nPassword: {password}")
    print(f"Strength Level: {strength}")

    if missing:
        print("Missing conditions:", ", ".join(missing))
    else:
        print("All security conditions met ✅")

def main():
    password = input("Enter your password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
