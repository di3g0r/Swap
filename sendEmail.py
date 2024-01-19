import smtplib, ssl

def sendMail(receiver: str,subject: str, message: str):
    port = 465  # For SSL
    sender_email = "intercambioderegalos55@gmail.com"
    password = "qhrzvukilxzyhnqe"
    receiver_email = receiver
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Construct the email headers
    email_headers = f"Subject: {subject}\nFrom: {sender_email}\nTo: {receiver_email}\n\n"

    # Concatenate the headers and the message
    full_message = email_headers + message

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, full_message)
        print("Correo enviado!")