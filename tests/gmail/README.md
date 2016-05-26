Environment
===========
	Mac OSX 10.11.5 used
	Install Android SDK
	Install Appium

Setup for Test
==============
Create an AVD
-------------
	Create an AVD created and run it.
	Install Gmail from http://opengapps.org/
	Sign in an Gmail account in Gmail app

Run check of appium-doctor
--------------------------
	appium-doctor is missing from 1.5.2 binary, get it from github

Run Appium
----------
	Appium configured(using the testGmail.appiumconfig) and launch a server

Test
====
Clone this github
-----------------
	$git clone https://github.com/3r1ccc/pytest.demo.git

Create and run an virtualenv
----------------------------
	$virtualenv ss	
	$source ss/bin/activate

Installation of py.test dependency
----------------------------------
	$python setup.py install
	or 
	$pip -r install requirements.txt


Run testGmail
-------------
	github.3r1ccc.pytest.demo ericcc$ py.test tests/gmail/test_sent_mail.py 

