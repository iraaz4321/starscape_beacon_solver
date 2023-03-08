# **Currently no endpoint is being hosted and code won't be updated or fixed due to state of the game**
# starscape_beacon_solver

Beacon solver is free tool for solving beacons in starscape all of the code is provided under MIT license.

**API**

Api end point can be found at: http://iraaz.eu.pythonanywhere.com/api/solve?
Colors and their letters can be found here https://i.imgur.com/0XMGC8Bh.jpg
api end point takes arguments as query string. Arguments are found below
```
main (required) Letter of the beacon target system. Example main=A
rest (required) Letters of the rest of the beacon colors separated by comma. Example rest=A,M
connected (optional) Amount of systems which are connected to target. Example connected=4

Example query
http://iraaz.eu.pythonanywhere.com/api/solve?main=A&rest=B,B,G,G
```
If you use our API in non private manner we kindly ask you to credit us by providing link to this github page. 

**API ratelimiting**

Currently API is limited to 5 requests/minute (For now. If you need more I recommed hosting the solver yourself)

**discord bot**

We provide hosted discord bot which can solve beacons for you. You can invite it [here](https://discord.com/api/oauth2/authorize?client_id=814130510544502835&permissions=277025704000&scope=bot%20applications.commands)

**Website**

WIP for the most part currently only 3d rendering of the map. http://iraaz.eu.pythonanywhere.com/

**Google sheets version**

Will be added once cleaned up

**Our other projects**

Beacon loot data: https://docs.google.com/spreadsheets/d/1jv37VjkdWJu8qG5-6R-xZqWqt5lY4VO8DONKNqUFSpA/edit?usp=sharing 

scrap drop chances: https://docs.google.com/spreadsheets/d/1XbJ6ypmnZ1Ox0jw1RLzwfQhKfhufdN8iKMpPzGFXGqs/edit?usp=sharing

If you wish to help or have any questions dm iraas#0559 (765119856403021864)






