    #!/usr/bin/env python
    import  smtplib
     
     
    def send_mail(email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
     
    send_mail("mymail@gmail.com", "mypass123", "TEST1")
