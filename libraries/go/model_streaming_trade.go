/*
 * Tradier API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: v1
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package tradier
// StreamingTrade struct for StreamingTrade
type StreamingTrade struct {
	Cvol string `json:"cvol,omitempty"`
	Date string `json:"date,omitempty"`
	Last string `json:"last,omitempty"`
	Price string `json:"price,omitempty"`
	Size string `json:"size,omitempty"`
	Symbol string `json:"symbol,omitempty"`
	Exch string `json:"exch,omitempty"`
	Type string `json:"type,omitempty"`
}
