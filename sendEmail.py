import smtplib, ssl

def sendMail(receiver: str, message: str):
    port = 465  # For SSL
    sender_email = "intercambioderegalos55@gmail.com"
    password = "qhrzvukilxzyhnqe"
    receiver_email = receiver
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Correo enviado!")