U# G3W-ADMIN-ELEPROFILE

G3W-SUITE plugin for create a chart of elevation profile based on a DTM

## Installation

(Change the following 1.0.0 example version number)

```sh
# Install module from github (v1.0.0)
pip3 install git+https://github.com/g3w-suite/g3w-admin-elevation-profile.git@v1.0.0

# Install module from github (dev branch)
# pip3 install git+https://github.com/g3w-suite/g3w-admin-elevation-profile.git@dev

# Install module from local folder (git development)
# pip3 install -e /g3w-admin/plugins/eleprofile

# Install module from PyPi (not yet available)
# pip3 install g3w-admin-elevation-profile
```

Add 'eleprofile' module to G3W_LOCAL_MORE_APPS config value inside local_settings.py:

```python
G3WADMIN_LOCAL_MORE_APPS = [
    ...
    'eleprofile'
    ...
]
```

Sync tree menu by manage.py:

```sh
./manage.py sitetree_resync_apps eleprofile
```

**Compatibile with:**
[![g3w-admin version](https://img.shields.io/badge/g3w--admin-3.5-1EB300.svg?style=flat)](https://github.com/g3w-suite/g3w-admin/tree/v.3.10.x)
[![g3w-suite-docker version](https://img.shields.io/badge/g3w--suite--docker-3.10-1EB300.svg?style=flat)](https://github.com/g3w-suite/g3w-suite-docker/tree/v3.10.x)
[![g3w-admin version](https://img.shields.io/badge/g3w--admin-3.6-1EB300.svg?style=flat)](https://github.com/g3w-suite/g3w-admin/tree/v.3.11.x)
[![g3w-suite-docker version](https://img.shields.io/badge/g3w--suite--docker-3.11-1EB300.svg?style=flat)](https://github.com/g3w-suite/g3w-suite-docker/tree/v3.11.x)
