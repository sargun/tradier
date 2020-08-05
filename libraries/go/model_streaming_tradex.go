/*
 * Tradier API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: v1
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package tradier
// StreamingTradex struct for StreamingTradex
type StreamingTradex struct {
	Cvol string `json:"cvol,omitempty"`
	Date string `json:"date,omitempty"`
	Last string `json:"last,omitempty"`
	Price string `json:"price,omitempty"`
	Size string `json:"size,omitempty"`
	Exch string `json:"exch,omitempty"`
	Symbol string `json:"symbol,omitempty"`
	Type string `json:"type,omitempty"`
}