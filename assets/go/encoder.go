package main

import (
	"encoding/base64"
	"fmt"
	"log"
	"os"
	"os/exec"
	"runtime"
)

var clear map[string]func()
var opened bool = false

func init() {
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
	if opened == false {
		CallClear()
		opened = true
	}
	var Input int
	cmd := exec.Command("cmd.exe", "/c", "title", "Encoder")
	cmd.Run()

	fmt.Print("\n" + "------ Golang Utility ------" + "\n")
	fmt.Println("\n" + "1. Encode")
	fmt.Println("2. Decode")
	fmt.Println("3. Exit")
	fmt.Print("\nNumber: ")
	fmt.Scanln(&Input)
	switch Input {
	case 1:
		CallClear()
		var Input string
		fmt.Println("\nWrite the Text to be encoded (no spaces)")
		fmt.Print("\nText: ")
		fmt.Scanln(&Input)
		Encoding := base64.StdEncoding.EncodeToString([]byte(Input))
		CallClear()
		fmt.Println("\nEncoding results: " + Encoding)
		main()
	case 2:
		CallClear()
		var Input string
		fmt.Println("\nWrite the Text to be decoded")
		fmt.Print("\nText: ")
		fmt.Scanln(&Input)
		value, err := base64.StdEncoding.DecodeString(Input)
		if err != nil {
			log.Fatal("Error: ", err)
		}
		CallClear()
		fmt.Println("\nEncoding results: " + string(value))
		main()
	case 3:
		CallClear()
		fmt.Println("\n-> Exiting")
		fmt.Print("    Code 0...")
		os.Exit(0)
	default:
		fmt.Println("Use a function from the menu ! And dont use spaces in the functions")
		fmt.Scanln()
		CallClear()
		main()
	}
}
