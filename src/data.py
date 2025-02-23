csv_content = """Serial Number,Product Name,Input Image Urls
1,SKU1,https://via.placeholder.com/150, https://via.placeholder.com/200
2,SKU2,https://via.placeholder.com/250, https://via.placeholder.com/300
3,SKU3,https://via.placeholder.com/350, https://via.placeholder.com/400
"""

with open("sample.csv", "w") as file:
    file.write(csv_content)

print("✅ sample.csv created successfully!")
