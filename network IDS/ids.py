# ids.py

print("NETWORK INTRUSION DETECTION SYSTEM")
print("=" * 40)

threshold = 100

n = int(input("Enter number of network records to monitor: "))

print("\nEnter Network Details:")

for i in range(n):
    print(f"\nRecord {i+1}")

    ip = input("Enter IP Address: ")
    requests = int(input("Enter Number of Requests: "))

    print("\nAnalyzing Traffic...")

    if requests > threshold:
        print(f"IP Address : {ip}")
        print(f"Requests   : {requests}")
        print("ALERT: Suspicious Activity Detected!")
        print("Response: IP flagged for investigation.")
    else:
        print(f"IP Address : {ip}")
        print(f"Requests   : {requests}")
        print("Status: Normal Traffic")

print("\nMonitoring Completed.")