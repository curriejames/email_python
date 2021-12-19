import smtplib  
conn =smtplib.SMTP('smtp-mail.outlook.com',587)
print('hello')  
type(conn)
try:  
    conn.ehlo()  
    conn.starttls()  
    conn.login('Dummysender@hotmail.com','Jennett1985')  
    conn.sendmail('Dummysender@hotmail.com','Dummyrecipient@gmail.com','Subject:Subject line\n\nI like boots and turkey bacon')  
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    conn.quit()