day1_visitors = {'Alice', 'Bob', 'Charlie'}
day2_visitors = {'Bob', 'David', 'Eve'}

union_result = day1_visitors | day2_visitors
print("Union using | :", union_result)  

union_result_method = day1_visitors.union(day2_visitors)
print("Union using union() method :", union_result_method)  



