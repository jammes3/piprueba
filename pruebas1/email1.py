import smtplib

message = "hola este es un mensaje con python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('jammespruebas@gmail.com', 'Hamburgesadenaranja.')

server.sendmail('jammesduran3@gmail.com', message)

server.quit()

print("correo enviado")
