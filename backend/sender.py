import smtplib, ssl, os

# Vars
PORT = 587  # For SSL
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASS = os.getenv("SENDER_PASS")

def send_emails_to_sellers(orders: dict[str, list], orderID: int):
    with smtplib.SMTP("smtp-mail.outlook.com", PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASS)
        
        for seller_email, items in orders.items():
            msg = f"New Order!! ID: {orderID}\n\n"
            for idx, product in enumerate(items):
                msg += f"Item {idx + 1} ==> Product ID: {product["id"]} - Name: {product["product name"]} - Quantity: {product["quantity"]}\n"
                
            server.sendmail(SENDER_EMAIL, seller_email, msg)    
