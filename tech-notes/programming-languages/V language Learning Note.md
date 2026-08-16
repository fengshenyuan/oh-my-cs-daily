## V 0.2.4 language Learning Note
(1). println function does not support print multiple variables
```v
a := 0x7B
b := 0b01111011
c := 0o173
println(a, b, c)  // error: expected 1 arguments, but got 3
```

(2). integer will stack overflow
```v
a := i64(123)
b := byte(42)
c := i8(128) // -128
```

(3). why we need 3 different array delete func
```v
a.delete_many(start, size) removes size consecutive elements beginning with index start – triggers reallocation

a.delete(index) equivalent to a.delete_many(index, 1)

a.delete_last() remove last element from array

```

(4). no reverse indexing yet
```v
println(names[-1]) // error: negative index `-1`
```

(5). array sort need improvement => unified sort api. The sort & sort_with_compare is not unified and numbers.sort(a > b) is not strightforward like python-style
- the param of sort should be unified to a function
- better to accept python or sql style sorting(given the name of field and the order of each field)
```v
mut numbers := [1, 3, 2]
numbers.sort() // 1, 2, 3
numbers.sort(a > b) // 3, 2, 1
println(numbers)

struct User {
	age  int
	name string
}

mut users := [User{21, 'Bob'}, User{20, 'Zarkon'}, User{25, 'Alice'}]
users.sort(a.age < b.age) // sort by User.age int field
users.sort(a.name > b.name) // reverse sort by User.name string field

println(users)


struct User {
	age  int
	name string
}

mut users := [User{21, 'Bob'}, User{65, 'Bob'}, User{25, 'Alice'}]

custom_sort_fn := fn (a &User, b &User) int {
	// return -1 when a comes before b
	// return 0, when both are in same order
	// return 1 when b comes before a
	if a.name == b.name {
		if a.age < b.age {
			return 1
		}
		if a.age > b.age {
			return -1
		}
		return 0
	}
	if a.name < b.name {
		return -1
	} else if a.name > b.name {
		return 1
	}
	return 0
}
users.sort_with_compare(custom_sort_fn)

```

(6). map has default value when nothing given: can be improved
```v
mut m := map[string]int{}
m['a'] = 1
m['b'] = 2
println(m['a'])
println(m['not_a'] // default value?
println('a' in m)
println('ab' in m)
println(m.keys())
```

(7). Bugs: when run in watch mode and os.input module, the terminal does give a response after type a word
```v
import os

fn main() {
	// read text from stdin
	name := os.input('Enter your name: ')
	println('Hello, $name!')
}

2021-10-20 17:51:44.221: "/Users/yuanguo/workspace/learnpool/v/v" run variables.v | pid:   97839 | reload cycle:     0
Enter your name: yuan
--> no respnose here
```

(8). if expression?
```v
num := 777
s := if num % 2 == 0 { 'even' } else { 'odd' }
println(s)
// "odd"
```

(9). V closure works fine
```v
mut i := 1
my_closure := fn [mut i] () int {
	return i++
}

println(my_closure())  // 1
println(my_closure())  // 2
println(my_closure())  // 3, the inner i changed as expected
println(i)   // 1, this outer i doesn't change
```

(10). i++ return i before added
```v
fn new_counter() fn () int {
	mut i := 1
	return fn [mut i] () int {
		x := i++
		println('x = $x')
		println('i = $i')
		return i
	}
}

c := new_counter()
c(), c(), c()

// output:
// x = 1
// i = 2
// x = 2
// i = 3
// x = 3
// i = 4

```

(11). else if is too strange: there are 3 keyword in one line but only one variable
```v
interface Something {}

fn announce(s Something) {
	if s is Dog {
		println('a $s.breed dog') // `s` is automatically cast to `Dog` (smart cast)
	} else if s is Cat {
		println('a $s.breed cat')
	} else {
		println('something else')
	}
}
```

(12).maybe better syntax, since we already have or syntax for error handling
```v
import net.http

fn f(url string) ?string {
	resp := http.get(url) ?  // http.get(url) or ?
	return resp.text
}
```

(13). channel needs to be improved
```v
ch := chan int{cap: 1}
ch2 := chan f64{cap: 1}
n := 5
// push
ch <- n
ch2 <- 7.3
// ch2 <- 7.4 this won't response anything value to investitage
mut y := f64(0.0)
m := <- ch // pop creating new variable
y = <- ch2 // pop into existing variable
println(m)
println(y)

ch2 <- 7.4
println(<- ch2) // channel can be reused
```

(14). library json has some issues
```v
import json
struct User {
	name string [required]
	age int
	foo Foo [skip]
	last_name string [json: lastName]
}

data := '{"name": "yuanguo", "age": 18, "lastName": "Guo"}'
user := json.decode(User, data) or {
	eprintln('failed to decode json, error: $err')
	return
}

println(user.foo)
```
After decode, the Foo has a default value `x: 32767`. It doesn't make sense to give it a init value and can be printed.

```v
User{
    name: 'yuanguo'
    age: 18
    foo: Foo{
        x: 32767
    }
    last_name: 'Guo'
}
```
