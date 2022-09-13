while True:
    try:
        BTC_URL = float(input('What is Bitcoin price today?:\n'))
        Dollar_Have = float(input('How much $ do you have?:\n'))
        Can_Buy = str(Dollar_Have / BTC_URL)
        print('You can buy:\n' + Can_Buy)
    except ValueError:
        print('You can only enter numbers')
