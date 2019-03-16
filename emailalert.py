def email_alert(symbol, currval, currtime, upper_val, lower_val):

	import smtplib
	from datetime import datetime, timedelta
	from email.message import EmailMessage
	from email.headerregistry import Address
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	port = 465  # For SSLc
	msg = MIMEMultipart()
	fromaddr = "tradingviewalert92@gmail.com"
	address_list = ["connor.winemiller@gmail.com", "alexa94@vt.edu"]
	password = 'TradingviewAlerts9294'


	for toaddr in address_list:
		msg['From'] = fromaddr
		msg['To'] = toaddr
		body = "At {currET} ET ({currtime} UTC):\n\nCurrent value is: {currval}\nUpper target is: {upperval}\nLower target is: {lowerval}".format(currET=(currtime-timedelta(hours=4)).strftime("%c"), currtime=(currtime).strftime("%c"), currval=str(currval), upperval=str(upper_val), lowerval=str(lower_val))
		msg.attach(MIMEText(body, 'plain'))


		if currval > upper_val:
			msg['Subject'] = symbol.upper() + " is ABOVE target price line"

		else:
			msg['Subject'] = symbol.upper() + " is BELOW target price line"


		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login('tradingviewalert92', password)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
	return None



