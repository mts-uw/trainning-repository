package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func NextLine() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	input := s.Text()
	l := strings.Split(input, " ")
	l = int(l)
	return l
}

func main() {
	var N, X int5
	var A []int
	fmt.Scan(&N, &X)
	fmt.Scan(&A)

	fmt.Println(N, X)
	fmt.Println(A)
}
