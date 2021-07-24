# LinebotCallScript
This is a side project to auto filling google form with LineBot on GCP linux server,  
and the code is suppose to put on linux server when running it.  
(If you want to reference this sample code, you need to modify "LinebotCallScript/PracticeLineBot"  
which automatically filling google form and was done by selenium, but I won't refer to it following article.)  

## Environment
Python 3.7.2  
- pip install requirement.txt  

## Third party
- Django  
- Selenium  
- ngrok  

## Demo
While entering the specific keywords, then the script I put on GCP linux server will perform  
to fill the annoying google form.   
![Demo pic1](https://github.com/ycc789741ycc/LinebotCallScript/blob/master/pics/Demo1.png "Demo pic1")

## Proxy
I use [ngrok](https://dashboard.ngrok.com/get-started/setup) to apply for URL.
- 1.Download ngrok.exe on your linux server  
- 2.Open the terminal  
    ```
    ./ngrok authtoken XXXXXXXXXXXXXXX 
    screen  
    ./ngrok http 8000
    ```

## Run Django on Linux
- 1.Check URL on terminal  
![Demo pic2](https://github.com/ycc789741ycc/LinebotCallScript/blob/master/pics/Demo2.png "Demo pic2")
- 2.Open the terminal "Ctrl + d + a" to detach the screen.
- 3.Add URL (a3xxxxx.ngrok.io) to LinebotCallScript/DjangoPractice/settings -> ALLOWED_HOSTS
- 4.Open the terminal  
  ```
  screen
  python runserver.py
  ```
  "Ctrl + d + a" to detach the screen  
- 5\.  
  If you want to check the screen  
  ```
  screen -ls
  ```
  If you want to switch to the screen  
  ```
  screen -r YOUR SCREEN ID
  ```
  
  ## LINE Webhook  
  Go to [LINE's official website](https://developers.line.biz/en/) and LOGIN to create your LINE server,  
  and it is neccessary to go Webhook setting to enable your URL.
  ![Demo pic3](https://github.com/ycc789741ycc/LinebotCallScript/blob/master/pics/Demo3.png "Demo pic3")
  
  ## End
  Now you can deploy your script with LineBot, though I omit a lot of detail about my code :joy:
