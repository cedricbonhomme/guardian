# Guardian

[![PyPi version](https://img.shields.io/pypi/v/guardian.svg?style=flat-square)](https://pypi.org/project/guardian)

Monitor the status of a set of services. Characteristics:

- definition of the services to monitor with a YAML file;
- tests performed by custom scripts (Shell scripts, Python scripts, etc.);
- no database and serverless;
- generation of HTML status page;
- email notifications;
- IRC notifications.


## Installation

```bash
$ pipx install guardian
  installed package guardian 0.2.1, Python 3.9.2
  These apps are now globally available
    - guardian
done! ✨ 🌟 ✨
```

You can now use Guardian from anywhere on your system.


## Usage

```bash
$ guardian --help
usage: guardian [-h] -c CONFIG_FILE [--email] [--irc] [--html]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_FILE, --config CONFIG_FILE
                        Configuration file (YAML).
  --email               Send notification of failed test(s) via email.
  --irc                 Send notification of failed test(s) via IRC.
  --html                Generate a HTML status page.
```


In order to use notification via IRC you need to install
[irker](http://www.catb.org/~esr/irker/). irker is very easy to install and
to run, no configuration is needed. Once executed, irker will wait for JSON
formatted messages on the port 6659. irker will automatically join the channel
you have specified in the
[Guardian configuration file](guardian/config/conf.cfg.sample#L2).
irker will maintain connection state for multiple channels, avoiding obnoxious
join/leave spam.

Configurations related to the sending of emails are in the
[same file](guardian/config/conf.cfg.sample#L5).


## Examples

The goal of the INI configuration file is to set global variables (IRC channel, SMTP
server, etc.). If you do not create your own configuration file, the default one will
be used automatically.

The services to monitor must be described in one (or several) YAML file(s).


```bash
$ cp guardian/config/config.cfg.sample guardian/config/config.cfg
$ cp guardian/config/services.yaml.example guardian/config/services.yaml


$ guardian -c guardian/config/services.yaml
+ Service Newspipe
 - Test about page
     ✅
+ Service MOSP
 - Test main page
     ✅
 - Test search with API v2
     ✅
 - Test API v1
     ✅
+ Freshermeat
 - Test main page
     ✅
Execution time: 0.47015 seconds.
✨ 🌟 ✨ All 5 tests are successful.
```


With email notification:

```bash
$ guardian -c guardian/config/google-services.yaml --email
+ Google services
 - Test GMail
     ✅
 - Test Web search
     ❌
 - Test Google Drive
     ✅
1 error occurred.
Execution time: 0:00:00.793011
Sending email notification...
```

You can combine email notifications, IRC notifications and HTML reporting.


## Contributing

Patches and questions? Send to my [public
inbox](https://lists.sr.ht/~cedric/public-inbox):
[`~cedric/public-inbox@lists.sr.ht`](mailto:~cedric/public-inbox@lists.sr.ht).
Thanks!


## License

[Guardian](https://sr.ht/~cedric/guardian) is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html).

Copyright (C) 2021-2023 [Cédric Bonhomme](https://www.cedricbonhomme.org)
