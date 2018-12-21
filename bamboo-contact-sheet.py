from PyBambooHR import PyBambooHR
import sys

if len(sys.argv) < 2:
    print("ERROR: Bamboo HR API key not specified.")
    quit()

bamboo = PyBambooHR.PyBambooHR(subdomain='infinityworks', api_key=sys.argv[1])

print("Getting employee directory...")

employees = bamboo.get_employee_directory()

#Sort the list alphabetically on lastName
employees = sorted(employees, key=lambda d: d["lastName"])

#for employee in employees:
#    if employee["location"] == 'Manchester':
#        print("{} {}, {}, {}, {}".format(employee["firstName"], employee["lastName"], employee["jobTitle"], employee["department"], employee["photoUrl"]))

#print()

print("Creating contact sheet...")

with open('output.html', 'w') as outfile:
    with open("template.html") as infile:
        for line in infile:
            if "<!--content-->" in line:
                for employee in employees:
                    if employee["location"] == 'Manchester':
                        outfile.write('<div class="employee"><div class="photo"><img src="{}"/></div><div class="info"><div class="name">{} {}</div><div class="title">{}</div><div class="team">{}</div></div></div>'.format(employee["photoUrl"], employee["firstName"], employee["lastName"], employee["jobTitle"], employee["department"]))
            else:
                outfile.write(line)

print ("Done")