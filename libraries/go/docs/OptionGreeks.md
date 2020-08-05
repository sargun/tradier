# OptionGreeks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Delta** | **float64** | Delta (Δ) represents the rate of change between the option&#39;s price and a $1 change in the underlying asset&#39;s price. | [optional] 
**Gamma** | **float64** | Gamma (Γ) represents the rate of change between an option&#39;s delta and the underlying asset&#39;s price. | [optional] 
**Thetha** | **float64** | Theta (Θ) represents the rate of change between the option price and time, or time sensitivity - sometimes known as an option&#39;s time decay. | [optional] 
**Vega** | **float64** | Vega (v) represents the rate of change between an option&#39;s value and the underlying asset&#39;s implied volatility. | [optional] 
**Rho** | **float64** | Rho (p) represents the rate of change between an option&#39;s value and a 1% change in the interest rate. | [optional] 
**Phi** | **float64** | Phi indicates the expected change in the option premium due to a small change in the foreign currency interest rate. | [optional] 
**BidIv** | **float32** | Bid implied volatility | [optional] 
**MidIv** | **float32** | Mid implied volatility | [optional] 
**AskIv** | **float32** | Ask implied volatility | [optional] 
**SmvVol** | **float32** | ORATS final implied volatility | [optional] 
**UpdatedAt** | [**time.Time**](time.Time.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


