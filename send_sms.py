import requests

import config


def send_sms(message, test_flag=1):
    """
    Send SMS using txtlocal.co.uk API

    test_flag (int): 1 to enable to test_mode (no sms sent), 0 to send sms
    """
    username = config.TXTLOCAL_USERNAME
    sender = config.TXTLOCAL_SENDER
    apihash = config.TXTLOCAL_API_HASH
    url = 'https://api.txtlocal.com/send/'
    # More numbers can be added to the tuple
    numbers = config.TXTLOCAL_NUMBERS

    params = {'test'    : test_flag,
          'username': username,
          'hash'    : apihash,
          'message' : message,
          'sender'  : sender,
          'numbers' : numbers }
 
    print('Attempting to send SMS...')
    try:
      response = requests.get(url, params)
      print('Message sent. Status code: ', response.status_code)
    except Exception as e:
      print('An error occured: ', e)