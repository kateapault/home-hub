

# MVP
## TODO
[x] set up basic flask backend w tide phase & test function
[] set up basic vue frontend w time & tide phase & test display
[] set up broker w tide phase & test topic
[] set up docker to run it all at once
[] make flask send new tide phase every hour & send new test every 10 sec 
[] remove test once test is working
[] 

### notes
- using mosquitto
    - front end keeps disconnecting????
    - 
### FE
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

#### starting
- vue tutorial
- set up very basic vue app with moon phase component & time (bc multiple components)
- set up functions in flask & get data to mqtt topics
- update front end components based on topics
- once that's displaying/functioning properly, add in weather and the rest
#### serving
- look up how to get this all to run on raspberry pi - docker needed?
- look up how to get this to update itself when live/prod/master branch gets updated
- actually set up raspberry pi & monitor

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
