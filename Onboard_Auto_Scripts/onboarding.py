import csv
import os
from datetime import datetime

# ================================
# IT Onboarding Automation Tool
# Built by: Minh Tuan Nguyen
# Description: Automates AD user 
# onboarding from CSV input
# ================================

def read_employees(filename):
    """Read employee data from CSV file"""
    if error_check(filename):
        exit()
    
    employees = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    
    print(f"✓ Successfully read {len(employees)} employees from {filename}")
    return employees

def generate_username(firstname,lastname,existing_username):
    base_username=(firstname[0]+lastname).lower()
    
    username = base_username
    counter = 1
    while username in existing_username:
        username = f"{base_username}{counter}"
        counter += 1
    existing_username.add(username)
    return username


def generate_email(username, domain="Siemens.com"):
    return f"{username}@{domain}"

def generate_output_csv(employees_data,filename ="onboarding_output.csv"):
    fieldnames =[ 'Username',
                'Email',
                'Department', 
                'FirstName',
                'LastName',
                'Department',
                'StartDate',
                'TempPassword',
                'Status'
              ]
    
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees_data)

def load_existing_users(filename="existing_users.json"):
    import json
    if not os.path.exists(filename):
        return set()
    with open(filename, 'r') as file:
        data = json.load(file)
        print(f"✓ Loaded {len(data['usernames'])} existing users from database")
        return set(data['usernames'])
    
def save_existing_users(usernames, filename="existing_users.json"):
    import json
    with open(filename, 'w') as file:
        json.dump({'usernames': list(usernames)}, file, indent=4)
    
    print(f"✓ Database updated — {len(usernames)} total users saved")

def error_check(filename):
    if not os.path.exists(filename):
        print(f"✗ File not exist - please check to see if they exist: {filename}")
        exit()

############################################ Main Scripts

#read input and generate 
employees = read_employees('employees.csv')
existing_usernames = load_existing_users()
processed_employees = []

for emp in employees:
    username = generate_username(emp['FirstName'], emp['LastName'], existing_usernames)
    email = generate_email(username)
    processed_emp = {
        'Username': username,
        'Email': email,
        'Department': emp['Department'],
        'FirstName': emp['FirstName'],
        'LastName': emp['LastName'],
        'StartDate': emp['StartDate'],
        'TempPassword': 'WelcomeSiemens2026',
        'Status': 'Ready'
    }
    processed_employees.append(processed_emp)

#generate output
generate_output_csv(processed_employees)
#add the new user names back to database 
save_existing_users(existing_usernames)


#output test 
print()
print("=" * 45)
print("         ONBOARDING SUMMARY")
print("=" * 45)
print(f"  Output file               : onboarding_output.csv")
print(f"  Completed at              : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 45)
