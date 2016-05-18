# mailmerge
Create per-user HTML emails by rendering an HTML template using data from .xlsx spreadsheet. It doesn't require Excel but works with it. mailmerge is written in Python and includes an OS X compiled binary that requires no installation and has no dependencies. A Windows binary can be build on request. While this repositry is public, public use would require further development.

Overview
=======

mail merge is similar to Microsoft Office's mailmerge except that it sends HTML email, it doesn't depend on Outlook, and
it's scriptable.

Usage
=====
Duplicate the mailmerge folder. Rename the duplicate to be the subject of your email. Put your data into named columns
in data.xlsx, edit the html template 'template.html'  using TextEdit and run send.command (Mac) or send.exe (Windows).
To create a new emailing, duplicate the entire folder.

Details
=======
send loops over every row in the first sheet of data.xlsx (except the header row) sending one email per row. The email
is HTML and it is addressed to the email address in the 'To' field.  The html created by rendering the template
'template.html' with data from 'data.xlsx.'

'data.xlsx' must have the columns 'To' and 'From'. Column titles are case sensitive. The 'Name' column  is recommended
but optional. The Skiprow column is optional; it's used if you want to send the email for only some rows. Put "yes" or
"true" or 1 in Skiprow for rows that you want to skip.

In your template, enclose the name of the data you want merged in double braces. For example, Dear {{Name}}, will get
rendered as Dear <name>, where name is the name from the current row. {{Name}} refers to a column name in data.xlsx and
it is care sensitive

Column names in the header row of data.xlsx are rendered in 'template.html' by enclosing the column name in braces. Just
follow the pattern in 'template.html.'   The encoding of 'template.html' should be UTF-8 if you're going to have latin
or unicode characters (this is the default on Mac and I believe on Widnows).

To do a test run where every email is send to you, fill the 'Redirect' column with your email address.

A log of sent emails will be in mailmerge.log
