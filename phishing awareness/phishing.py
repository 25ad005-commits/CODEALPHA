# phishing.py

print("PHISHING AWARENESS TRAINING")
print("-" * 35)

print("\nWhat is Phishing?")
print("Phishing is a cyber attack used to steal personal information.")

print("\nSigns of Phishing Emails:")
print("1. Unknown sender")
print("2. Urgent messages")
print("3. Suspicious links")
print("4. Requests for passwords")

print("\nFake Website Indicators:")
print("1. Incorrect URL")
print("2. No HTTPS")
print("3. Poor design or spelling mistakes")

print("\nSocial Engineering Tactics:")
print("- Impersonation")
print("- Fear and urgency")
print("- Fake rewards")

print("\nSafety Tips:")
print("- Verify sender identity")
print("- Avoid suspicious links")
print("- Use strong passwords")
print("- Enable Two-Factor Authentication")

print("\nQUIZ")

score = 0

if input("1. Click links from unknown emails? (yes/no): ").lower() == "no":
    score += 1

if input("2. Is HTTPS safer than HTTP? (yes/no): ").lower() == "yes":
    score += 1

if input("3. Share passwords through email? (yes/no): ").lower() == "no":
    score += 1

print("\nYour Score:", score, "/ 3")

if score == 3:
    print("Excellent! You are phishing aware.")
elif score == 2:
    print("Good! Keep learning.")
else:
    print("Review phishing safety practices.")