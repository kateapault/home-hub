# Home Hub

because my fiance needed something to replace asking Alexa


## setup so far
to start up broker:
ensure docker is up and running, then:
`docker-compose up -d`

to start up back end:
`flask run --debug`

to start up front end:
`npm run dev`


# ongoing notes
- for some reason specifying localhost & port 1883 for both vue and python renders them unable to connect, but leaving them off allows connection



# TO DOs
- put all startup into single docker file