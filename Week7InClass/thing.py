student_id = "2025-CS-0342"
year = student_id[0:4]
print(f"Year: {year}")

course_code = "CS1300-001"
if course_code.startswith("CS"):
    print("Computer Science course")
    
products = ["laptop", "tablet", "smartphone", "desktop"]
print(products)
products = products + ["headphones"]
print(products)
products = products[:3] + ["webcam"] + products[3:]
print(products)
removed_item = products.pop(2)
print(products)

replaced_item = products[1]
products[1] = "smartwatch"
print(f"Replaced: {replaced_item} with {products[1]}")

print(f"Slice of products: {products[3:6]}")

#print total products in stock  
print(f"Total products in stock: {len(products)}")