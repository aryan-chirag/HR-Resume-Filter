# Resume Analyzer Project

#JOB DATA

jobs = {
    "Data Scientist": ["Python", "Machine Learning", "Statistics", "SQL"],
    "Data Analyst": ["Python", "Excel", "SQL", "Visualization"],
    "ML Engineer": ["Python", "Machine Learning", "TensorFlow"],
    "AI Engineer": ["Python", "Deep Learning", "NLP"],

    "Web Developer": ["HTML", "CSS", "JavaScript", "React"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript"],
    "Backend Developer": ["Node.js", "Databases", "APIs"],
    "Full Stack Developer": ["HTML", "CSS", "JavaScript", "Node.js"],

    "Software Engineer": ["Java", "DSA", "OOP"],

    "Mobile App Developer": ["Java", "Kotlin", "Android"],

    "Cloud Engineer": ["AWS", "Cloud", "DevOps"],
    "DevOps Engineer": ["Docker", "Kubernetes", "CI/CD"],

    "Cyber Security Analyst": ["Networking", "Security", "Linux"],

    "Database Administrator": ["SQL", "Database Management"],
    "Data Engineer": ["Python", "SQL", "ETL"],

    "UI/UX Designer": ["Figma", "Design", "User Experience"],

    "QA Engineer": ["Testing", "Automation"],

    "Blockchain Developer": ["Blockchain", "Solidity"],

    "IoT Developer": ["C", "Sensors", "IoT"]
}

#LOWERCASE VERSION FOR MATCHING

jobs_lower = {}
for job in jobs:
    jobs_lower[job.lower()] = [s.lower() for s in jobs[job]]

#USER INPUT

skills = input("Enter your skills (comma separated): ").lower().split(",")
skills = [s.strip() for s in skills]

cgpa = float(input("Enter your CGPA: "))
projects = int(input("How many projects you have done: "))
intern = input("Do you have internship experience (yes/no): ").lower().strip()

print("\nAvailable roles:")
for j in jobs:
    print("-", j)

role = input("\nEnter role you want: ").lower().strip()

if role not in jobs_lower:
    print("Invalid role, run again.")
    exit()

#MATCHING

req = jobs_lower[role]

matched = []
for s in skills:
    if s in req:
        matched.append(s)

missing = []
for s in req:
    if s not in skills:
        missing.append(s)

#SCORING

skill_marks = (len(matched) / len(req)) * 50

if cgpa >= 9:
    cgpa_marks = 20
elif cgpa >= 8:
    cgpa_marks = 15
else:
    cgpa_marks = 10

proj_marks = min(projects * 3, 15)

intern_marks = 15 if intern == "yes" else 0

total = skill_marks + cgpa_marks + proj_marks + intern_marks

#RESULT

if total >= 80:
    level = "Strong"
elif total >= 60:
    level = "Average"
else:
    level = "Needs Improvement"

result = "Selected" if total >= 60 else "Not Selected"

#FIND BETTER ROLE

best_job = role
best_count = len(matched)

for j in jobs_lower:
    count = 0
    for s in skills:
        if s in jobs_lower[j]:
            count += 1

    if count > best_count:
        best_count = count
        best_job = j

#OUTPUT

print("\n----- RESULT -----")

real_role = [j for j in jobs if j.lower() == role][0]

print("Role:", real_role)
print("Your Score:", round(total, 2), "/100")
print("Skill Match:", round((len(matched)/len(req))*100, 2), "%")
print("Level:", level)
print("Final Result:", result)

print("\nScore Details:")
print("Skills:", round(skill_marks, 2))
print("CGPA:", cgpa_marks)
print("Projects:", proj_marks)
print("Internship:", intern_marks)

real_skills = jobs[real_role]
missing_display = []

for s in real_skills:
    if s.lower() in missing:
        missing_display.append(s)

print("\nMissing Skills:")
if missing_display:
    print(", ".join(missing_display))
else:
    print("None")

#SUGGESTIONS

print("\nSuggestions:")

if missing_display:
    print("- Try to learn:", ", ".join(missing_display))

if cgpa < 8:
    print("- Try improving your CGPA")

if projects < 3:
    print("- Do more projects")

if intern == "no":
    print("- Try getting internship experience")

#BETTER ROLE 

if best_job != role:
    better = [j for j in jobs if j.lower() == best_job][0]
    print("\nYou may also try:", better)
