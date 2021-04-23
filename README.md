# Guardian

Check the status of interdependent services.

- based on a yaml file;
- checks and measures performed by probes;
- no database;
- serverless;
- export different kind or reports.


## Example

```bash
$ cp guardian/config/services.yaml.example guardian/config/services.yaml

$ guardian -c guardian/config/services1.yaml
+ Service my.monarc.lu
 - Check front server with curl
     -> OK
 - Check casesmodels with curl
     -> OK
 - Check casesmodels2 with curl
     -> OK
 - Check Back Office with curl
     -> OK
+ Service MOSP
 - Check API
     -> OK
+ Stats Service
 - Check /about.json endpoint
     -> OK
✨ 🌟 ✨ All tests are successful.
```

## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html).

Copyright (C) 2021 [Cédric Bonhomme](https://www.cedricbonhomme.org)
