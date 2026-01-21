enrollment_course_a = {'Alice', 'Sally', 'Robert', 'Terry'}
enrollment_course_b = {'Tony', 'Sarah', 'Rebecca', 'Alice'}

is_disjoint_result = enrollment_course_a.isdisjoint(enrollment_course_b)
print("Are the sets disjoint?", is_disjoint_result)

is_overlapping = len(enrollment_course_a & enrollment_course_b) > 0
print("Are the sets overlapping?", is_overlapping)

