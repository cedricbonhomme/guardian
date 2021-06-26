#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import socket

from guardian import conf


def irker(message):
    """Send a JSON formatted message to an instance of irker."""
    data = {"to": conf.IRC_CHANNEL, "privmsg": message}
    try:
        s = socket.create_connection((conf.IRKER_HOST, conf.IRKER_PORT))
        s.sendall(json.dumps(data).encode("utf-8"))
    except socket.error as e:
        sys.stderr.write("irkerd: write to server failed: %r\n" % e)
