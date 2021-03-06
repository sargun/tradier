# Go API client for tradier

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

## Overview
This API client was generated by the [OpenAPI Generator](https://openapi-generator.tech) project.  By using the [OpenAPI-spec](https://www.openapis.org/) from a remote server, you can easily generate an API client.

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.GoClientCodegen

## Installation

Install the following dependencies:

```shell
go get github.com/stretchr/testify/assert
go get golang.org/x/oauth2
go get golang.org/x/net/context
go get github.com/antihax/optional
```

Put the package under your project folder and add the following in import:

```golang
import "./tradier"
```

## Documentation for API Endpoints

All URIs are relative to *https://sandbox.tradier.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**MarketsEventsSessionPost**](docs/DefaultApi.md#marketseventssessionpost) | **Post** /markets/events/session | 
*DefaultApi* | [**MarketsHistoryGet**](docs/DefaultApi.md#marketshistoryget) | **Get** /markets/history | 
*DefaultApi* | [**MarketsOptionsChainsGet**](docs/DefaultApi.md#marketsoptionschainsget) | **Get** /markets/options/chains | 
*DefaultApi* | [**MarketsOptionsExpirationsGet**](docs/DefaultApi.md#marketsoptionsexpirationsget) | **Get** /markets/options/expirations | 
*DefaultApi* | [**MarketsOptionsLookupGet**](docs/DefaultApi.md#marketsoptionslookupget) | **Get** /markets/options/lookup | 
*DefaultApi* | [**MarketsOptionsStrikesGet**](docs/DefaultApi.md#marketsoptionsstrikesget) | **Get** /markets/options/strikes | 
*DefaultApi* | [**MarketsQuotesGet**](docs/DefaultApi.md#marketsquotesget) | **Get** /markets/quotes | 
*DefaultApi* | [**MarketsQuotesPost**](docs/DefaultApi.md#marketsquotespost) | **Post** /markets/quotes | 
*DefaultApi* | [**UserProfileGet**](docs/DefaultApi.md#userprofileget) | **Get** /user/profile | 


## Documentation For Models

 - [InlineResponse2Xx](docs/InlineResponse2Xx.md)
 - [InlineResponse2Xx1](docs/InlineResponse2Xx1.md)
 - [InlineResponse2Xx1Expirations](docs/InlineResponse2Xx1Expirations.md)
 - [InlineResponse2Xx1ExpirationsExpiration](docs/InlineResponse2Xx1ExpirationsExpiration.md)
 - [InlineResponse2Xx1ExpirationsStrikes](docs/InlineResponse2Xx1ExpirationsStrikes.md)
 - [InlineResponse2Xx2](docs/InlineResponse2Xx2.md)
 - [InlineResponse2Xx2Strikes](docs/InlineResponse2Xx2Strikes.md)
 - [InlineResponse2Xx3](docs/InlineResponse2Xx3.md)
 - [InlineResponse2Xx3Symbols](docs/InlineResponse2Xx3Symbols.md)
 - [InlineResponse2Xx4](docs/InlineResponse2Xx4.md)
 - [InlineResponse2Xx4Stream](docs/InlineResponse2Xx4Stream.md)
 - [InlineResponse2Xx5](docs/InlineResponse2Xx5.md)
 - [InlineResponse2Xx5History](docs/InlineResponse2Xx5History.md)
 - [InlineResponse2Xx5HistoryDay](docs/InlineResponse2Xx5HistoryDay.md)
 - [InlineResponse2XxOptions](docs/InlineResponse2XxOptions.md)
 - [Option](docs/Option.md)
 - [OptionGreeks](docs/OptionGreeks.md)
 - [Profile](docs/Profile.md)
 - [ProfileProfile](docs/ProfileProfile.md)
 - [ProfileProfileAccount](docs/ProfileProfileAccount.md)
 - [Quote](docs/Quote.md)
 - [Quotes](docs/Quotes.md)
 - [QuotesQuotes](docs/QuotesQuotes.md)
 - [StreamingQuote](docs/StreamingQuote.md)
 - [StreamingSummary](docs/StreamingSummary.md)
 - [StreamingTimesale](docs/StreamingTimesale.md)
 - [StreamingTrade](docs/StreamingTrade.md)
 - [StreamingTradex](docs/StreamingTradex.md)


## Documentation For Authorization



## BearerAuth

- **Type**: HTTP basic authentication

Example

```golang
auth := context.WithValue(context.Background(), sw.ContextBasicAuth, sw.BasicAuth{
    UserName: "username",
    Password: "password",
})
r, err := client.Service.Operation(auth, args)
```



## Author



