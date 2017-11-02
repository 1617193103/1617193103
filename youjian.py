import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '15251684301@126.com'
msg['to'] = '1139299516@qq.com'
msg['subject'] = '网易新闻'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

#smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com', '25')
smtp.login('15251684301@126.com', 'si1139299516')
smtp.sendmail('15251684301@126.com', '1139299516@qq.com', str(msg))
smtp.quit()