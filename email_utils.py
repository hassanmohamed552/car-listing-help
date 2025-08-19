import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import json
import os

# Load environment variables
load_dotenv()
smtp_email = os.getenv("SMTP_EMAIL")
smtp_password = os.getenv("SMTP_PASSWORD")

#create send email function
def send_email(json_data: dict, image_path: str, recipient: str):
    msg = EmailMessage()
    msg["Subject"] = "Car Listing Submission"
    msg["From"] = smtp_email
    msg["To"] = recipient
    msg.set_content("Attached is the car listing JSON and image.")

    msg.add_attachment(
        json.dumps(json_data, indent=2).encode("utf-8"),
        maintype="application",
        subtype="json",
        filename="car_data.json"
    )

    with open(image_path, "rb") as img:
        msg.add_attachment(img.read(), maintype="image", subtype="jpeg", filename="car_image.jpg")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(smtp_email, smtp_password)
        server.send_message(msg)
