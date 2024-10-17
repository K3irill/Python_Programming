from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from mail import EMAIL,EMAIL_TEST, PASSWORD 

# help(smtplib)
msg = MIMEMultipart()




message = 'It\'s important for you!'
password = PASSWORD
msg['From'] = EMAIL
msg['To'] =  EMAIL_TEST
msg['Subject'] = "Subscription"

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(msg['From'], PASSWORD)


print(msg)

server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("successfully sent email to %s:" % (msg['To']))