import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

sender_email = "abasitmarkting181@gmail.com"
# receiver_email = "recipient@example.com"
app_password = "vktf qexa prpx udvt"

# Load the CSV into a DataFrame
leads = pd.read_csv('output.csv')

leads["COMPANY WEBSITE"] = leads["COMPANY WEBSITE"].fillna('Unknown')

# View the first 5 rows
# print(df.columns)
# print(df["COMPANY NAME"])

# with_website_template = """
# Hi {first_name} {last_name},
#
# I hope you're doing well.
#
# I recently came across **{company_name}** and took some time to review your website. I was impressed by your business and the services you offer, but I also noticed a few opportunities where your website could be optimized to better support your growth.
#
# I specialize in **modern website development and optimization**, helping businesses improve their online presence through faster performance, better user experience, and more effective designs that convert visitors into customers.
#
# From my initial review, I identified a few areas where your website could potentially be improved, such as:
#
# Enhancing design and overall professionalism
# Improving loading speed and mobile responsiveness
# IOptimizing user experience and navigation
# * Increasing trust and conversion potential
#
# I’d be happy to share a few personalized suggestions and discuss how we could help **{company_name}** strengthen its online presence.
#
# Would you be available for a quick chat sometime this week?
#
# Best regards,
# Abdul Basit
# Nirvex Digital
# """


def generate_msg(lead):
    if lead._5 != "Unknown":
        with_website_template = f"""
        Hi {lead._2},

        I hope you're doing well.

        I recently came across {lead._4} and took a look at your website. Your business has strong potential, but I noticed a few areas where the website experience and overall presentation could be improved to better attract and convert customers.

        I’m reaching out on behalf of Nirvex Digital, where we specialize in modern website development and optimization. We help businesses improve their online presence through fast, professional, and user-friendly websites designed to build trust and generate more customers.
        
        I already have a few ideas that could help strengthen your online presence, and I’d be happy to share them with you. Would you be available for a quick conversation sometime this week?

        Best regards,
        Abdul Basit
        Nirvex Digital
        """
        return with_website_template
    else:
        without_website_template = f"""
        Hi {lead._2},

        I hope you're doing well.

        I recently came across {lead._4} and noticed that your business may not currently have a website. In today’s market, a professional website can help businesses build trust, attract more customers, and create a stronger online presence.
        
        I’m reaching out on behalf of Nirvex Digital, where we specialize in modern website development and optimization. We help businesses improve their online presence through fast, professional, and user-friendly websites designed to build trust and generate more customers.
        
        I’d love to discuss how a website could help {lead._4} grow and bring in more opportunities. Would you be open to a quick chat sometime this week?

        Best regards,
        Abdul Basit
        Nirvex Digital
        """
        return without_website_template


for lead in leads.itertuples():
    receiver_email = lead.EMAIL
    body = generate_msg(lead)

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Quick question about {lead._4}’s online presence"

    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail's SMTP server using SSL (Port 465)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

