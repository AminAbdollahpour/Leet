package main

import (
	"sort"
	"strings"
)

func isAnagram(s string, t string) bool {
	w := strings.Split(s, "")
	d := strings.Split(t, "")
	sort.Strings(w)
	sort.Strings(d)

	return strings.Join(w, "") == strings.Join(d, "")
}
