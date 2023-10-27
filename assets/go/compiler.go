package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"runtime"
	"strings"
)

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
}

func CallClear() {
	value, ok := clear[runtime.GOOS]
	if ok {
		value()
	} else {
		fmt.Print("\n")
	}
}

func javac(file string) {
	exec.Command("cmd.exe", "/c", "title", "Javac Compiler").Run()
	if !strings.Contains(file, ".java") {
		file += ".java"
	}
	cmd := exec.Command("cmd.exe", "/c", "javac", file)
	out, err := cmd.Output()
	_ = out
	cmd.Run()

	if err != nil {
		log.Fatal("Error : ", err)
	}

	fmt.Println("Done", out)
	exec.Command("cmd.exe", "/c", "java", file).Run()
	main()
}

func golang(file string) {
	exec.Command("cmd.exe", "/c", "title", "Go Compiler").Run()
	if !strings.Contains(file, ".go") {
		file += ".go"
	}
	cmd := exec.Command("cmd.exe", "/c", "go", "build", file)
	out, err := cmd.Output()
	_ = out
	cmd.Run()
	if err != nil {
		log.Fatal("Error : ", err)
	}
	fmt.Println("Done, ", out)
	exec.Command("cmd.exe", "/c", "go", "run", file).Run()
	main()
}

func python(file string) {
	exec.Command("cmd.exe", "/c", "title", "Python Compiler").Run()
	if !strings.Contains(file, ".py") || !strings.Contains(file, ".pyw") {
		file += ".py"
	}
	cmd := exec.Command("cmd.exe", "/c", "pyinstaller", "--onefile", file)
	out, err := cmd.Output()
	cmd.Run()
	if err != nil {
		log.Fatal("Error : ", err)
	}
	fmt.Println("Done, ", out)
	exec.Command("cmd.exe", "/c", "python", file)
	main()
}

func main() {
	var input int
	var file string
	CallClear()
	exec.Command("cmd.exe", "/c", "title", "Compilers").Run()
	fmt.Print("\n" + "------ COMPILER ------" + "\n")
	fmt.Println("\n1. javac compiler")
	fmt.Println("2. python compiler (pyinstaller)")
	fmt.Println("3. golang compiler")
	fmt.Print("\nNumber : ")
	fmt.Scanln(&input)
	fmt.Print("\nFile : ")
	fmt.Scanln(&file)
	switch input {
	case 1:
		javac(file)
	case 2:
		python(file)
	case 3:
		golang(file)
	}
}
