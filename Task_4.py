import re

def passwordValidator(password):
    try:
        if re.fullmatch(r"[a-zA-Z]+", password):
            return f"0 -> '{password}' is a very weak password !, it contains only letters"
        elif re.fullmatch(r"[0-9]+",password):
            return f"1 ->'{password}' is a weak password !, it contains only numbers"
        elif re.fullmatch(r"[\d]+[\w]+",password):
            return  f"2 -> '{password}' is a strong password !."
        elif re.fullmatch(r"[\d\w\D\W]+",password):
            return f"3 -> '{password}' is a very strong password"
    except:
        return f"'{password}' is invalid"

