package main

import (
	"fmt"
)

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(nums, target)
	fmt.Printf("%d %d\n", result[0], result[1])
}

// twoSum returns the indexes of two numbers whose sum is equal to target
// otherwise it returns -1 -1
func twoSum(nums []int, target int) []int {
	numMap := map[int]int{}

	for k, v := range nums {
		if reqIndex, isPresent := numMap[target-v]; isPresent {
			return []int{reqIndex, k}
		} else {
			numMap[v] = k
		}
	}

	return []int{-1, -1}
}
