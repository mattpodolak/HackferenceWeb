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
    return render_template('email-confirm.html', email_add = input)

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

    html = '''<!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml">

    <head>
    	<!-- Latest compiled and minified CSS -->
    	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    	<!-- custom css -->
    	<style>
    	.button {
    		background-color: white; 
    		border: 2px solid #FF3D81;
    		color: #FF3D81;
    		border-radius:20px;    
    		padding: 8px 32px;
    		text-align: center;
    		text-decoration: none;
    		display: inline-block;
    		font-size: 16px;
    	}

    	.maxlevel {
    		color: #FF3D81;
    	}

    	.between {
    		font-size: 24px;
    		color: #FF7F08;
    	}

    	#tablesetup {
    		display:block;
    		border-radius: 16px 55px;
    		border-collapse: collapse;
    		border-spacing: 4px;
    		padding: 20px;
    		max-width: 420px;
    		background: #FFFFFF;
    	}

    	#borderglow {
    		box-shadow: 0px 0px 2px #b3b3b3;
    		-webkit-box-shadow: 0px 0px 2px #FFFFFF;
    		-moz-box-shadow: 0px 0px 2px #FFFFFF;
    	}

    	h1 {
    		font-size: 14px;
    		color: #000000;
    	}

    	h2 {
    		font-size: 48px;
    		color: #FF7F08;
    		text-shadow: -1px 0 #000000,0 1px #000000,1px 0 #000000,0 -1px #000000;
    	}


    	h3 {
    		font-size: 24px;
    		color: #4d4e4f;
    	}

    	h4 {
    		font-size: 22px;
    		color: #4d4e4f;
    	}

    	h5 {
    		font-size: 14px;
    		color: #4d4e4f;
    	}

    	</style>
    </head>

    <body>

    	<!-- temp filler -->
    	<div>
    		<table>
    			<tr>
    				<td height="20"></td>
    			</tr>
    		</table>
    	</div>

    	<!-- email body -->
    	<div align="center">
    		<div id="tablesetup" style="border:2px solid #b3b3b3;" style="background:#FFFFFF;">
    			<center>
    				<table cellspace="0" cellpadding="0" align="center" width="380" bgcolor="#ffffff" style="background:#ffffff;max-width:100%">
    					<tbody style="background:#FFFFFF">

    						<!-- logo -->
    						<tr>
    							<td width="380" align="center">
    								<img src="https://image.ibb.co/gYP9V6/knowhow.png" style="max-width:180">
    							</td>
    						</tr>

    						<!-- title -->
    						<tr>
    							<td width="380" align="center">
    								<h2><b>KnowHow</b></h2>
    							</td>
    						</tr>

    						<!-- message & report button -->
    						<tr>
    							<td width="380" align="center">
    								<h4><b>Start up in 30 seconds.</b></h4>
    							</td>
    						</tr>
    						<tr>
    							<td height="24" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    						</tr>

    						<!-- creating and engaing -->
    						<tr>
    							<td id="borderglow" height="2" bgcolor="#b3b3b3" style="background:#b3b3b3"></td>
    						</tr>
    						<tr>
    							<td height="12" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    						</tr>
    						<td align="center">
    							<h3><b><span class="between">CREATE</span> AND <span class="between">ENGAGE</b></h3>
    						</td>
    						<tr>
    							<td width="380" align="center">
    								<h5><b>download and get started on your project</b></h5>
    							</td>
    						</tr>
    						<tr>
    							<td height="12" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    						</tr>
    						<tr>
    							<td width="380" align="center">
    								<img src="https://www.gstatic.com/android/market_images/web/play_prism_hlock_2x.png" width="220">
    							</td>
    						</tr>
    						<tr>
    							<td height="24" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    						</tr>

    						<!-- other offerings and packages -->
    						<tr>
    							<td id="borderglow" height="2" bgcolor="#b3b3b3" style="background:#b3b3b3"></td>
    						</tr>
    						<tr>
    							<td height="12" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    						</tr>
    						<td align="center">
    							<h3><b><span class="between">CULTIVATE</span> YOUR <span class="between">NETWORK</span></b></h3>
    						</td>
    						<tr>
    							<td width="380" align="center">
    								<h5><b>seamless integration with social media</b></h5>
    							</td>
    						</tr>
    						<tr>
    							<td height="12" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    						</tr>
    						<tr>
    							<td>
    								<table align="center" style="border-spacing:10px; max-width:100%">
    									<tr>
    										<td>
    											<img src="https://facebookbrand.com/wp-content/themes/fb-branding/prj-fb-branding/assets/images/fb-art.png" width="70">
    										</td>
    										<td width="30" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    										<td>
    											<img src="http://www.edigitalagency.com.au/wp-content/uploads/new-linkedin-logo-png-transparent-background.png" width="70">
    										</td>
    										<td width="30" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    										<td>
    											<img src="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png" width="70">
    										</td>
    									</tr>
    								</table>
    							<td>
    						</tr>
    						<tr>
    							<td height="24" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    						</tr>

    						<!-- logo bar -->
    						<tr>
    							<td id="borderglow" height="2" bgcolor="#b3b3b3" style="background:#b3b3b3"></td>
    						</tr>
    						<tr>
    							<td height="12" bgcolor="#ffffff" style="background:#FFFFFF"></td>
    						</tr>
    						<tr>
    							<td width="380" align="center">
    								<h1><p>KnowHow Support Team</p></h1>
    							</td>
    						</tr>
    						<tr>
    							<td>
    								<table align="center" style="border-spacing:10px; max-width:100%">
    									<tr>
    										<td>
    											<h1><p>sponsor_1</p></h1>
    										</td>
    										<td width="30"></td>
    										<td>
    											<h1><p>sponsor_2</p></h1>
    										</td>
    										<td width="30"></td>
    										<td>
    											<h1><p>sponsor_3</p></h1>
    										</td>
    									</tr>
    								</table>
    							<td>
    						</tr>

    						<!-- copyright -->
    						<tr>
    							<td width="380" align="center">
    								<p><h1><i>Copyright &copy; KnowHow</i></h1></p>
    							</td>
    						</tr>
    					</tbody>
    				</table>
    			</center>
    		</div>
    	</div>

    	<!-- temp filler -->
    	<div>
    		<table>
    			<tr>
    				<td height="20" bgcolor="#ffffff" style="background:#ffffff"></td>
    			</tr>
    		</table>
    	</div>
    </body>
    </html>'''
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