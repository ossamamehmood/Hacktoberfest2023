package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}
func main() {
	fmt.Println("Happy Hacktoberfest 2023 to everyone! -- jahway603\n")
	fmt.Println("Let's run a goroutine!!!\n")

	f("direct")

	go f("goroutine")

	go func(msg string) {
		fmt.Println(msg)
	}("going")

	time.Sleep(time.Second)
	fmt.Println("done")

	fmt.Println("\nEveryone have fun!")
}
