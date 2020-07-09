# tradier_python.DefaultApi

All URIs are relative to *https://sandbox.tradier.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**markets_events_session_post**](DefaultApi.md#markets_events_session_post) | **POST** /markets/events/session | 
[**markets_history_get**](DefaultApi.md#markets_history_get) | **GET** /markets/history | 
[**markets_options_chains_get**](DefaultApi.md#markets_options_chains_get) | **GET** /markets/options/chains | 
[**markets_options_expirations_get**](DefaultApi.md#markets_options_expirations_get) | **GET** /markets/options/expirations | 
[**markets_options_lookup_get**](DefaultApi.md#markets_options_lookup_get) | **GET** /markets/options/lookup | 
[**markets_options_strikes_get**](DefaultApi.md#markets_options_strikes_get) | **GET** /markets/options/strikes | 
[**markets_quotes_get**](DefaultApi.md#markets_quotes_get) | **GET** /markets/quotes | 
[**markets_quotes_post**](DefaultApi.md#markets_quotes_post) | **POST** /markets/quotes | 
[**user_profile_get**](DefaultApi.md#user_profile_get) | **GET** /user/profile | 


# **markets_events_session_post**
> InlineResponse2XX4 markets_events_session_post()



Create a streaming session for use with the Tradier Streaming API. This session can be used with the streaming endpoints to obtain updates to the market as they happen. 

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import tradier_python
from tradier_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox.tradier.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tradier_python.Configuration(
    host = "https://sandbox.tradier.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tradier_python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tradier_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradier_python.DefaultApi(api_client)
    
    try:
        api_response = api_instance.markets_events_session_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->markets_events_session_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2XX4**](InlineResponse2XX4.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_history_get**
> InlineResponse2XX5 markets_history_get(symbol, interval=interval, start=start, end=end)



Get historical pricing for a security. This data will usually cover the entire lifetime of the company if sending reasonable start/end times. You can fetch historical pricing for options by passing the OCC option symbol (ex. AAPL220617C00270000) as the symbol. 

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import tradier_python
from tradier_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox.tradier.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tradier_python.Configuration(
    host = "https://sandbox.tradier.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tradier_python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tradier_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradier_python.DefaultApi(api_client)
    symbol = None # object | 
interval = 'interval_example' # str |  (optional)
start = '2013-10-20' # date |  (optional)
end = '2013-10-20' # date |  (optional)

    try:
        api_response = api_instance.markets_history_get(symbol, interval=interval, start=start, end=end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->markets_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | [**object**](.md)|  | 
 **interval** | **str**|  | [optional] 
 **start** | **date**|  | [optional] 
 **end** | **date**|  | [optional] 

### Return type

[**InlineResponse2XX5**](InlineResponse2XX5.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_options_chains_get**
> InlineResponse2XX markets_options_chains_get(symbol, expiration, greeks=greeks)



Get all quotes in an option chain. Greek and IV data is included courtesy of ORATS. Please check out their APIs for more in-depth options data. 

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import tradier_python
from tradier_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox.tradier.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tradier_python.Configuration(
    host = "https://sandbox.tradier.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tradier_python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tradier_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradier_python.DefaultApi(api_client)
    symbol = 'symbol_example' # str | 
expiration = '2013-10-20' # date | 
greeks = True # bool |  (optional)

    try:
        api_response = api_instance.markets_options_chains_get(symbol, expiration, greeks=greeks)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->markets_options_chains_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **expiration** | **date**|  | 
 **greeks** | **bool**|  | [optional] 

### Return type

[**InlineResponse2XX**](InlineResponse2XX.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_options_expirations_get**
> InlineResponse2XX1 markets_options_expirations_get(symbol, include_all_roots=include_all_roots, strikes=strikes)



Get expiration dates for a particular underlying.  Note that some underlying securities use a different symbol for their weekly options (RUT/RUTW, SPX/SPXW). To make sure you see all expirations, make sure to send the includeAllRoots parameter. This will also ensure any unique options due to corporate actions (AAPL1) are returned. 

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import tradier_python
from tradier_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox.tradier.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tradier_python.Configuration(
    host = "https://sandbox.tradier.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tradier_python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tradier_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradier_python.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Underlying symbol of the chain
include_all_roots = False # bool | Send expirations related to all option roots (optional) (default to False)
strikes = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.markets_options_expirations_get(symbol, include_all_roots=include_all_roots, strikes=strikes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->markets_options_expirations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Underlying symbol of the chain | 
 **include_all_roots** | **bool**| Send expirations related to all option roots | [optional] [default to False]
 **strikes** | **bool**|  | [optional] [default to False]

### Return type

[**InlineResponse2XX1**](InlineResponse2XX1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_options_lookup_get**
> InlineResponse2XX3 markets_options_lookup_get(underlying)



Get all options symbols for the given underlying. This will include additional option roots (ex. SPXW, RUTW) if applicable. 

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import tradier_python
from tradier_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox.tradier.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tradier_python.Configuration(
    host = "https://sandbox.tradier.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tradier_python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tradier_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradier_python.DefaultApi(api_client)
    underlying = 'underlying_example' # str | Underlying symbol of the chain

    try:
        api_response = api_instance.markets_options_lookup_get(underlying)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->markets_options_lookup_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying symbol of the chain | 

### Return type

[**InlineResponse2XX3**](InlineResponse2XX3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_options_strikes_get**
> InlineResponse2XX2 markets_options_strikes_get(symbol, expiration=expiration)



Get an options strike prices for a specified expiration date. 

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import tradier_python
from tradier_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox.tradier.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tradier_python.Configuration(
    host = "https://sandbox.tradier.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tradier_python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tradier_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradier_python.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Underlying symbol of the chain
expiration = '2013-10-20' # date |  (optional)

    try:
        api_response = api_instance.markets_options_strikes_get(symbol, expiration=expiration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->markets_options_strikes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Underlying symbol of the chain | 
 **expiration** | **date**|  | [optional] 

### Return type

[**InlineResponse2XX2**](InlineResponse2XX2.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_quotes_get**
> Quotes markets_quotes_get(symbols, greeks=greeks)



Get a list of symbols using a keyword lookup on the symbols description. Results are in descending order by average volume of the security. This can be used for simple search functions. 

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import tradier_python
from tradier_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox.tradier.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tradier_python.Configuration(
    host = "https://sandbox.tradier.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tradier_python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tradier_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradier_python.DefaultApi(api_client)
    symbols = ['symbols_example'] # list[str] | 
greeks = True # bool |  (optional)

    try:
        api_response = api_instance.markets_quotes_get(symbols, greeks=greeks)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->markets_quotes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | [**list[str]**](str.md)|  | 
 **greeks** | **bool**|  | [optional] 

### Return type

[**Quotes**](Quotes.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_quotes_post**
> Quotes markets_quotes_post(symbols, greeks=greeks)



Get a list of symbols using a keyword lookup on the symbols description. Results are in descending order by average volume of the security. This can be used for simple search functions. 

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import tradier_python
from tradier_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox.tradier.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tradier_python.Configuration(
    host = "https://sandbox.tradier.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tradier_python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tradier_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradier_python.DefaultApi(api_client)
    symbols = 'symbols_example' # list[str] | 
greeks = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.markets_quotes_post(symbols, greeks=greeks)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->markets_quotes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | [**list[str]**](str.md)|  | 
 **greeks** | **bool**|  | [optional] [default to False]

### Return type

[**Quotes**](Quotes.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_profile_get**
> Profile user_profile_get()



The user’s profile contains information pertaining to the user and his/her accounts. In addition to listing all the accounts a user has, this call should be used to create a personalized experience for your customers (i.e. displaying their name when they log in). 

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import tradier_python
from tradier_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox.tradier.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tradier_python.Configuration(
    host = "https://sandbox.tradier.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tradier_python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tradier_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradier_python.DefaultApi(api_client)
    
    try:
        api_response = api_instance.user_profile_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->user_profile_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

