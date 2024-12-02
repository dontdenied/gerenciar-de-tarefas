package main 
import "fmt"




func main(){
	tabelabrasileiro:= map[string]int{
		"flamengo": 91,
		"santos": 80,
		"palmeiras": 72,
		"atlético": 70,
		"grêmio": 70,
		"inter": 70,
		"corinthians": 66,
		"vasco": 60,
		"fluminense": 56,
	}
	for chave, valor := range tabelabrasileiro{
		fmt.Println("time:",chave,"-> ", "pontos:", valor)
	}
	fmt.Println(tabelabrasileiro["flamengo"])
	}
