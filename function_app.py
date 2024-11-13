import logging
import azure.functions as func
import pandas as pd
import os
# Modules import
from date_variables import *    # Day/week variables
# Mailing import
import smtplib
from email.mime.text import MIMEText
from pretty_html_table import build_table

################## Classes ##################
class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password, recipient_email):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
    # Modified to work with Pandas DataFrames
    def send_email(self, subject, message, dataframe: pd.DataFrame):
        try:
            # Convert the PySpark DataFrame to an HTML table using pretty-html-table
            html_table = build_table(dataframe, 'blue_light')
            message_with_table = f"{message}\n\n{html_table}"

            # Create a connection to the SMTP server
            smtp_server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtp_server.starttls()
            smtp_server.login(self.sender_email, self.sender_password)

            # Create the email message
            msg = MIMEText(message_with_table, 'html')  # Set the content type to 'html'
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = subject

            # Send the email
            smtp_server.sendmail(self.sender_email, self.recipient_email, msg.as_string())

            # Quit the SMTP server
            smtp_server.quit()

            print("Email sent successfully!")

        except Exception as e:
            print("An error occurred while sending the email:", str(e))
        

################## Functions ##################
def helper_function():
    # Additional helper logic here
    logging.info('Helper function executed')

################## Timer Trigger ##################
app = func.FunctionApp()

# @app.schedule(schedule="0 0 * * * *", arg_name="myTimer", run_on_startup=True,
#               use_monitor=False)          # Triggered every day at midnight

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    # TODO: send mail   
    # Example DataFrame creation using Pandas
    data = {"Name": ["John", "Anna", "Mike"], "Age": [28, 23, 35]}
    test_df = pd.DataFrame(data) 

    sender = "supp.pub.cz@gmail.com"
    # password = dbutils.secrets.get(scope = "key-vault-secrets", key = "MailingSupportPublicisGoogleAppPass")
    password = os.getenv("MAILING_SUPPORT_PUBLICIS_GOOGLE_APP_PASS")
    recipient = "ondrej.mach@publicisgroupe.cz"
    # recipient = "michal.svoboda@publicisgroupe.cz"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587 
    subject_future = f"Budoucí kampaně startující v následujícím týdnu č.{next_week_num}" 
    subject_past = f"Kampaně, které startovaly v minulém týdnu č.{last_week_num}"
    test_message = "Hello, this is a test email sent from Python!"

    email_sender_last_week = EmailSender(smtp_server, smtp_port, sender, password, recipient)
    email_sender_last_week.send_email(subject_past, test_message, test_df)

    # TODO: Connect to blob

    # TODO: Connect to database

    logging.info('Python timer trigger function executed.\n TODAY IS WEEK NUMBER: ', week_num)