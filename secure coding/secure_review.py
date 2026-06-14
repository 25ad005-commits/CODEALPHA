# secure_review.py

print("SECURE CODING REVIEW TOOL")
print("-" * 30)

filename = input("Enter Python file name to review: ")

try:
    with open(filename, "r") as file:
        code = file.read()

    print("\nSecurity Review Report")
    print("-" * 30)

    issues = 0

    if "eval(" in code:
        print("[WARNING] Use of eval() detected.")
        issues += 1

    if "exec(" in code:
        print("[WARNING] Use of exec() detected.")
        issues += 1

    if "password =" in code or "password=" in code:
        print("[WARNING] Hardcoded password found.")
        issues += 1

    if "SELECT" in code and "+" in code:
        print("[WARNING] Possible SQL Injection risk.")
        issues += 1

    if issues == 0:
        print("[OK] No common security issues found.")

    print("\nRecommendations:")
    print("- Avoid eval() and exec().")
    print("- Do not hardcode passwords.")
    print("- Use parameterized SQL queries.")
    print("- Validate user input.")
    print("- Follow secure coding practices.")

except FileNotFoundError:
    print("File not found.")