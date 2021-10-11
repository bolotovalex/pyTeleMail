import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import settings

#TODO Type username and password
username = settings.username
password = settings.password

def clean(text):
    # чистый текст для создания папки
    return "".join(c if c.isalnum() else "_" for c in text)

imap = imaplib.IMAP4_SSL(settings.imap) # <- Imap server, example imap.gmail.com
imap.login(username, password)

status, messages = imap.select("INBOX")

