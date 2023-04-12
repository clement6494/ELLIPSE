# ELLIPSE
# Project - Devops - MARTINEZ - CONCHEZ


## Description

This project aim to exploit a web API (JCDecaux) using Python to retreive data on bikes in diverse cities through the world.

# Summary

- [Project-Devops-MARTINEZ-CONCHEZ](#project---devops---martinez---conchez)
  - [Description](#description)
- [Summary](#summary)
- [Instructions](#instructions)
- [1. Creation of the NodeJS web application](#1-creation-of-the-nodejs-web-application)
  - [Installation](#installation)
  - [Usage](#use-the-application)
  - [Test](#test-the-application)

- [Usefull links](#usefull-links)
- [Authors](#authors)

# Before starting

To clone the repository :

```bash
https://github.com/clement6494/ELLIPSE.git
```

## Instructions

# 1. Creation of the NodeJS web application

## Installation

  This app is written with Nodejs and uses Redis database.
  
  * 1) [install NodeJs](https://nodejs.org/en/download/)
  
  * 2) [install REDIS](https://redis.io/download)

Go to the [userapi](./userapi/) directory of the application (where `package.json` file located) and run :

  ```bash
  npm install 
  ```
![image](images/1_npminstall.png)

## Use the application
 * 1) Start a server
  
  From the [userapi](./user-api/) directory of the repository, use the command below:

```bash
npm run start
```
![image](images/1_npmrunstart.png)

<http://localhost:3000> should be accessible and our web application will run (make sure to have the Redis server open) :

![image](images/1_localhost3000.png)

* 2) To create a user, send the curl POST request to the application with the user data :

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"sergkudinov", "firstname":"sergei", "lastname":"kudinov"}' \
  http://localhost:3000/user
```
![image](images/1_curlPOST.png)

It should output:

```bash
{"status":"success","msg":"OK"}
```  

After, if you go to <http://localhost:3000/user/sergkudinov>, with "sergkudinov" being the username that you had in your POST data, it will display in the browser the following, with correspondance to the data that you posted :  

```bash
{"status":"success","msg":{"firstname":"sergei","lastname":"kudinov"}}
```
![image](images/1_localhost3000usersergkudinov.png)

You can also use POST, GET , and DELETE.
UPDATE wasn't finished because we didn't undersood well what was the ID in the model given of username,firstname,lastname. So we didn't know what souldn't be change and used as ID.

## Test the application 

Go to the [userapi](./userapi/) directory of the application (where `package.json` file located) and run the command below:

```bash
npm run test
``` 
All 12 tests should be passed :  

![image](images/1_npmruntest.PNG)



## Authors


- Clément CONCHEZ-BOUEYTOU: <clement.conchezboueytou@ece.edu.fr> - ING4 gp5

Copyright © Clément CONCHEZ-BOUEYTOU, 2023
![image](images/LogoECE.PNG)

