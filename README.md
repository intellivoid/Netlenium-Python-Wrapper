# Netlenium Python Wrapper

This python package allows you to automate Web Browsers such as
Firefox, Opera and Chrome using Netlenium in your Python Code.


This library does not provide the actual executable files for
Netlenium, nor will it start the Netlenium server. You must
have Netlenium installed on your system and running if you want
to create sessions using this library.

[Find Netlenium Binaries here](https://netlenium.intellivoid.info/)

## Setup

Install using `setup.py`
```shell script
sudo -H python3 -m pip install .
```

Install using PyPi
```
sudo -H python3 -m pip install netlenium
```


## Usage Example

```python
import netlenium

client = netlenium.Client()

# Custom Setup
#client = netlenium.Client(target_driver=netlenium.types.DriverType.firefox)
#proxy = netlenium.Proxy(
#    host="127.0.0.1",
#    port=8080,
#    authentication_required=False,
#    username=None,
#    password=None
#)
#client.set_proxy_configuration(proxy)

client.load_url("https://google.com/")

SearchInput = client.get_element(netlenium.types.By.name, "q")
SearchInput.send_keys("Netlenium")
SearchInput.submit()
# Wait for the page to finish loading


# List search results
for element in client.get_elements(netlenium.types.By.class_name, "g"):
    print(element.inner_text)
    print("\n")

client.stop()
```