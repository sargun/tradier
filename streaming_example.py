import tradier
from pprint import pprint
from tradier_python import streaming_client

configuration = tradier.Configuration(
	host = "https://api.tradier.com/v1",
)
configuration.access_token = 'YOUR PRODUCTION ACCESS TOKEN'

api_client = tradier.ApiClient(configuration)
api_instance = tradier.DefaultApi(api_client)
session = api_instance.markets_events_session_post()
for i in streaming_client.events(api_client, 'AAPL', session):
	pprint(i)