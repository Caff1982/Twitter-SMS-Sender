
# Twitter-SMS-Sender

## Description

The purpose of this project is to monitor a Twitter account and send an SMS whenever keywords are included in the tweet. I created this to monitor Elon Musk's account and notify me if he mentions certain cryptocurrencies.

## How to use

- Create a new Twitter application and generate consumer key and access token. Put these in config.py (https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
- Create a txtlocal account (https://www.textlocal.com/signup/) and obtain username, sender and API hash. Put these in the config.py file along with the phone number(s) you want to send to. The first 10 texts are sent free.
- Get the Twitter user-id of the account you want to monitor (I used https://tweeterid.com/) and put this in config.py.
- The keywords to search for in the tweet are defined in the TwitterListener class in main.py. A text will be sent if any one of these words are in the text.
- If you want to run the program for a long time I would recommend hosting it on Heroku.

Note: This project sends SMS messages to UK phone numbers. If you are not in the UK the project could be easily updated by changing the send_sms.py file to a service that works in your country.

## Contributing

Any Issues or Pull Requests are always welcome.

## License

Licensed under the MIT license.