
Перевод метров в футы

```shell
package main

import (
	"fmt"
)

func main() {

	var metrs float64
	fmt.Print("Метры: ")
	fmt.Scanf("%f", &metrs)

	futs := metrs * 0.3048

	fmt.Print("Футы: ",fmt.Sprintf("%.4f", futs))	

}
```

Поиск наименьшего


```shell
package main

import (
	"fmt"
)

func main() {

	x := []float64{48, 96, 86, 68, 57, -50.22, -63, 70, 37, 34, 83, 0.22, 19, 97, 9, 1}
	min := x[0]
	for i := 1; i < len(x); i++ {
		if min > x[i] {
			min = x[i]
		}

	}

	fmt.Println("Наименьший элемент: ", min)

}
```

Вывести числа от 1 до 100, кратные 3

```shell
package main

import (
	"fmt"
)

func main() {

	startd := 1
	finishd := 100
	c := 3
	for i := startd; i <= finishd; i++ {
		if i%c == 0 {
			fmt.Print(i, ", ")
		}

	}

}
```

