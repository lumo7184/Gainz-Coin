import fitbit_auth

def print_tokens(CLIENT_ID, CLIENT_SECRET):
    server = fitbit_auth.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
    server.browser_authorize()
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
    print('---------------------------------\n')
    print('ACCESS_TOKEN\n')
    print(ACCESS_TOKEN)
    print()
    print('REFRESH_TOKEN\n')
    print(REFRESH_TOKEN)
    print()
