"""
    [DESCRIPTION]: This is sample #12 for python.

    This is sending an email in python. This email will only be sent
    to one recipient.

    [IMPORTANT]: You must turn off less secure apps on your Google account.
    
    If we do not do this the email will NOT be sent !
    [SOURCE / Turn Off Less secure apps]
        https://support.google.com/accounts/answer/6010255?hl=en
"""
__title__ = "Sample Twelve."
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"

# Simple mail transfer protocol.
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

class ConsoleEmailer:
    """
    Name        :   ConsoleEmailer
    Purpose     :   This class will be filled of methods that correspond
                    to sending an email through a console application.
    """

    def __init__(self, from_address, to_address, subject, message, host, port):
        self.from_address = from_address
        self.to_address = to_address
        self.subject = subject
        self.message = message
        self.host = host
        self.port = port

    def configure_message(self):
        """ [This will configure the message for the email] """
        py_email_message = MIMEMultipart()
        py_email_message["From"] = self.from_address
        py_email_message["To"] = self.to_address
        py_email_message["Subject"] = "This is a email sent through the console using Python 3."
        py_email_message.attach(MIMEText(self.message, "html", "utf-8"))
        msg = py_email_message.as_string()
        return msg

    def configure_server(self, password):
        """ [This configures the server.] """
        # Put the SMPT connection into TLS mode (Transport Layer Security).
        server = SMTP(self.host, self.port)
        server.starttls()
        
        server.login(self.from_address, password)

        _configured_message = self.configure_message()
        server.sendmail(self.from_address, self.to_address, _configured_message)
        server.quit()

if __name__ == "__main__":

    # Create an email object to access the methods.
    _from_address = ""
    _to_address = ""
    _subject = "Python 3 | Console Email Application"
    _gmail_host = "smtp.gmail.com"
    _port_number = 587

    gitHubLink = "https://github.com/BraidenGole"
    today = date.today()
    _message = """
               <h1>Hi {0} this is just a test email written using python 3.</h1>
               <br>
               <h3>Visit my GitHub page at <a href="{1}">Braiden's GitHub Profile</a></h3><br>
               <small><strong>Date sent:</strong> {2}</small>
               """.format(_to_address, gitHubLink, today)

    # Instantiate an email object.
    email_1 = ConsoleEmailer(_from_address, _to_address, _subject, _message, _gmail_host, _port_number)

    _password = "<Password>"
    email_1.configure_server(_password)



