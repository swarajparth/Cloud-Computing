Install and configure Docker/Container platform in an EC2 instance on AWS. Depending on your system, you might have to use sudo for all commands given below. (Here we have taken the windows operating system).<br/>
# Step: 1
Install Docker Community Edition on your machine : [https://docs.docker.com/install/](https://docs.docker.com/install/)<br/>
On ubuntu it should be as easy as
```sh
apt-get install docker docker.io -y 
```
# Step: 2
Type 
```sh
docker
```
in your terminal and check if its properly working.
# Step: 3
1. Go to docker [https://hub.docker.com](https://hub.docker.com). Search for the Python official image and pull the image having python version 3.8. 
```sh
docker pull python:3.8-slim
```
2. The following command is for checking the downloaded image in the container.
```sh
docker images
```
# Step: 4
Fire up a container container. 
1. you can name it anything you want 
```sh
docker run -dit --name=pyContainer python:3.8-slim
```
2. Here the name is pyContainer, You can change according to your choice but you can't create two containers with same name.<br/>
Your container should be listed here.<br/>
```sh
docker container ls
```
3. To go inside your container, remember this cmd
```sh
docker exec -it pyContainer /bin/bash
```
Here as we have the container name as pyContainer so we need to pass the name of the container here then /bin/bash.
4. If you have done it correctly, the something like the following should show up in
your terminal
```sh
root@02UwU3:/#
```
# Step: 5
Inside the container go ahead check of the version python that you want is running correctly.
```sh
root@02UwU3:/# python -c"print('hello world')"
```
```sh
root@02UwU3:/# python --version
```
Take note of the directory structure
```sh
root@02UwW3:/# ls
```
Exit the container like so
```sh
root@02UwW3:/#exit
```
# Step: 6
The container is basically running linux, so think of it as being inside the terminal of your own laptop. You can run
```sh
root@02UwW3:/# sudo apt-get update
```
Note: Do this before exit command.<br/>
and see for yourself. However, it is running in isolation, so its interaction with your machine is limited (can be changed). This container will have python3.8 installed by default, so that you don’t needlessly waste time setting up a another installation of python. This concept extendsto any tool that you want to use!
# Step: 7
Since the container is running isolated and running inside your terminal, theonly way for you nowisto create a newfile inside the container and use commandline tools like vim, nano to make write any sort of script inside the container. This could be an annoyance.(if you are okay with it,then good for you.) Lets fix that.
Since we cannot edit a launched container, we will stop and delete it and create a new container where we mount a folder of your local machine inside the container,so that any changes you make in that directory of your local machine shows up in your container. So, in your local terminal, run the following<br/>
Recall what you named your container, if you dont, just 
```sh
docker container ls
```
```sh
docker container stop pyContainer
```
```sh
docker container rm pyContainer
```
Create a new folder or use an existing one
```sh
mkdir testfolder
```
Note: After making the folder we need to put the python codes inside that **testfolder**(which is in the local machine, not be present in docker container) so that our docker container can copy those files from the **testfolder** to the **myfolder**(which is inside of the docker conatiner).<br/>
For example here we have the **[lab_06.py](https://github.com/swarajparth/Cloud-Computing/blob/main/Lab%2006/lab_6.py)** file which has been kept inside the **testfolder** and then we run the following two commands(respectively two below commands) to copy that **testfolder** conatins to the **myfolder** conatainer.
Find out the path of your folder
```sh
dir
```
Use the following command to copy the files of the **testfolder** folder to **myfolder** folder.<br/>
```sh
docker run -dit --name=pyC -v C:\Users\USER\testfolder:/home/myfolder python:3.8-slim
```
Now execute..
```sh
docker exec -it pyC /bin/bash
```
Note: your mounted folder should up as 'myfolder'. Any changes in this directory should show up in both your local machine and this container.
```sh
root@02UwU3:/# ls
```

# Example
```sh
C:\Users\USER> docker container ls
CONTAINER ID   IMAGE             COMMAND     CREATED          STATUS          PORTS     NAMES
ffdff95d7500   python:3.8-slim   "python3"   23 seconds ago   Up 21 seconds             pyshyam
d0f9f5a3378f   python:3.8-slim   "python3"   7 minutes ago    Up 7 minutes              pyC
21caead621be   python:3.8-slim   "python3"   28 minutes ago   Up 28 minutes             pyContainer

C:\Users\USER> docker exec -it pyshyam /bin/bash
root@ffdff95d7500:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

root@ffdff95d7500:/# cd home

root@ffdff95d7500:/home# ls
myfolder

root@ffdff95d7500:/home# cd myfolder/

root@ffdff95d7500:/home/myfolder# ls
python.txt  python_file.py

root@ffdff95d7500:/home/myfolder# python python_file.py
The distance is :  10.63014581273465

root@ffdff95d7500:/home/myfolder# exit.
```

Created by @shyammarjit.

