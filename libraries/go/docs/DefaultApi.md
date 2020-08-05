# \DefaultApi

All URIs are relative to *https://sandbox.tradier.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**MarketsEventsSessionPost**](DefaultApi.md#MarketsEventsSessionPost) | **Post** /markets/events/session | 
[**MarketsHistoryGet**](DefaultApi.md#MarketsHistoryGet) | **Get** /markets/history | 
[**MarketsOptionsChainsGet**](DefaultApi.md#MarketsOptionsChainsGet) | **Get** /markets/options/chains | 
[**MarketsOptionsExpirationsGet**](DefaultApi.md#MarketsOptionsExpirationsGet) | **Get** /markets/options/expirations | 
[**MarketsOptionsLookupGet**](DefaultApi.md#MarketsOptionsLookupGet) | **Get** /markets/options/lookup | 
[**MarketsOptionsStrikesGet**](DefaultApi.md#MarketsOptionsStrikesGet) | **Get** /markets/options/strikes | 
[**MarketsQuotesGet**](DefaultApi.md#MarketsQuotesGet) | **Get** /markets/quotes | 
[**MarketsQuotesPost**](DefaultApi.md#MarketsQuotesPost) | **Post** /markets/quotes | 
[**UserProfileGet**](DefaultApi.md#UserProfileGet) | **Get** /user/profile | 



## MarketsEventsSessionPost

> InlineResponse2Xx4 MarketsEventsSessionPost(ctx, )



Create a streaming session for use with the Tradier Streaming API. This session can be used with the streaming endpoints to obtain updates to the market as they happen. 

### Required Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse2Xx4**](inline_response_2XX_4.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketsHistoryGet

> InlineResponse2Xx5 MarketsHistoryGet(ctx, symbol, optional)



Get historical pricing for a security. This data will usually cover the entire lifetime of the company if sending reasonable start/end times. You can fetch historical pricing for options by passing the OCC option symbol (ex. AAPL220617C00270000) as the symbol. 

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**symbol** | **string**|  | 
 **optional** | ***MarketsHistoryGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a MarketsHistoryGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **interval** | **optional.String**|  | 
 **start** | **optional.String**|  | 
 **end** | **optional.String**|  | 

### Return type

[**InlineResponse2Xx5**](inline_response_2XX_5.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketsOptionsChainsGet

> InlineResponse2Xx MarketsOptionsChainsGet(ctx, symbol, expiration, optional)



Get all quotes in an option chain. Greek and IV data is included courtesy of ORATS. Please check out their APIs for more in-depth options data. 

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**symbol** | **string**|  | 
**expiration** | **string**|  | 
 **optional** | ***MarketsOptionsChainsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a MarketsOptionsChainsGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **greeks** | **optional.Bool**|  | 

### Return type

[**InlineResponse2Xx**](inline_response_2XX.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketsOptionsExpirationsGet

> InlineResponse2Xx1 MarketsOptionsExpirationsGet(ctx, symbol, optional)



Get expiration dates for a particular underlying.  Note that some underlying securities use a different symbol for their weekly options (RUT/RUTW, SPX/SPXW). To make sure you see all expirations, make sure to send the includeAllRoots parameter. This will also ensure any unique options due to corporate actions (AAPL1) are returned. 

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**symbol** | **string**| Underlying symbol of the chain | 
 **optional** | ***MarketsOptionsExpirationsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a MarketsOptionsExpirationsGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeAllRoots** | **optional.Bool**| Send expirations related to all option roots | [default to false]
 **strikes** | **optional.Bool**|  | [default to false]

### Return type

[**InlineResponse2Xx1**](inline_response_2XX_1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketsOptionsLookupGet

> InlineResponse2Xx3 MarketsOptionsLookupGet(ctx, underlying)



Get all options symbols for the given underlying. This will include additional option roots (ex. SPXW, RUTW) if applicable. 

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**underlying** | **string**| Underlying symbol of the chain | 

### Return type

[**InlineResponse2Xx3**](inline_response_2XX_3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketsOptionsStrikesGet

> InlineResponse2Xx2 MarketsOptionsStrikesGet(ctx, symbol, optional)



Get an options strike prices for a specified expiration date. 

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**symbol** | **string**| Underlying symbol of the chain | 
 **optional** | ***MarketsOptionsStrikesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a MarketsOptionsStrikesGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **expiration** | **optional.String**|  | 

### Return type

[**InlineResponse2Xx2**](inline_response_2XX_2.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketsQuotesGet

> Quotes MarketsQuotesGet(ctx, symbols, optional)



Get a list of symbols using a keyword lookup on the symbols description. Results are in descending order by average volume of the security. This can be used for simple search functions. 

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**symbols** | [**[]string**](string.md)|  | 
 **optional** | ***MarketsQuotesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a MarketsQuotesGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **greeks** | **optional.Bool**|  | 

### Return type

[**Quotes**](quotes.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketsQuotesPost

> Quotes MarketsQuotesPost(ctx, symbols, optional)



Get a list of symbols using a keyword lookup on the symbols description. Results are in descending order by average volume of the security. This can be used for simple search functions. 

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**symbols** | [**[]string**](string.md)|  | 
 **optional** | ***MarketsQuotesPostOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a MarketsQuotesPostOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **greeks** | **optional.Bool**|  | [default to false]

### Return type

[**Quotes**](quotes.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UserProfileGet

> Profile UserProfileGet(ctx, )



The user’s profile contains information pertaining to the user and his/her accounts. In addition to listing all the accounts a user has, this call should be used to create a personalized experience for your customers (i.e. displaying their name when they log in). 

### Required Parameters

This endpoint does not need any parameter.

### Return type

[**Profile**](profile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

