# instagram-scraper

This python script is to retrieve list of usernames whom you should unfollow :p (People whom you follow but they don't follow you)

## Steps to run

`
python main.py --username <USERNAME> --password <PASSWORD>
`

If there are special characters in the password, we will have to escape them using "\\". 

This generates a file named `unfollowers_<USERNAME>.txt` in your directory containing the list of people to unfollow.

## Dependencies

1. Python3 
2. instaloader
3. numpy

Note: This script does not work with accounts where two factor authentication is enabled.
