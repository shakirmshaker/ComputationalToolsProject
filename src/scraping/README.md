# Crawling

The crawling method using **tor** was inspired by [Tor IP rotation](https://github.com/baatout/tor-ip-rotation-python-example).

You do not have to use tor, I added it as an option.

*101_results.json* was the result of getting all the addressses from Copenhagen (101) municipality.
*example.json* is an example property record by the rental website.

## How to run

First run main.py option **1.** to get the addresses from the specific municipality (there should be an option to chose for municipality) and then option **2.** to get rental and further information.

## TODO

- [ ] Add option to choose municipality
- [ ] Fill in TODO in code, have the option to scrap without TOR.
- [ ] Find how to get the total records

## To use TOR

This information was taken by the [Tor IP rotation](https://github.com/baatout/tor-ip-rotation-python-example).

## Requirements
PS: **These are the requirments for Mac OS X**. You can find the requirements for Linux in [PyTorStemPrivoxy](https://github.com/FrackingAnalysis/PyTorStemPrivoxy).

### Tor
```shell
brew update
brew install tor
```

*Notice that the socks listener is on port 9050.*

Next, do the following:
- Enable the ControlPort listener for Tor to listen on port 9051, as this is the port to which Tor will listen for any communication from applications talking to the Tor controller.
- Hash a new password that prevents random access to the port by outside agents.
- Implement cookie authentication as well.

You can create a hashed password out of your password using:
```shell
tor --hash-password my_password
```

Then, update the `/usr/local/etc/tor/torrc` with the port, hashed password, and cookie authentication.
```shell
# content of torrc
ControlPort 9051
# hashed password below is obtained via `tor --hash-password my_password`
HashedControlPassword 16:E600ADC1B52C80BB6022A0E999A7734571A451EB6AE50FED489B72E3DF
CookieAuthentication 1
```

Restart Tor again to the configuration changes are applied.	
```shell
brew services restart tor
```

### Privoxy

Tor itself is not a http proxy. So in order to get access to the Tor Network, use `privoxy` as an http-proxy though socks5.

Install `privoxy` via the following command:
	
```shell
brew install privoxy
```

Now, tell `privoxy` to use TOR by routing all traffic through the SOCKS servers at localhost port 9050.
To do that append `/usr/local/etc/privoxy/config` with the following
```shell
forward-socks5t / 127.0.0.1:9050 . # the dot at the end is important
```

Restart `privoxy` after making the change to the configuration file.
```shell
brew services restart privoxy
```