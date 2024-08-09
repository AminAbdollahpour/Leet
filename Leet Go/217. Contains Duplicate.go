package main

func containsDuplicate(nums []int) bool {
	s := map[int]bool{}
	for i := 0; i < len(nums); i++ {
		s[nums[i]] = true
	}
	return len(nums) != len(s)
}
