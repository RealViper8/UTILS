package main

import (
	"fmt"
	"os"
	"os/exec"
	"runtime"
)

var clear map[string]func()

func init() {
	clear = make(map[string]func())
	clear = make(map[string]func())
	clear["linux"] = func() {
		cmd := exec.Command("clear")
		cmd.Stdout = os.Stdout
		cmd.Run()
	}
	clear["windows"] = func() {
		cmd := exec.Command("cmd", "/c", "cls")
		cmd.Stdout = os.Stdout
		cmd.Run()
	}
}

func CallClear() {
	value, ok := clear[runtime.GOOS]
	if ok {
		value()
	} else {
		fmt.Print("\n")
	}
}

func main() {
	var i string
	fmt.Print("\n------ POINTERS ------\n")
	fmt.Println("\n1. Get input pointer")
	fmt.Println("2. Change Pointer")
	fmt.Println("3. Exit")
	fmt.Print("\nNumber: ")
	fmt.Scanln(&i)
	switch i {
	case "1":
		CallClear()
		fmt.Println("Pointer Address: ", &i)
		main()
	case "2":
		CallClear()
		fmt.Print("Change to what?: ")
		fmt.Scanln(&i)
		fmt.Println("Done")
		main()
	case "3":
		fmt.Println("\n-> Exiting ")
		fmt.Println("    Code 0...\n")
		os.Exit(0)
	}
}
