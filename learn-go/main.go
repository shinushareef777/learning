package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

func firstExercise(seq string) string {
	const C int = 50
	const H int = 30
	var result string
	splitted := strings.Split(seq, ",")
	for j, i := range splitted {
		num, err := strconv.Atoi(strings.TrimSpace(i))
		if err != nil {
			fmt.Println(err, "err")
			return ""
		}
		op := (2 * C * num) / H
		sqrt := math.Sqrt(float64(op))
		rounded := int(math.Round(sqrt))
		result += strconv.Itoa(rounded)
		if j != len(splitted)-1 {
			result += ", "
		}
	}
	return result
}

func secondExercise(x int, y int) [][]int {
	var result [][]int
	for i := 0; i < x; i++ {
		var arr []int
		for j := 0; j < y; j++ {
			arr = append(arr, i*j)
		}
		result = append(result, arr)
	}
	return result
}

func thirdExercise(seq string) string {
	words := []string{}
	for _, i := range strings.Split(seq, ",") {
		words = append(words, strings.TrimSpace(i))
	}
	sort.Strings(words)
	newSeq := strings.Join(words, ",")
	return newSeq
}

func fourthExercise(lines string) string {
	return strings.ToUpper(lines)
}

func fifthExercise(seq string) string {
	words := strings.Split(seq, " ")
	var newArr []string
	contains := func(word string) bool {
		for _, j := range newArr {
			if j == word {
				return true
			}
		}
		return false
	}
	for _, i := range words {
		if contains(i) {
			continue
		} else {
			newArr = append(newArr, i)
		}
	}
	sort.Strings(newArr)
	joined := strings.Join(newArr, " ")
	return joined
}

func sixthExercise(binSeq string) string {
	seqArr := strings.Split(binSeq, ",")
	var output string
	for _, bin := range seqArr {
		binNum, err := strconv.ParseInt(bin, 2, 64)
		if err != nil {
			return ""
		}
		if binNum%5 == 0 {
			if output != "" {
				output += ","
			}
			output += bin
		}
	}
	return output
}

func seventhExercise() string {
	var output string
	for i := 100; i < 301; i++ {
		converted := strconv.Itoa(i)
		first, _ := strconv.Atoi(string(converted[0]))
		second, _ := strconv.Atoi(string(converted[1]))
		third, _ := strconv.Atoi(string(converted[2]))
		if first%2 == 0 && second%2 == 0 && third%2 == 0 {
			if output != "" {
				output += ","
			}
			output += converted
		}
	}
	return output
}

func eighthExercise(sentence string) {
	var letters int
	var digits int
	re := regexp.MustCompile("[^a-zA-Z0-9]+")
	converted := strings.Split(re.ReplaceAllString(sentence, ""), "")
	for _, i := range converted {
		if _, err := strconv.Atoi(i); err == nil {
			digits += 1
		} else {
			letters += 1
		}
	}
	fmt.Println("LETTERS: ", letters)
	fmt.Println("DIGITS: ", digits)
}

func twelthExercise() {
	m := map[int]bool{1: true, 2: false, 3: false}
	delete(m, 2)
	for k, v := range m {
		fmt.Println(k, v)
	}
}

func thirteenExercise() {
	f, err := os.Create("info.txt")
	if err != nil {
		log.Fatal("err1: ", err)
	}
	defer f.Close()
	_, err2 := f.WriteString("The Go gopher is an iconic mascot!")
	if err2 != nil {
		log.Fatal("err2: ", err2)
	}
}

func SwapValues() {
	x, y := 5.5, 8.8
	ptrx, ptry := &x, &y
	x, y = *ptry, *ptrx
	fmt.Println(x, y)
}

func main() {
	first := firstExercise("100, 150, 180")
	second := secondExercise(3, 5)
	third := thirdExercise("without, hello,bag,world")
	fourth := fourthExercise("Hello World")
	fifth := fifthExercise("hello world and practice makes perfect and hello world again")
	sixth := sixthExercise("101,0100,0011,10100,1010,1001,1111")
	seventh := seventhExercise()
	eighthExercise("hello world! 123")
	fmt.Println("first: ", first)
	fmt.Println("Second: ", second)
	fmt.Println("Third: ", third)
	fmt.Println("fourth: ", fourth)
	fmt.Println("fifth: ", fifth)
	fmt.Println("sixth: ", sixth)
	fmt.Println("seventh: ", seventh)
	twelthExercise()
	thirteenExercise()
	SwapValues()
}
