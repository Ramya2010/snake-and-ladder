import smtplib
s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='ramya20102000@gmail.com'
receiver='rahulhn2000@gmail.com'
msg="hey"
s.login(sender,'++11ramya')
s.sendmail('ramya20102000@gmail.com','rahulhn2000@gmail.com',msg)
print("message sent successfully")
s.quit()