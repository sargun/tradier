# This code is manually written by Sargun!

import requests, requests_async, json
from tradier_python import ApiClient


from tradier_python.models import StreamingQuote, StreamingTrade, StreamingQuote, StreamingSummary, StreamingTradex, StreamingTimesale
handlers = {
	'trade': StreamingTrade,
	'quote': StreamingQuote,
	'summary': StreamingSummary,
    'timesale': StreamingTimesale,
	'tradex': StreamingTradex
}

def events(api_client : ApiClient, symbols, session, filter=None, linebreak=True, validOnly=True, advancedDetails=False):
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


async def async_events(api_client : ApiClient, symbols, session, filter=None, linebreak=True, validOnly=True, advancedDetails=False):
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
	r = requests_async.post(session.stream.url, stream=True, params=payload, headers=headers)
	r.raise_for_status()
	async for line in r.iter_lines():
		if line:
			data = json.loads(line)
			dtype = data['type']
			if dtype not in handlers:
				raise Exception(f'Received unknown {dtype}')
			yield api_client._ApiClient__deserialize(data, handlers[dtype])
