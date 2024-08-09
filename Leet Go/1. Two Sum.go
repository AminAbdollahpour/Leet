package main

func twoSum(nums []int, target int) []int {
	for i, number1 := range nums {
		for j := i + 1; j < len(nums); j++ {
			if nums[j]+number1 == target {
				return []int{i, j}
			}
		}
	}
	return nil
}
