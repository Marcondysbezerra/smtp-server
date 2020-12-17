import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Configuração do servidor:
host = 'smtp.gmail.com'
port = 587
user = '<EMAIL>'
password = '<SENHA>'

server = smtplib.SMTP(host, port)

# Login no servidor:
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem:
mensage = 'Olá mundo!'
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = '<EMAIL DE DESTINO>'
email_msg['Subject'] = '<ASSUNTO DA MENSAGEM>'

email_msg.attach(MIMEText(mensage, 'plain'))

# Enviando a mensagem:
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()

