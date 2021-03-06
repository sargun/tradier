/*
 * Tradier API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: v1
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package tradier
// StreamingTimesale struct for StreamingTimesale
type StreamingTimesale struct {
	Symbol string `json:"symbol,omitempty"`
	Exch string `json:"exch,omitempty"`
	Bid float64 `json:"bid,omitempty"`
	Ask float64 `json:"ask,omitempty"`
	Last float64 `json:"last,omitempty"`
	Size float64 `json:"size,omitempty"`
	Date string `json:"date,omitempty"`
	Seq float32 `json:"seq,omitempty"`
	Flag string `json:"flag,omitempty"`
	Cancel bool `json:"cancel,omitempty"`
	Correction bool `json:"correction,omitempty"`
	Session string `json:"session,omitempty"`
}
