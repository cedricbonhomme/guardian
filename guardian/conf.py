#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser

# load the configuration
config = configparser.SafeConfigParser()
try:
    config.read("guardian/config/conf.cfg")
except Exception:
    pass  # config.read("guardian/config/conf.cfg.sample")


IRC_CHANNEL = config.get("irc", "channel", fallback="")
IRKER_HOST = config.get("irc", "host", fallback="localhost")
IRKER_PORT = int(config.get("irc", "port", fallback=6659))

MAIL_FROM = config.get("email", "mail_from", fallback="guardian@localhost")
MAIL_TO = [config.get("email", "mail_to", fallback="")]
SMTP_SERVER = config.get("email", "smtp", fallback="")
USERNAME = config.get("email", "username", fallback="")
PASSWORD = config.get("email", "password", fallback="")
