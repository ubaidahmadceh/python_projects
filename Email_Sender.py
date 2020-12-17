import smtplib

to = input("Enter recepient Email : ")

content = input("Type Your Message : ")

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.login('senderemail@gmail.com', '1234')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()


sendemail(to, content)
