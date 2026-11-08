def validate_password(password):
    if len(password) < 8:
        return "Құпиясөз кемінде 8 символдан тұруы керек"
    if not any(ch.isdigit() for ch in password):
        return "Құпиясөзде кемінде бір цифр болуы керек"
    if not any(ch.isupper() for ch in password):
        return "Құпиясөзде бас әріп болуы керек"
    return "Құпиясөз сенімді"

print(validate_password("abc"))
print(validate_password("abcdefgh1"))
print(validate_password("Abcdefgh1"))