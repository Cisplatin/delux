# Delux

Automatic apartment door entry.

# Developing

To download and prepare the repository, run:

```
git clone https://github.com/Cisplatin/delux
cd ./delux
pip install -r requirements.txt
```

To add personal settings to Delux, create a `settings.yaml` file with the following format:

```
admin_number: 16471234567
building_number: 16471234569
whitelist:
  16471234567: thom yorke
  16471234568: jonny greenwood
```
