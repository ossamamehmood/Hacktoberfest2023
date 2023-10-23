package utils

import "regexp"

// Regex contains regex related operations
type Regex struct{}

// IsKeyValid is a funciton to check wether the provided key for the URL is valid
func (Regex) IsKeyValid(key string) bool {
	re := regexp.MustCompile(`[^\w\-._~]|\s`)
	matches := re.FindAllString(key, -1)
	if len(matches) > 0 {
		return false
	}
	return true
}
