#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser

# load the configuration
config = configparser.SafeConfigParser()
try:
    config.read("guardian/config/conf.cfg")
except:
    config.read("guardian/config/conf.cfg.sample")


IRC_CHANNEL = config.get("irc", "channel")
IRKER_HOST = config.get("irc", "host")
IRKER_PORT = int(config.get("irc", "port"))

MAIL_FROM = config.get("email", "mail_from")
MAIL_TO = [config.get("email", "mail_to")]
SMTP_SERVER = config.get("email", "smtp")
USERNAME = config.get("email", "username")
PASSWORD = config.get("email", "password")
