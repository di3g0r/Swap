import smtplib, ssl

port = 465  # For SSL
password = "your password"

sender_email = "intercambioderegalos55@gmail.com"
receiver_email = "reciever@mail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Correo enviado!")


