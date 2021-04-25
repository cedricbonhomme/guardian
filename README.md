# Guardian

Check the status of interdependent services.

- based on a YAML file;
- tests performed by custom scripts (Shell script, Python script, etc.);
- no database and serverless;
- generation of HTML status page;
- email notifications.


## Examples

```bash
$ guardian --help
usage: guardian [-h] -c CONFIG_FILE [--email] [--html]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_FILE, --config CONFIG_FILE
                        Configuration file (YAML).
  --email               Send an email in case of failed test(s).
  --html                Generate a HTML status page.


$ cp guardian/config/services.yaml.example guardian/config/monarc-services.yaml


$ guardian -c guardian/config/monarc-services.yaml
+ Service my.monarc.lu
 - Check HTTPS front server
     ✅
 - Check HTTPS FO1 (casesmodels)
     ✅
 - Check HTTPS FO2 (casesmodels2)
     ✅
 - Check HTTPS Back Office
     ✅
+ Service MOSP
 - Check API
     ✅
+ Stats Service
 - Check /about.json endpoint
     ✅
✨ 🌟 ✨ All 6 tests are successful.
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

## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html).

Copyright (C) 2021 [Cédric Bonhomme](https://www.cedricbonhomme.org)
