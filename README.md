# Gainz Token
#Crypto Currency 
#We have created a proof of physical work, smart contract blockchain platform. The platform is a ERC-20 token & Ethereum based smart contract network that currently works with a real FitBit device. Gainz token is “mined” by physical work and distributed when goals are completed. The smart contract technology allows personal trainers and fitness influencers to challenge other influencers in a step/calorie/distance FitBit challenge, winner takes all the tokens on the wager.

The prototype utilizes a smart contract called Tasks. The hierarchy of the prototype designed is the following:

└── Web Application Backend
     └── Coaches
          └── Tasks
               └── Users

e.g. Coaches create Tasks which can be accepted and monitored by users. The Web Application serves as an intermediary between FitBit (or other fitness tracking device) data from the User and the accepted Tasks.

Ideally, the application will have some tolerance for centralization to limit its dependence on data storage via the somewhat expensive smart contracts however these decisions will have to be addressed when future developers are building out the final product. It’s important to think critically about the advantages of blockchain vs. traditional databases and the best applications of the future will be the ones that take advantage of both. Because solidity as well as the scalability of the Ethereum network are both constantly changing and improving, the Gainz Network will have to be adaptive in how it functions and make compromises in the short term.

The Gainz Token network is a blockchain product that you can use to create fitness challenges.  The python backend continuously updates from the fitbit servers.  The live fitbit continuously pushes data throughout the day.  Once the data is on the fitbit servers you can access it from the Fitbit API library once a user inputs their users credentials.  Once a user registers with fitbit, you input your users credentials into our platform.  Our python code wraps up that fitbit data into a “data frame object” which can be easily used in our smart contract solidity program.  

authorized_client = fitbit.Fitbit(CLIENT_ID, 
                                  		CLIENT_SECRET, 
                                  		oauth2=True, 
                                  		access_token=ACCESS_TOKEN, 
                                  		refresh_token=REFRESH_TOKEN)

The CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN, and REFRESH_TOKEN  will be taken from east users fitbit account so we can upload their data from the fitbit API library. 

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

The web application prototype demonstrates the combination of smart contracts and blockhain technology with fitness data recording devices as well as the gamification of the health industry. While the prototype proves the concept, the final product of what will eventually run the Gainz Network will have to build out and address important technical issues such as multi-user infrastructure, a scalable and secure backend, anti-cheating protocols, as well as storage and cost concerns communicating with the Ethereum network. These areas of development will be in constant flux as Ethereum is still not a finished product and rapidly changing the way it operates. The next step should be a mobile application that can utilize data flow architecture of the prototype while enabling a network of users to participate. Initially you’d focus on user adoption and network maturity while the smart contracts would be more basic and once the network has grown, shift gears to more complicate smart contract logic.


