Description
===========
Small python script to mail people specified in a text file the content of a defined html file

Requirements
============
* Requests library
* MAILGUN_BASE_URL environment variable with your mailgun api url
* MAILGUN_SECRET environment variable with your mailgun secret key
* "recipient.txt" file with all the addresses emails should be sent to. One address per line
* Email html content is read from "mail.html"

HOW TO RUN
==========
`python mail.py`
