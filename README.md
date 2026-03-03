# IT-Onboard-Automation-Tool
A Python automation script that streamlines the IT onboarding  process for new employees. Designed to simulate real enterprise  Active Directory workflows used in corporate IT environments.

---------------------------------------------------------------------
Functionality

- It can read new employee data from a csv input file
- Auto-Generates active directory usernames (first name + last name)
- Auto generates company email addresses
- Detects and handles duplicate username automatically
- Exports a complete onboarding report to csv
- Generates an indiviual IT check list per employee
- Persists username history in a JSON database across multiple runs
---------------------------------------------------------------------
Project management

-this project was managed using Scrum methodology in Jira:
- Organized into Epics, Stories, and Tasks
- Worked in sprints with a defined backlog
- Documented in Confluence IT Knowledge Base
---------------------------------------------------------------------
Technology Used

- Python 3.13
- CSV module — employee data input and output
- JSON module — persistent username database
- OS and DateTime modules — file management and timestamps

---------------------------------------------------------------------
Future Improvements

- Integrate with JIRA REST API to auto-create onboarding tickets 
- Build GUI
- Connect this project to Active Directory using Python ldap3 module

Final results
<img width="2179" height="1181" alt="image" src="https://github.com/user-attachments/assets/3e7b1c9a-5bf0-44f1-8b36-37d266fddadd" />
