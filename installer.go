package main

import (
	"fmt"
	"os"
	"os/exec"
	"runtime"
)

var Reset = "\033[0m"
var Red = "\033[31m"
var Green = "\033[32m"
var Yellow = "\033[33m"
var Blue = "\033[34m"
var Purple = "\033[35m"
var Cyan = "\033[36m"
var Gray = "\033[37m"
var White = "\033[97m"

var clear map[string]func()

func init() {
	clear = make(map[string]func())
	clear["linux"] = func() {
		cmd := exec.Command("clear") //Linux example, its tested
		cmd.Stdout = os.Stdout
		cmd.Run()
	}
	clear["windows"] = func() {
		cmd := exec.Command("cmd", "/c", "cls") //Windows example, its tested
		cmd.Stdout = os.Stdout
		cmd.Run()
	}
	if runtime.GOOS == "windows" {
		Reset = ""
		Red = ""
		Green = ""
		Yellow = ""
		Blue = ""
		Purple = ""
		Cyan = ""
		Gray = ""
		White = ""
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

func install() {
	cmdStruct := exec.Command("cmd.exe", "/c", "start", "setup.bat")
	out, err := cmdStruct.Output()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(out))
}

func main() {
	CallClear()
	var i int
	cmd := exec.Command("cmd.exe", "/c", "title", "Setup")
	cmd.Run()
	fmt.Println("\n" + Cyan + "------ " + Blue + "Setup" + Cyan + " ------" + Reset + "\n")
	fmt.Println(Green + "1. Install the requirements and update pip")
	fmt.Println(Cyan + "2. Install the requirements" + Blue)
	fmt.Println("3. Update Pip")
	fmt.Println(Red + "4. Exit" + Reset + "\n")
	fmt.Print(Blue+"Number: ", Purple)
	fmt.Scanln(&i)
	fmt.Print(Reset)
	switch i {
	case 1:
		install()
		fmt.Print(Cyan + "Done " + "\n" + Blue + "Press Enter to continiue !" + Reset)
		fmt.Scanln()
		main()
	case 2:
		cmd := exec.Command("cmd.exe", "/c", "python", "-m", "pip", "install", "-r", "requirements.txt")
		out, err := cmd.Output()
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println("\n" + Green + string(out) + Reset + "\n")
		fmt.Print(Cyan + "Done " + "\n" + Blue + "Press Enter to continiue !" + Reset)
		fmt.Scanln()
		CallClear()
		main()
	case 3:
		cmdStruct := exec.Command("cmd.exe", "/c", "python", "-m", "pip", "install", "--upgrade", "pip")
		out, err := cmdStruct.Output()
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println("\n" + Green + string(out) + Reset + "\n")
		fmt.Print(Cyan + "Done " + "\n" + Blue + "Press Enter to continiue !" + Reset)
		fmt.Scanln()
		CallClear()
		main()
	case 4:
		fmt.Println("\n" + Red + "-> Exiting")
		fmt.Println(Green + "    Code 0..." + Reset + "\n")
		os.Exit(0)
	default:
		fmt.Println("Please choose something from the list !")
	}
}
