from datetime import datetime
from zoneinfo import ZoneInfo

attendance = []

PH_TIMEZONE = ZoneInfo("Asia/Manila")

print("======================================")
print("           MAGANDANG arAU!")
print("    WELCOME TO ATTENDANCE SYSTEM")
print("======================================")

while True:
    print("\n--- STUDENT ATTENDANCE ---")

    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Full Name: ").strip()
    subject = input("Enter Subject: ").strip()

    if not student_id or not name or not subject:
        print("Please complete all information!")
        continue

    now = datetime.now(PH_TIMEZONE)
    today = now.strftime("%Y-%m-%d")

    duplicate = False

    for record in attendance:
        if (record["id"] == student_id
                and record["subject"].lower() == subject.lower()
                and record["date"] == today):
            duplicate = True
            break

    if duplicate:
        print("\nAttendance already recorded for this subject today!")
    else:
        attendance.append({
            "id": student_id,
            "name": name,
            "subject": subject,
            "date": today,
            "time": now.strftime("%I:%M:%S %p")
        })

        print("\n======================================")
        print("       ATTENDANCE SUCCESSFUL!")
        print("======================================")
        print("Student ID:", student_id)
        print("Name:", name)
        print("Subject:", subject)
        print("Date:", now.strftime("%B %d, %Y"))
        print("Philippine Time:", now.strftime("%I:%M:%S %p"))
        print("======================================")
        print("Thank you for attending!")

    again = input("\nNext student? (yes/no): ").strip().lower()

    if again != "yes":
        print("\nMAGANDANG arAU! Goodbye!")
        break
