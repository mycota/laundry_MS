# LMS
MCA Sem 5 project

LMS stand for Laundry Management System

This is my first project in django and I must say am impress with how things went.

This project was develop using macOS, so if you are also on mac all you need is create a virtual env after cloning.

pip3 install -r requirements.txt
pip3 freeze -> requirements.txt // if requirements was not part
// If you decide to use mysql on mac OS
cp -r /usr/local/mysql/lib/* /usr/local/lib
You know the drill

Set your .env for the keys the settings.py

If you are on windows then you have to learn how to make it work yourself, but if I get time then I will make it work on windows too, but for now am a bit busy to do that.

Use the link below to generate a password and used it as your passord for the email to work

https://accounts.google.com/signin/v2/identifier?service=accountsettings&passive=1209600&osid=1&continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&followup=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&rart=ANgoxcd9dFcGb65G7_9xYTvinMD21xzWXY_H_2uj5ABTpSFEiH01V8u4dxGqQgAT7lPtECeeyOoU7t0FcK1Kcwp1r23M_ELZZg&csig=AF-SEnagfwdq893ugDX6%3A1568954712&flowName=GlifWebSignIn&flowEntry=ServiceLogin

Run python manage.py makemigrations
python manage.py migrate

Create a super user to login to the application and the django backend admin

