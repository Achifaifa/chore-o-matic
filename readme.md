Chore-O-Matic

Automated chore distributor for shared flats. Automatically emails the next chore to do to all users. 

### Use:

1.- Copy all files to a folder (index.html file can be ignored if there are no plans to use the website)
2.- Fill all fields in `data.py`, including the SMTP connection parameters. If an email account needs to be setup just for this, `mail.com` is the only provider that allows programmatic smtp access and doesn't ask for a phone number or the blood of a unicorn
3.- Make sure the computer is going to be up and with internet connection
4.- Program a cron job to run weekly.py every friday at 1200 (For example)

The script will automatically rotate all tasks, update the website and send an email to everyone with their new tasks. 

### TO-DO:

* online shopping list updatable/gettable by email