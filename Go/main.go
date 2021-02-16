package main

type Human interface{
	Say()
}

type Person struct{
	Name string
}

func (p Person) Say(){
	fmt.Println(p.Name)
}

func main(){
	ver mike Human = Person{"Mike"}
	mike.Say()
}