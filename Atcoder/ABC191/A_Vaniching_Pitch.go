package main

import "fmt"

func is_hitting_ok(v, t, s, d float64) string {
	hitting_time := d / v

	if hitting_time >= t && hitting_time <= s {
		return "No"
	} else {
		return "Yes"
	}
}

func main() {
	var V, T, S, D float64
	fmt.Scan(&V, &T, &S, &D)
	fmt.Println(is_hitting_ok(V, T, S, D))
}
