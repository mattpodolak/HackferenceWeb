from flask import Flask, render_template, request, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emailSubmit', methods=['POST'])
def emailSubmit():
    input = request.form['InputEmail']
    input = str(input)
    emailSend(input)
    print(input)
    #add email to database here
    return render_template('index.html')

#return render_template('index.html', key_1 = str(keys[0]), key_2 = str(keys[1]), key_3 = str(keys[2]), p_1 = str(summs[0]), p_2 = str(summs[1]), p_3 = str(summs[2]))

def emailSend(email_add):
    # default email
    me = "originalgomezzz@gmail.com"
    my_password = "Idontknow1337?"

    # target email
    you = email_add

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Alert"
    msg['From'] = me
    msg['To'] = you

    html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    # uncomment if interested in the actual smtp conversation
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

if __name__ == '__main__':
    app.run()