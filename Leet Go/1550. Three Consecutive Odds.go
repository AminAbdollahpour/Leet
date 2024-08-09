package main

import "fmt"

func threeConsecutiveOdds(arr []int) bool {
	for i := 0; i < len(arr)-2; i++ {
		if arr[i]%2 != 0 && arr[i+1]%2 != 0 && arr[i+2]%2 != 0 {
			return true

		}
	}
	return false
}

func main() {
	var arr = []int{2, 6, 5, 8}
	fmt.Print(threeConsecutiveOdds(arr))
}
