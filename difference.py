platform1_users = {1001, 1002, 1003, 1004, 1005}
platform2_users = {1003, 1004, 1005, 1006, 1007}

platform1_users = {1001, 1002, 1003, 1004, 1005}
platform2_users = {1003, 1004, 1005, 1006, 1007}

difference_result = platform1_users - platform2_users
print(difference_result)

second_difference_result = platform2_users - platform1_users
print(second_difference_result)

symmetric_difference = platform1_users ^ platform2_users
print(symmetric_difference)