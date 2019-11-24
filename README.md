# Description

The project from [here](https://docs.google.com/spreadsheets/d/1Wmich78faSgrLE6UtKZ5IJPir7sM4vjnoxIMZj4uckM/edit#gid=564880975)

Trello - [here](https://youtu.be/dQw4w9WgXcQ) (TBA)

Bonusly - [here](https://youtu.be/dQw4w9WgXcQ) (TBA)


# Docker

### Explanation
Dockerfile in this repository allows you to mainain a simple steady enviroment for your students' submissions. 

### Pulling

Now you can simply pull already existing docker images from Docker Hub with 

```docker pull mrartemev/leadership```

If you want to build your own docker image proceed to the next step

### Building
To build an image run following code inside repo directory

``` docker build --rm -t <image_name> . ```

For example:

```docker build --rm -t mrartemev/leadership .```

### Usage
To run docker image run following code inside repo directory

```docker run --rm -v `pwd`:/home/leader --name <name> --runtime nvidia -it -p <port>:8888 <image_name>```

For example:

```docker run --rm -v `pwd`:/home/leader --name leader --runtime nvidia -it -p 7777:8888 mrartemev/leadership```

I recommend to run this docker image in something like tmux or screen just in case

If something goes wrong ping me @mrartemev



