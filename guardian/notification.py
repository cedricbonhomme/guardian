#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import socket
import smtplib
from email.mime.text import MIMEText

from guardian import conf


def irker(message):
    """Send a JSON formatted message to an instance of irker."""
    if not conf.IRC_CHANNEL:
        raise "No IRC channel defined."
    data = {"to": conf.IRC_CHANNEL, "privmsg": message}
    try:
        s = socket.create_connection((conf.IRKER_HOST, conf.IRKER_PORT))
        s.sendall(json.dumps(data).encode("utf-8"))
    except socket.error as e:
        sys.stderr.write("irkerd: write to server failed: %r\n" % e)


def mail(mfrom, mto, message):
    """Send the notification via mail."""
    email = MIMEText(message, "plain", "utf-8")
    email["From"] = mfrom
    email["To"] = mto
    email["Subject"] = "Guardian : Alert"
    # email['Text'] = message

    server = smtplib.SMTP(conf.SMTP_SERVER)
    server.login(conf.USERNAME, conf.PASSWORD)
    server.send_message(email)
    server.quit()
