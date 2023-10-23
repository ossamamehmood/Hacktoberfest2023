// Package schemas contains various schemas that are used to deal with the relational database
package schemas

// Response is the general response that should be forwarded to the client
type Response struct {
	Status  string `json:"status"`
	Message string `json:"message"`
}
