engineering_dept = {"Alice" : "Manager", "Bob": "Jr. Engineer", "Charlie" : "Sr. Engineer", 
"David": "Sr. Manager", "Emma":"Tech Lead", "Frank": "Jr. Engineer"}

employee_tenure = {
    "Alice": 5,
    "Bob": 2,
    "Charlie": 4,
    "David": 4,
    "Emma": 6,
    "Frank": 2,
    "Grace": 4,
    "Harry": 5,
    "Ivy": 3,
    "Jack": 1
}

experienced_managers = {(employee, role) for (employee, role) in engineering_dept.items()
	if employee_tenure[employee] >= 4 if "Manager" in role}
print(experienced_managers)