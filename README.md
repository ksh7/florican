# Florican

> A tool for monitoring over SSH and getting notified on your favorite channels! It runs every 5 minutes and notifies if something goes wrong!

## Quick links

* [Installation](#installation)
* [Config example](#config-example)
* [ToDo](#todo)


## Introduction

What is Florican?

* Florican is *lightweight* and *easy* to set up monitoring service, using a single YAML file
* Florican can be used to monitor any service
* Florican notifies you on your favorite *channels* like e-mail, slack, telegram, etc

YAML file: specify which commands should be run on which servers and what output is expected, and `Florican` will let you know when something is wrong.


## Installation

Install Florican using pip and initialize:

```bash
pip install florican  # PyPI module is WIP
florican init
```

If you need specific channels like Twillio-SMS, Slack or Telegram etc, you need to install specific channel modules

```bash
pip install florican[all-channels]  # PyPI module is WIP
# or for specific ones, modify and run below
pip install -r channel-requirements.txt
```


## Config example

The florican configuration file is placed at `~/.florican/config.yaml` by default and would look something like this:

```yaml
servers:
  primary.website.com:
    - description: 'PostgreSQL status'
      command: 'sudo systemctl status postgresql.service | grep "Active: active" -c'
      expected: '1'
    - description: 'HTTP code website.com'
      command: 'curl -s -o /dev/null -w "%{http_code}" website.com'
      expected: '200'

notifiers:
  - type: slack
    token: 'abcd-efgh-jlkm'
    chat_id: 123456
```


## ToDo

- Use Docker
- Integrate more notification channels
- Release as `pip` module


## Florican Species

[Lesser Florican](https://en.wikipedia.org/wiki/Lesser_florican) & [Bengal Florican](https://en.wikipedia.org/wiki/Bengal_florican) are bustard species native to the Indian subcontinent and adjoining areas. It is listed as Critically Endangered on the [IUCN Red List](https://www.iucnredlist.org/species/22692015/130184896) because fewer than 1000 individuals were estimated to be alive in 2017.

![Alt desc](https://www.iucn.org/sites/default/files/content/images/2017/bustard.jpg)


## Credits & Inspiration

It is inspired by [Fikkie](https://pypi.org/project/fikkie) but using lightweight [Huey](https://github.com/coleifer/huey/) instead of Celery, and allowing more notification channels.
