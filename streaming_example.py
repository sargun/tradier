# Expects venv like:
# python3 -mvenv venv
# source venv/bin/activate
# cd libraries/python/urllib3 && python setup.py install; cd -
# pip install requests

import requests, os, json
from pprint import pprint
import tradier_urllib3
from tradier_urllib3.models import StreamingQuote, StreamingTrade, StreamingQuote, StreamingSummary, StreamingTradex, StreamingTimesale

configuration = tradier_urllib3.Configuration(
	host = "https://api.tradier.com/v1",
)

configuration.access_token = os.getenv('ACCESS_TOKEN', 'YOUR PRODUCTION ACCESS TOKEN')

api_client = tradier_urllib3.ApiClient(configuration)
api_instance = tradier_urllib3.DefaultApi(api_client)
session = api_instance.markets_events_session_post()

handlers = {
	'trade': StreamingTrade,
	'quote': StreamingQuote,
	'summary': StreamingSummary,
	'timesale': StreamingTimesale,
	'tradex': StreamingTradex
}

def events(api_client, symbols, session, filter=None, linebreak=True, validOnly=True, advancedDetails=False):
	symbols = symbols
	if isinstance(symbols, list):
		symbols = ','.join(symbols)
	payload = {
		'sessionid': session.stream.sessionid,
		'symbols': symbols,
		'linebreak': linebreak,
		'validOnly': validOnly,
		'advancedDetails': advancedDetails
	}
	if filter:
		payload['filter'] = filter
	headers = {
		'Accept': 'application/json'
	}
	r = requests.post(session.stream.url, stream=True, params=payload, headers=headers)
	r.raise_for_status()
	for line in r.iter_lines():
		if line:
			data = json.loads(line)
			dtype = data['type']
			if dtype not in handlers:
				raise Exception(f'Received unknown {dtype}')
			yield api_client._ApiClient__deserialize(data, handlers[dtype])

for i in events(api_client, 'AAPL', session):
	pprint(i)
