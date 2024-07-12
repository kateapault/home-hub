# Home Hub

because my fiance needed something to replace asking Alexa :sparkles:


## setup at the moment
to start up broker:
ensure docker is up and running, then:
`docker-compose up -d`

to start up back end:
start venv if not running, then:
`flask run --debug`

to start up front end:
`npm run dev`


## Troubleshooting notes
The front end MQTT subscription disconnects on error, and this seems to swallow the error message; I'll eventually fix that


### ongoing notes
- for some reason specifying localhost & port 1883 for both vue and python renders them unable to connect, but leaving them off allows connection? look up


# next TO DOs
- finish gathering weather data & push to topics
- add tests
- add styling to FE
- update placeholder broker credentials
- neaten up README / docs