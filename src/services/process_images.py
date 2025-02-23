import os
import requests
from io import BytesIO
from PIL import Image
from src.models.request_model import update_request_status
from src.services.webhook import send_webhook_notification  # ✅ Import webhook

# Folder to store processed images
OUTPUT_FOLDER = "uploads/processed"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def process_images(request_id, products):
    """Processes images in the background and sends a webhook when done."""
    processed_data = []

    for product in products:
        output_urls = []
        for img_url in product["input_urls"]:
            try:
                response = requests.get(img_url)
                if response.status_code == 200:
                    img = Image.open(BytesIO(response.content))
                    img = img.convert("RGB")

                    # Compress and save the image
                    output_filename = f"{OUTPUT_FOLDER}/{os.path.basename(img_url)}"
                    img.save(output_filename, "JPEG", quality=50)

                    output_urls.append(output_filename)

            except Exception as e:
                print(f"❌ Error processing image {img_url}: {e}")

        processed_data.append({
            "serial_number": product["serial_number"],
            "product_name": product["product_name"],
            "input_urls": product["input_urls"],
            "output_urls": output_urls
        })

    # ✅ Update request status in MongoDB
    update_request_status(request_id, "COMPLETED", processed_data)

    # ✅ Send Discord webhook notification
    send_webhook_notification(request_id, processed_data)

    print(f"✅ Image processing completed for request ID: {request_id}")
