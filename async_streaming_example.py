import os, json, asyncio, contextlib
import tradier_asyncio
from tradier_asyncio.models import StreamingQuote, StreamingTrade, StreamingSummary, StreamingTradex, StreamingTimesale

configuration = tradier_asyncio.Configuration(
	host = "https://api.tradier.com/v1",
)

configuration.access_token = os.getenv('ACCESS_TOKEN', 'YOUR PRODUCTION ACCESS TOKEN')

handlers = {
	'trade': StreamingTrade,
	'quote': StreamingQuote,
	'summary': StreamingSummary,
	'timesale': StreamingTimesale,
	'tradex': StreamingTradex
}

async def events(cm, api_client, symbols, session, filter=None, linebreak=True, validOnly=True, advancedDetails=False):
	symbols = symbols
	if isinstance(symbols, list):
		symbols = ','.join(symbols)
	payload = {
		'sessionid': session.stream.sessionid,
		'symbols': symbols,
	}
	if linebreak:
		payload['linebreak'] = 'true'
	if validOnly:
		payload['validOnly'] = 'true'
	if advancedDetails:
		payload['advancedDetails'] = 'true'
	if filter:
		payload['filter'] = 'true'

	headers = {
		'Accept': 'application/json'
	}
	async with api_client.rest_client.pool_manager.post(session.stream.url, params=payload, headers=headers) as r:
		r.raise_for_status()
		await cm.enter_async_context(r)
		content = r.content
		while True:
			line = await content.readline()
			data = json.loads(line)
			dtype = data['type']
			if dtype not in handlers:
				raise Exception(f'Received unknown {dtype}')
			yield api_client._ApiClient__deserialize(data, handlers[dtype])

async def main():
	async with tradier_asyncio.ApiClient(configuration) as api_client:
		api_instance = tradier_asyncio.DefaultApi(api_client)
		session = await api_instance.markets_events_session_post()
		async with contextlib.AsyncExitStack() as stack:
			async for i in events(stack, api_client, 'AAPL', session):
				print(f'Received event: {i}')

asyncio.run(main())