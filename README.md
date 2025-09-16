# python_labs

## Лабораторная работа 1

### Задание 1

```python
  name = input("Имя: ")
  years = int(input("Возраст: "))
  next_year = years + 1
  print(f"Привет, {name}! Через год тебе будет {next_year}.")
```

![ex1!](/images/lab1/ex1.png)

### Задание 2

```python
  num1 = float(input("a: ")) 
  num2 = float(input("b: ")) 
  summ = num1 + num2 
  avg = (num1 + num2) / 2 
  print(f"sum={summ:.2f}; avg={avg:.2f}") 
```

![ex2!](/images/lab1/ex2.png)

### Задание 3

```python
  price = float(input())
  discount = float(input()) 
  vat = float(input()) 
  base = price*(1-discount/100)
  vat_amount = base*(vat/100) 
  total = base + vat_amount 
  print(f"База после скидки: {base:.2f} ₽") 
  print(f"НДС: {vat_amount:.2f} ₽") 
  print(f"Итого: {total:.2f} ₽") 
```

![ex3!](/images/lab1/ex3.png)

### Задание 4

```python
  m = int(input("Минуты: "))
  hours = m // 60 
  minutes = m % 60 
  print(f"{hours}:{minutes:02d}") 
```

![ex4!](/images/lab1/ex4.png)

### Задание 5

```python
user_name = input(' ').split()
name = ' '.join(user_name)
print(f"ФИО: {name}")
print('Инициалы: {}{}{}'.format(user_name[0][0], user_name[1][0], user_name[2][0]))
print(f"Длина (символов): {len(name)-2}")
```

![ex5!](/images/lab1/ex5.png)
