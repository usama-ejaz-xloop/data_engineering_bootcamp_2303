# Introduction to Data Engineering
## Day 4 - Basics of Docker
This directory contains files related to hands-on part for day 3 of the module.

The detailed explanation of the tasks can be found in the slides at the end of the presentation file.

### Task 1
Follow procedure to compile the Hello World app in container, the final image should be small without development tools. Make it easy to pass own versions of greetings text while running container. Use multi-stage dockerfile with entrypoint/cmd.

Task path:
`tasks/1_introduction/day_4_basics_of_docker/task1`

### Task 2
Run WordPress with MariaDB in containers. Use own network and volumes to persist data for both containers. Check if wordpress is running: http://localhost:80

Task path:
`tasks/1_introduction/day_4_basics_of_docker/task2`

### Bonus task
Use alpine/distroless image for running the Hello World app from Task 1. Use following links as a startpoint:

- https://stackoverflow.com/questions/59341750/why-cant-i-run-a-c-program-built-on-alpine-on-ubuntu
- https://jpetazzo.github.io/2020/02/01/quest-minimal-docker-images-part-1/
- http://jurjenbokma.com/ApprenticesNotes/getting_statlinked_binaries_on_debian.xhtml
