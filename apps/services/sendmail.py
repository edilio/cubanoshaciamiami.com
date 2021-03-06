def createhtmlmail (html, text, sender, recipient, subject):
      	"""Create a mime-message that will render HTML in popular
	   MUAs, text in better ones"""
	import MimeWriter
	import mimetools
	import cStringIO

	out = cStringIO.StringIO() # output buffer for our message
	htmlin = cStringIO.StringIO(html)
 	txtin = cStringIO.StringIO(text)

	writer = MimeWriter.MimeWriter(out)
	#
	# set up some basic headers... we put subject here
	# because smtplib.sendmail expects it to be in the
	# message body
	#
	writer.addheader("Subject", subject)
	writer.addheader("MIME-Version", "1.0")
	writer.addheader("From", sender)
	writer.addheader("Reply-To", sender)
	writer.addheader("To", recipient)

	#
	# start the multipart section of the message
	# multipart/alternative seems to work better
	# on some MUAs than multipart/mixed
	#
	writer.startmultipartbody("alternative")
	writer.flushheaders()
	#
	# the plain text section
	#
	subpart = writer.nextpart()
	subpart.addheader("Content-Transfer-Encoding", "quoted-printable")
	pout = subpart.startbody("text/plain", [("charset", 'us-ascii')])
	mimetools.encode(txtin, pout, 'quoted-printable')
	txtin.close()
	#
	# start the html subpart of the message
	#
	subpart = writer.nextpart()
	subpart.addheader("Content-Transfer-Encoding", "quoted-printable")
	#
	# returns us a file-ish object we can write to
	#
	pout = subpart.startbody("text/html", [("charset", 'us-ascii')])
	mimetools.encode(htmlin, pout, 'quoted-printable')
	htmlin.close()
	#
	# Now that we're done, close our writer and
	# return the message body
	#
	writer.lastpart()
	msg = out.getvalue()
	out.close()
	#print msg
	return msg

def tellafriend(friendname,friendmail,myname,mymail,msg,copy): #if copy send a copy to my email
        sendhtmlmail(friendname,friendmail,myname,mymail,msg,copy)

def sendhtmlmail(to_name,to_mail,from_name,from_mail,msg, copy):
    import smtplib
    html = msg.replace("store.speedycomputers.us",'<a href="http://store.speedycomputers.us"> SpeedyComputers.us</a>')
    text = msg
    subject = "Recomendation! Cheack it out!"
    sender = '%s <%s>' %(from_name,from_mail)
    recipient = '%s <%s>' %(to_name,to_mail)
    message = createhtmlmail(html, text, "edilio@c4telecom.com", recipient, subject)
    server = smtplib.SMTP("mail.c4telecom.com")
    try:
        server.login("edilio","camilita")
        server.sendmail("edilio@c4telecom.com", recipient, message)
        if copy:
            server.sendmail("edilio@c4telecom.com", sender, message)
    finally:
        server.quit()

##print "comenzo"
##tellafriend('edilio','edilio73@gmail.com','Edilio Gallardo','store@magmail.speedycomputers.us',"""I thought you might be interested in this web site for computer services.
##store.speedycomputers.us""",False)
##print "termino"

