# instagram-unfollowers
Who unfollowed you, who followed you, who doesn't follow you back, who liked your pics the most and who never? Don't worry I got all the answers. Also this can used for non-private users too.

i. information
--------------

**This badboy creates a html file with information of:**

 - New unfollowers
 - New followers
 - Who is not following back 
 - Who liked your pics the most -- numerically of course :D
 - Who never liked your pics 
 

**Also you can check other profiles too. Of course they need to be public or your following.**

ii. install and run
-------------------

This project is based and forked from ahmdrz/instagram-statistics.

In order to install the requirement packages and run the progam. Type following to the terminal.
```
git clone https://github.com/cagrio/instagram-unfollowers
```
```
pip install -r requirements.txt
```
In order to use you need to get instagram id. It is different than username and just contains numbers. It can be learn from various sites. 
ex: http://www.ershad7.com/InstagramUserID/
 
 ![Alt Text](https://media.giphy.com/media/3ohs80R80RThSPnAkw/giphy.gif)

We see that instagram user id for nasa is 528817151

In order to use it you need to edit **main.py**
```
 print " ~ Connecting to Instagram"                                          
 #modify here                                                                
 insta = Instagram('usernamefoo', 'passfordfoo')                                   
             
```
After writing down the username and password run the program

    python main.py foouserid
 
Write whoever you want to check.  You or your Ex or nasa. Lets say you're checking nasa's account.

    python main.py 528817151
  

iii. some ideas
---------------

If you have Raspberry Pi up and running in your home or whatever. You can make it send you a email at every once a while. 

In order to send html output email with Mutt, download and configure your .muttrc according to your email provider. hen create a instagramReportEmail.sh

    #!/bin/bash 
    
    /usr/bin/python /home/pi/instagram-unfollowers/main.py 528817151 
    /usr/bin/mutt -e "my_hdr Content-Type: text/html" username@emailadress.com  -s "instagram report" < instagram-unfollowers/output.html

Alternatively since strange usernames can mess up html view of email reader, its safer to use output.html as attachment.

    #!/bin/bash 
    
    /usr/bin/python /home/pi/instagram-unfollowers/main.py 528817151 
    /bin/echo "brtyb github.com/cagrio" | /usr/bin/mutt -a "output.html" -s "instagram weekly follow report" -- username@emailadress.com 



And make sure you make it executable

    chmod +x instaReport.sh

Check if that works and make sure you get the email. Now lets make it periodical. In order to make the linuxbox do some periodical tasks write

    crontab -e

to the terminal. Following example uses Mutt to send email.  It send email at every sunday at 4:16 pm. This line is added to the crontab file.

16 16 * * SUN /home/pi/instaReport.sh


iv. license
---------------
See full license on [this](https://github.com/cagrio/instagram-unfollowers/blob/master/LICENSE) , Under GNU GENERAL PUBLIC LICENSE




