#!/usr/bin/env python

from __init__ import Message
from pdb import set_trace as debug
import sys
#Change this to be your name to recieve the test emails
testsubject = "lee@"  #lee@ is complete. snl.salk.edu gets filled in below.

#Below there is a test for sending authenticated email through
#smtp-auth. You'll need to fill in a valid SNL username and pwd
#otherwise, you'll get 'Authentication failure'

#============================================================#
print('Sending tests through smtp.snl.salk.edu')




    
#Test sending to a single recipient
m = Message()
m.To=testsubject + 'snl.salk.edu'
m.From=testsubject + 'salk.edu'
m.Body = 'This is a test.'
m.Subject='This is a test of single recipient'
print(m.Subject)
m.snlSend()

if len(sys.argv) == 1:

    #Test sending to a list of recipients

    m = Message()
    m.To=[testsubject + 'snl.salk.edu',testsubject + 'salk.edu']
    m.From=testsubject + 'salk.edu'
    m.Body = 'This is a test.'
    m.Subject='This is a test of list of recipients'
    print(m.Subject)
    m.snlSend()

    #Test sending to a list of recipients where one of the 
    #recipient addresses is malformed

    m = Message()
    m.To=['lee-snl.salk.edu',testsubject + 'snl.salk.edu']
    m.From=testsubject + 'salk.edu'
    m.Body = 'This is a test.'
    m.Subject='This is a test of list of recipients with malformed address'
    print(m.Subject)
    m.snlSend()
    
    #Test sending with no email address validation
    #Use this to send to a comma-separated To e.g.
    #m.To = "user@salk.edu, user1@salk.edu"
    #This way To recipients can see each other.

    m = Message()
    m.To='lee@snlsalk.edu, lee+1@snl.salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'This is a test.'
    m.Subject='This is a test of list of recipients with malformed address'
    print(m.Subject)
    m.snlSend(validateToAddresses=False)

    #Test sending Html body with a markdown plaintext version

    m = Message()
    m.To=testsubject + 'snl.salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Html = '<strong>This is a bold. </strong><br>This is not.'
    m.Subject='This is a test Html; There should be a markdown version in the plaintext slot.'
    print(m.Subject)
    m.snlSend()

    #Test sending Html body AND plaintext

    m = Message()
    m.To=testsubject + 'snl.salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'This is the plaintext version.'
    m.Html = '<strong>This is a bold. </strong><br>This is not.'
    m.Subject='This message has two versions: Html and plaintext'
    print(m.Subject)
    m.snlSend()

    #Test sending an attachment

    m = Message()
    m.To=testsubject + 'snl.salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'This email should have a jpeg picture attached.\n\n'
    m.attach("image.jpg")
    m.Subject='This message should have a picture of a dog attached.'
    print(m.Subject)
    m.snlSend()


    #Test sending fixed font message

    m = Message()
    m.To=testsubject + 'snl.salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'This email should have a fixed font.\nWWWWWWWWWW\nlllllllll1'
    m.Subject='This message should have a fixed font'
    m.makeFixedWidth()
    print(m.Subject)
    m.snlSend()

    #Test sending authenticated message through smtp-auth.snl.salk.edu

    m = Message()
    m.To=testsubject + 'snl.salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'This email was sent through smtp-auth'
    m.Subject='This email was sent throught smtp-auth'
    print(m.Subject)
    from smtplib import SMTPAuthenticationError
    try:
        m.snlSend(username = "jb", password = "put Jb's password here")
    except SMTPAuthenticationError:
        print("**Authentication failure")


    #Test sending with CC

    m = Message()
    m.To=testsubject + 'salk.edu'
    m.CC = testsubject + 'snl.salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'Test sending with CC'
    m.Subject='Test sending with CC'
    print(m.Subject)
    m.snlSend()

    #Test sending with BCC

    m = Message()
    m.To=testsubject + 'salk.edu'
    m.BCC = testsubject + 'snl.salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'Test sending with BCC'
    m.Subject='Test sending with BCC'
    print(m.Subject)
    m.snlSend()

    #Test text wrapping the plain text body using the wrapBody() method.
    #You can't do this to self.Html.
    m = Message()
    m.To=testsubject + 'salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).

 
    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

    The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
    '''
    m.Subject='Test wrapping at 40'
    print(m.Subject)
    m.wrapBody(width=40)
    m.snlSend()
    m.Subject='Test test wrapping at 120'
    m.wrapBody(width=120)
    print(m.Subject)
    m.snlSend()

    #Test adding a Precedence: bulk header
    m = Message()
    m.To=testsubject + 'snl.salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'This is a test.'
    m.Subject='This is a test of adding additional headers. Look for Precedence: bulk'
    m.addlHeaders = [["Precedence", "bulk"]]
    print(m.Subject)
    m.snlSend()
    

    # Test sending with non-default server
    m = Message()
    m.To=testsubject + 'salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'Test sending with non-default server'
    m.Subject='Test sending with non-default server'
    print(m.Subject)
    #Test using CS's server
    m.customSend('smtp.salk.edu')

    # Test sending with non-default server with authentication
    m = Message()
    m.To=testsubject + 'salk.edu'
    m.From=testsubject + 'salk.edu'
    m.Body = 'Test sending with non-default server with authentication'
    m.Subject='Test sending with non-default server with authentication'
    print(m.Subject)
    m.customSend('smtp.snl.salk.edu', username='jb', password="****")



#Test sending through gmail
#=================================================================#
raise SystemExit
print('\n=================================================\nSending tests through gmail')

#Test sending to a single recipient
m = Message()
m.To=testsubject + 'snl.salk.edu'
m.From=testsubject + 'salk.edu'
m.Body = 'This is a test.'
m.Subject='This is a test of single recipient'
print(m.Subject)
m.gmailSend()

#Test sending to a list of recipients

m = Message()
m.To=[testsubject + 'snl.salk.edu',testsubject + 'salk.edu']
m.From=testsubject + 'salk.edu'
m.Body = 'This is a test.'
m.Subject='This is a test of list of recipients'
print(m.Subject)
m.gmailSend()

#Test sending to a list of recipients where one of the 
#recipient addresses is malformed

m = Message()
m.To=['lee-snl.salk.edu',testsubject + 'snl.salk.edu']
m.From=testsubject + 'salk.edu'
m.Body = 'This is a test.'
m.Subject='This is a test of list of recipients with malformed address'
print(m.Subject)
m.gmailSend()

#Test sending Html body and no plaintext

m = Message()
m.To=testsubject + 'snl.salk.edu'
m.From=testsubject + 'salk.edu'
m.Html = '<strong>This is a bold. </strong><br>This is not.'
m.Subject='This is a test Html; There should be a markdown version'
print(m.Subject)
m.gmailSend()

#Test sending Html body AND plaintext

m = Message()
m.To=testsubject + 'snl.salk.edu'
m.From=testsubject + 'salk.edu'
m.Body = 'This is the plaintext version.'
m.Html = '<strong>This is a bold. </strong><br>This is not.'
m.Subject='This message has two versions: Html and plaintext'
print(m.Subject)
m.gmailSend()

#Test sending an attachment

m = Message()
m.To=testsubject + 'snl.salk.edu'
m.From=testsubject + 'salk.edu'
m.Body = 'This email should have a jpeg picture attached.\n\n'
m.attach("image.jpg")
m.Subject='This message should have a picture attached'
print(m.Subject)
m.gmailSend()
