

# MVP
## TODO
[x] set up basic flask backend w moon phase & test function
[x] set up basic vue frontend w time & moon phase & test display
[x] set up broker w moon phase & test topic
[x] make flask send new moon phase every 12 hour & send new test every 10 sec 
[x] remove test once test is working
[x] add tide
[] straighten out weather language
[x] add current weather
[] add hourly weather
[] add weekly weather
[] set up values at startup
[] make it pretty
[] set up docker to run it all at once

### notes
- using mosquitto
    - front end disconnects when there is an error and seems to swallow the error messages when doing so
    - 

### FE components
- cute header
- body/container for all the information
- current time - can update itself w/o backend input
- current date & day of week - can update itself w/o backend input
- current weather (update every 1 or 5 min)
- hourly weather for today (update every hour?)
- moon phase (update every 12h)
- tide (update every 30 min)
- daily weather next 7 days (update every 8 or 12h)
- astrology thing possibly? no idea what ought to be in this tho

#### tests
- not thorough I know
- BE: add integration test for each endpoint
- 

#### serving
- look up how to get this all to run on raspberry pi - docker needed presumably?
- look up how to get this to update itself when live/prod/master branch gets updated
- set up github to run tests on push
- set up raspberry pi & monitor

# EXPANSIONS
## mini feature - subway times
### FE
- component for subway
- little list of southbound & northbound trains; show arrival times & colors
### BE
- add to house info file
- display/include always. constants - our stop location
- wmata api...?
#### show travel time to trivia on Tuesdays

## mini feature ideas
- fun fact of the day

## bigger feature ideas
- grocery list (text endpoint to add to grocery list; text other endpoint to get grocery list; text to clear?)
- Lana schedule (windows for feeding / walking / vitamins; have text endpoint to take in fed/walk info & update windows based on when last done. Send notification / show in yellow/red when it's time to do so again)
- hook up to google calendar or something to show events?
- reminders?

## sending and recieving sms
### could use out of box service OR could set up by myself
### setup involves:
- make SMTP server (look at docker-mailserver)
- basically gotta make a stripped down email client
- should be able to accept and sent sms; should try and limit incoming/outgoing mail to our phone #s (keep in .env and cross check all incoming/outgoing?)
- python email API to listen on server & to send messages via server
