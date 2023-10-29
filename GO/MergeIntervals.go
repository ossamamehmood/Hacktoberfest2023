package main

import (
    "fmt"
    "sort"
)

type Interval struct {
    Start int
    End   int
}

func merge(intervals []Interval) []Interval {
    if len(intervals) == 0 {
        return nil
    }

    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i].Start < intervals[j].Start
    })

    merged := []Interval{intervals[0]}

    for i := 1; i < len(intervals); i++ {
        if merged[len(merged)-1].End >= intervals[i].Start {
            merged[len(merged)-1].End = max(merged[len(merged)-1].End, intervals[i].End)
        } else {
            merged = append(merged, intervals[i])
        }
    }

    return merged
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    intervals := []Interval{{1, 3}, {2, 6}, {8, 10}, {15, 18}}
    merged := merge(intervals)
    fmt.Println("Merged Intervals:", merged)
}
