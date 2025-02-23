import requests

# Replace this with your actual Discord webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1343185650991759360/mElhPGFJHhSL0lgIViip_1qY_IQXJZlenkjsnKVX3pwi8SlPu7z_3CU2jydzseEZEUrW"

def send_webhook_notification(request_id, output_data):
    """Send a webhook notification to Discord when processing is completed."""
    
    # Formatting message for Discord
    message = f"✅ **Image Processing Completed!**\n**Request ID:** {request_id}\n"
    
    # Add processed image URLs to the message
    for product in output_data:
        message += f"**Product:** {product['product_name']}\n"
        for url in product["output_urls"]:
            message += f"📷 Processed Image: {url}\n"
    
    payload = {
        "content": message  # Discord webhook expects "content"
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
        if response.status_code == 204:  # 204 = Success (No Content)
            print(f"✅ Webhook sent successfully for request ID: {request_id}")
        else:
            print(f"❌ Webhook failed: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"❌ Error sending webhook: {e}")
