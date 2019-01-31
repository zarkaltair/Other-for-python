import smtplib
import ssl


try:
    port = 465
    smtp_server = 'smtp.gmail.com'
    sender_email = '...'
    sender_password = '...'
    receiver_email = '...'
    message = '''
    Hello world!!!
    '''

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, message)

except smtplib.SMTPAuthenticationError:
    print('Auth error!\nActive "less secure app access" in Gmail')