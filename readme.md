
# Polyclinic

```
This program generates a synthetic dataset that imitates real data
```


## Roadmap

- [x] `class Row`
- [ ] `class Row` limits
- [ ] `class Dataset`
- [ ] `class Dataset` limits
- [ ] `.xlsx` output


## Table "Row"

| №    | Property                | Sample                   | Limits                                 |
|------|-------------------------|--------------------------|----------------------------------------|
|      |                         |                          |                                        |
| `01` | `fio`                   | `Иванов Иван Иванович`   | `Словарь` `*`                          |
|      |                         |                          |                                        |
| `02` | `passport`              | `1234 123456`            | `* ID` `RUS/BEL/KAZ`                   |
| `03` | `snils`                 | `123-456-789 12`         | `* ID`                                 |
|      |                         |                          |                                        |
| `04` | `symp_type`             | `боль в горле`           | `Комбинация (1-10)` `Словарь (5000)`   |
|      |                         |                          |                                        |
| `05` | `doctor_type`           | `лор`                    | `Словарь (50)`                         |
|      |                         |                          |                                        |
| `06` | `doctor_date `          | `2020-01-22T08:30+03:00` | `Раб.время`                            |
|      | `doctor_next_date`      | `2020-01-25T12:30+03:00` | `tests_date + 1 day`                   |
|      |                         |                          |                                        |
| `07` | `tests_type`            | `мазок на ковид`         | `Комбинация (0-5)` `Словарь (250)`     |
|      |                         |                          |                                        |
| `08` | `tests_date`            | `2020-01-24T09:30+03:00` | `doctor_date + 1~3 days` `Раб.время`   |
|      |                         |                          |                                        |
| `09` | `tests_price`           | `2000 руб.`              | `Рубли`                                |
|      |                         |                          |                                        |
| `10` | `card_num`              | `1234 5678 1234 5678`    | `UI: вероятн. (банк, платеж.сист.)`    |


## More

Не менее `50 000` строк  
Пациенты могут повторяться  
Карты могут повторяться `(1-5)`  


## Links

data  
`└──` male  
`│    ├──` [name.txt](https://sevabashirov.livejournal.com/655717.html)  
`│    └──` [surname.txt](http://www.rusinkg.ru/russkij-yazyk/article/42-russkij-yazyk-v-mire/6164-samye-rasprostranennye-russkie-familii-rejting-500)  
`├──` female  
`│    ├──` [name.txt](https://sevabashirov.livejournal.com/655717.html) 
`│    └──` surname.txt


```
parser: data/male/surname.txt -> data/female/surname.txt + data/male/surname_tmp.txt

если (surname[:2] == "ов" | "ев" | "ин"):
    surname+"a" -> female/surname.txt
иначе:
    surname -> male/surname_tmp.txt
    # обработаю вручную
```
