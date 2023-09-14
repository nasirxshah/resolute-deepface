# Deployment Process
### Clone this repo in your local machine
You need to to have git installed in your machine in order to clone this repo. You can clone using following command:
``` bash
git clone https://github.com/nasirxshah/resolute-deepface.git
```
### Build a docker image
For this step, you must install Docker in your machine. First, you have to build a docker image. Inoder to build an image, Dockerfile is used.
``` bash
docker build -t <image-tag> .
```

### Run docker
You can test your docker image is running properly by:
``` bash
docker run -p 5000:5000 --name <container-name> <image-tag>
```
It will create a new container. You can stop the conatiner by:
``` bash
docker stop <container-name>
```
### Push Image to DockerHub
after that, you need to push the image to dockerhub or google cloud registry. following command can be used to push to docker hub :
``` bash
docker tag <image-tag>:<tag> docker.io/<dockerhub-acoount-id>/<image-tag>:<tag>
```
```bash
docker push docker.io/<dockerhub-acoount-id>/<image-tag>:<tag>
```

### Google Cloud Run deploy
- First you must create a google cloud account.
- Open cloud run in product section
- Add a new project
- Create a service
- Enter docker image url
- Allocate sufficient resources
- Set Port 5000 on container
- finnaly, Deploy

# Usage
There are 3 api endpoints available
- /register     
- /recognise    
- / 

### GET /
Here you can test the server is currently running.
you just need to send a GET request

### POST /register
Here you can register a user with username, email and face image with base64 encoding by POST method. Body section is as follows:

```code
{
    "username: <username>,
    "email" <email>,
    "img": <base64-img>
}
```

### POST /recognise
here you can recognise a user if user exists with face image by POST method. Body section is as follows:
```code
{
    "img": <base64-img>
}
```


### Live URL Deployed in Google Cloud Run
```
https://resolute-deepface-hhslguetla-el.a.run.app/
```
