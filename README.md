# Guardian

Check the status of interdependent services.

- based on a yaml file;
- checks and measures performed by probes;
- no database;
- serverless;
- email notifications.


## Example

```bash
$ guardian -h
usage: guardian [-h] -c CONFIG_FILE [--email]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_FILE, --config CONFIG_FILE
                        Configuration file (YAML).
  --email               Send an email in case of failed test(s).


$ cp guardian/config/services.yaml.example guardian/config/monarc-services.yaml


$ guardian -c guardian/config/monarc-services.yaml
+ Service my.monarc.lu
 - Check front server with curl
     ✅
 - Check casesmodels with curl
     ✅
 - Check casesmodels2 with curl
     ✅
 - Check Back Office with curl
     ✅
+ Service MOSP
 - Check API
     ✅
+ Stats Service
 - Check /about.json endpoint
     ✅
✨ 🌟 ✨ All 6 tests are successful.
```

## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html).

Copyright (C) 2021 [Cédric Bonhomme](https://www.cedricbonhomme.org)
