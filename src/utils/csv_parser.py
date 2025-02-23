import pandas as pd

def parse_csv(file):
    """Parse and validate the uploaded CSV file."""
    df = pd.read_csv(file.file)

    required_columns = ["Serial Number", "Product Name", "Input Image Urls"]
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Invalid CSV format: Missing required columns.")

    products = []
    for _, row in df.iterrows():
        input_images = row["Input Image Urls"].split(", ")
        products.append({
            "serial_number": row["Serial Number"],
            "product_name": row["Product Name"],
            "input_urls": input_images,
            "output_urls": []
        })
    
    return products
