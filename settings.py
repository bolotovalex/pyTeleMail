username = ""  # <-Type username
password = ""  #
imap = ""  # <-IMAP server url
imap_port = ""  #
smtp = ""  # <-SMTP server url
smtp_port = ""  #

if __name__ == "__main__":
    '''Test connect to imap server, get status connect, get numbers of messages'''
    from imaplib import IMAP4_SSL

    imap = IMAP4_SSL(imap)
    imap.login(username, password)
    status, messages = imap.select("INBOX")
    print(f'Staus connect: {status}')
    print(f'INBOX messages: {messages}')
