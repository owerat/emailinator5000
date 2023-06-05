Emailinator5000
===============

Emailinator5000 is a webapp designed to extract email addresses from a given text input. It is built using Flask.

![screenshot](https://github.com/owerat/emailinator5000/assets/135650175/5a8dea05-cb58-41c9-ba32-8a53e2773814)

How it works
------------

You paste or type your text into a text box on the webapp. After submitting the form, the app will process the text, extract all email addresses, and display them in two formats:

1.  Line by line in a text box.
2.  As a single line of text in another text box, with email addresses separated by semicolons for outlook/email clients

In addition, the extracted email addresses will be saved into a file named emails.txt. This was part of the orignal operation and by default this is overridden on each run and is not defined in the container.

Running the application using Docker
------------------------------------

1. Pull the Docker image from the Docker registry. 
2. Start a container based on the image. 
3. App will be running on: http://localhost:5000.