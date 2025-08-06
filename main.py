import string
import re

def has_repeating_number_patterns(password):
    # Pattern 1: Three or more of the same digit (e.g., 111, 2222)
    if re.search(r'(\d)\1{2,}', password):
        return True

    # Pattern 2: Repeating digit sequences (e.g., 123123, 456456)
    for i in range(1, len(password) // 2):
        seq = password[:i]
        repeated = seq * (len(password) // len(seq))
        if seq.isdigit() and repeated in password:
            return True

    return False

def has_common_number_sequences(password):
    """
    Detects common numeric sequences such as 123, 1234, 7890, 987, etc.
    Returns True if any sequence is found.
    """
    common_sequences = [
        '123', '1234', '12345', '123456',
        '234', '345', '456', '4567', '5678',
        '789', '890', '098', '9876', '987', '876',
        '000', '111', '222', '333', '444', '555', '666', '777', '888', '999'
    ]
    
    for seq in common_sequences:
        if seq in password:
            return True
    return False

def check_password_strength(password, common_passwords_file='common.txt'):
    # Character type checks
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)

    length = len(password)
    score = 0

    # Load common password list with UTF-8 encoding
    try:
        with open(common_passwords_file, 'r', encoding='utf-8', errors='ignore') as f:
            common_passwords = f.read().splitlines()
    except FileNotFoundError:
        print(f"❌ Error: '{common_passwords_file}' not found.")
        return

    # Check if password is common
    if password in common_passwords:
        print("❌ Password found in common password list. Score: 0/10")
        return

    # Length scoring
    if length >= 8:
        score += 2
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if length >= 20:
        score += 1

    # Character type scoring
    score += has_upper + has_lower + has_digit + has_special  # max +4

    # Penalize for repeated number patterns
    if has_repeating_number_patterns(password):
        print("⚠️  Warning: Your password contains repeating number sequences (e.g., '111', '123123').")
        print("   These patterns are easier to guess. Consider making it more random.")
        score -= 2

    # Penalize for common numeric sequences like 123, 4567, 9876
    if has_common_number_sequences(password):
        print("⚠️  Warning: Your password contains common number sequences (e.g., '123', '9876').")
        print("   These are predictable and insecure.")
        score -= 2

    # Clamp score between 0 and 10
    score = max(0, min(score, 10))

    # Final score
    print(f"\n✅ Password checked successfully. Score: {score}/10")

    # Strength label
    if score >= 9:
        strength = "Very Strong 💪"
    elif score >= 7:
        strength = "Strong ✅"
    elif score >= 5:
        strength = "Moderate ⚠️"
    elif score >= 3:
        strength = "Weak ❗"
    else:
        strength = "Very Weak ❌"

    print(f"🔒 Password Strength: {strength}\n")

    # Suggestions to improve
    if score < 8:
        print("🛠 Suggestions to improve your password:")
        if not has_upper:
            print("- Add at least one uppercase letter.")
        if not has_lower:
            print("- Add at least one lowercase letter.")
        if not has_digit:
            print("- Include at least one number.")
        if not has_special:
            print("- Use special characters (e.g., !, @, #, etc.).")
        if length < 12:
            print("- Make your password longer (12+ characters recommended).")
        if has_repeating_number_patterns(password):
            print("- Avoid repeating number sequences (e.g., 123123, 1111).")
        if has_common_number_sequences(password):
            print("- Avoid common number patterns (e.g., 123, 9876).")


# --- Entry point ---
if __name__ == "__main__":
    try:
        password = input("Enter a password to check: ")
        check_password_strength(password)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

