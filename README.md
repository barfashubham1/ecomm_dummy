
# Ecomm. Dummy Project

## Project setup steps-

### 1. Clone Project in local -
step first is to clone repo. in local environment.
to clone use "git clone https://github.com/barfashubham1/ecomm_dummy.git" [url](https://github.com/barfashubham1/ecomm_dummy.git)


### 2. After cloning-
```cd ecomm_dummy ```


### 3. Create your virtual env
Create a virtual environment to install dependencies in and activate it:

to create virtual env- 

``` virtualenv2 --no-site-packages MyVirtualEnv``` 

or use

``` conda create MyVirtualEnv``` 

  if you use anaconda.

### 4. activate env---
use 

```source MyVirtualEnv/bin/activate```
 or 

```conda activate MyVirtualEnv```


### 5.Install dependencies if have and makemigrations

use 

```(MyVirtualEnv)$ "pip install -r requirements.txt```


then cd into project ```cd mystore``` and run ```python manage.py migrate``` to migrate database.
After running migrate command run ``` python manage.py makemigrations ``` or add a app name after makemigrations if you want to make migrations for specific app.

### 6. Run project-
To run project type 
``` python manage.py runserver ``` in mystore dir.





