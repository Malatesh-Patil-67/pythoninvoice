


import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def DailyTableLoadreport_fn(recipientsList, sender, pwd):
    try:
        fromaddr = sender
        recipients = recipientsList
        msg: object = MIMEMultipart()
        msg['From'] = ' Fragma BFLDL Project Reporter ' + fromaddr
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = "Fragma DataLake Finnacle Load Report"
        body = ""
        msg.attach(MIMEText(body, 'plain'))

        filename = 'Finnacle_Daily_Load_Report_' + str(epoch) + '.xlsx'
        attachment_1 = '/tmp/Finnacle_Daily_Load_Report_Failed_' + str(epoch) + '.xlsx'
        attachment_2 = '/tmp/Finnacle_Daily_Load_Report_Succeeded_' + str(epoch) + '.xlsx'
        attachment_3 = '/tmp/Finnacle_Daily_Load_Report_InProgress_' + str(epoch) + '.xlsx'
        # attachment_4 = '/tmp/Finnacle_Daily_Load_Report_'+str(epoch)+'.xlsx'
        files = []
        files.append(attachment_1)
        files.append(attachment_2)
        files.append(attachment_3)
        # files.append(attachment_4)

        #     filename = 'Finnone_Daily_Load_Report_'+str(epoch)+'.xlsx'
        #     attachment = open('/tmp/Finnone_Daily_Load_Report_'+str(epoch)+'.xlsx', "rb")
        for file in files:
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(open(file, "rb").read())
            encoders.encode_base64(p)
            #       p.add_header('Content-Disposition', "attachment; filename= %s" % file)
            p.add_header('Content-Disposition', 'attachment; filename= "{0}"'.format(os.path.basename(file)))
            msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        #   s.login(fromaddr, "Fds@12345")
        s.login(fromaddr, pwd)
        text = msg.as_string()
        s.sendmail(fromaddr, recipients, text)
        s.quit()

        print("Report Sent")
        return False
    except Exception as e:
        print("An Exception occurred: " + str(e))
        return True
