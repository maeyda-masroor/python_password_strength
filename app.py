import streamlit as st

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_+=<>?/[]{},." for c in password)

    if length < 6:
        return "Very Weak 🔴"
    elif length < 8:
        return "Weak 🟠"
    elif length >= 8:
        if has_upper and has_lower and has_digit and has_special:
            return "Very Strong ✅"
        elif has_upper and has_lower and (has_digit or has_special):
            return "Strong 🟢"
        elif has_upper or has_lower or has_digit or has_special:
            return "Moderate 🟡"
    
    return "Weak 🟠"  # Default case

st.title("Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    strength = check_password_strength(password)
    st.write(f"Password Strength: **{strength}**")
