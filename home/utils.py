import smtplib
from email.mime.text import MIMEText
def sending_email(body,email_to):
    subject = "tieu de email"
    email_from = "dinhthai160@gmail.com"

    message = MIMEText(body)
    message["subject"] = subject
    message["email_from"] = email_from
    message["email_to_list"] = email_to
    #khoi tao ket noi
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    #login
    smtp_login_email, smtp_login_password = "dinhthai160@gmail.com","ykpwafmpdnkvmmte"
    server.login(smtp_login_email,smtp_login_password)
    #send email
    server.sendmail(email_from,email_to,message.as_string())
    #exxit
    server.quit()
    print("send success")

    
    
    