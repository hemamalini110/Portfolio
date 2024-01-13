import smtplib ,ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "notequal110@gmail6.com"
    password = "cmlo boai jork tpwm"
    receiver = "notequal110@gmail.com"
    context = ssl.create_default_context()
    message = message
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

