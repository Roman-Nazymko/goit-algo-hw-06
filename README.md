# Порівняння алгоритмів DFS та BFS для знаходження шляхів у графі країн Європи

## Опис графу
Мережа країн Європи була побудована на основі географічних позицій та відстаней між столицями країн. Граф складається з 37 вершин (країн) і 56 ребер (кордонів між країнами). Вага ребер відповідає відстаням між країнами.


### Результати DFS:

DFS: visited France
DFS: visited Spain
DFS: visited Portugal
DFS: visited Belgium
DFS: visited Netherlands
DFS: visited Germany
DFS: visited Denmark
DFS: visited Poland
DFS: visited Czech Republic
DFS: visited Austria
DFS: visited Switzerland
DFS: visited Italy
DFS: visited Slovenia
DFS: visited Hungary
DFS: visited Slovakia
DFS: visited Ukraine
DFS: visited Romania
DFS: visited Bulgaria
DFS: visited North Macedonia
DFS: visited Albania
DFS: visited Montenegro
DFS: visited Bosnia
DFS: visited Croatia
DFS: visited Serbia
DFS: visited Greece
DFS: visited Moldova
DFS: visited Russia
DFS: visited Belorussia
DFS: visited Lithuania
DFS: visited Latvia
DFS: visited Estonia
DFS: visited Finland
DFS: visited Sweden
DFS: visited Norway


### Результати BFS:

BFS: visited France
BFS: visited Spain
BFS: visited Belgium
BFS: visited Germany
BFS: visited Italy
BFS: visited Switzerland
BFS: visited Portugal
BFS: visited Netherlands
BFS: visited Denmark
BFS: visited Poland
BFS: visited Czech Republic
BFS: visited Austria
BFS: visited Slovenia
BFS: visited Ukraine
BFS: visited Belorussia
BFS: visited Lithuania
BFS: visited Slovakia
BFS: visited Hungary
BFS: visited Croatia
BFS: visited Romania
BFS: visited Moldova
BFS: visited Russia
BFS: visited Latvia
BFS: visited Serbia
BFS: visited Bosnia
BFS: visited Bulgaria
BFS: visited Finland
BFS: visited Estonia
BFS: visited North Macedonia
BFS: visited Montenegro
BFS: visited Greece
BFS: visited Sweden
BFS: visited Albania
BFS: visited Norway


***Шлях, знайдений за допомогою DFS:***
[('France', 'Spain'), ('Spain', 'Portugal'), ('France', 'Belgium'), ('Belgium', 'Netherlands'), ('Netherlands', 'Germany'), ('Germany', 'Denmark'), ('Germany', 'Poland'), ('Poland', 'Czech Republic'), ('Czech Republic', 'Austria'), ('Austria', 'Switzerland'), ('Switzerland', 'Italy'), ('Italy', 'Slovenia'), ('Slovenia', 'Hungary'), ('Hungary', 'Slovakia'), ('Slovakia', 'Ukraine'), ('Ukraine', 'Romania'), ('Romania', 'Bulgaria'), ('Bulgaria', 'North Macedonia'), ('North Macedonia', 'Albania'), ('Albania', 'Montenegro'), ('Montenegro', 'Bosnia'), ('Bosnia', 'Croatia'), ('Croatia', 'Serbia'), ('Albania', 'Greece'), ('Romania', 'Moldova'), ('Ukraine', 'Russia'), ('Russia', 'Belorussia'), ('Belorussia', 'Lithuania'), ('Lithuania', 'Latvia'), ('Latvia', 'Estonia'), ('Russia', 'Finland'), ('Finland', 'Sweden'), ('Sweden', 'Norway')]

***Шлях, знайдений за допомогою BFS:***

[('France', 'Spain'), ('France', 'Belgium'), ('France', 'Germany'), ('France', 'Italy'), ('France', 'Switzerland'), ('Spain', 'Portugal'), ('Belgium', 'Netherlands'), ('Germany', 'Denmark'), ('Germany', 'Poland'), ('Germany', 'Czech Republic'), ('Germany', 'Austria'), ('Italy', 'Slovenia'), ('Poland', 'Ukraine'), ('Poland', 'Belorussia'), ('Poland', 'Lithuania'), ('Czech Republic', 'Slovakia'), ('Austria', 'Hungary'), ('Slovenia', 'Croatia'), ('Ukraine', 'Romania'), ('Ukraine', 'Moldova'), ('Ukraine', 'Russia'), ('Belorussia', 'Latvia'), ('Hungary', 'Serbia'), ('Croatia', 'Bosnia'), ('Romania', 'Bulgaria'), ('Russia', 'Finland'), ('Latvia', 'Estonia'), ('Serbia', 'North Macedonia'), ('Bosnia', 'Montenegro'), ('Bulgaria', 'Greece'), ('Finland', 'Sweden'), ('North Macedonia', 'Albania'), ('Sweden', 'Norway')]


### Пояснення різниці

***DFS (Пошук в глибину):***
DFS досліджує якомога глибше одну гілку графа перед поверненням та переходом до наступної гілки.
Цей підхід призводить до глибшого проникнення в один напрямок, що може призвести до довшого шляху та відвідування менш важливих вузлів спочатку.
У нашому випадку, DFS досліджує всі можливі країни, починаючи з Франції, перш ніж повертатися назад до попередніх вузлів.

***BFS (Пошук в ширину):***
BFS досліджує всі сусіди поточного вузла, перш ніж переходити до вузлів наступного рівня.
Цей підхід забезпечує знаходження найкоротшого шляху в графах без ваг.
У нашому випадку, BFS відвідує країни в порядку їхньої близькості до Франції, що забезпечує більш рівномірний обхід графа.

## Висновки
DFS підходить для завдань, де потрібно досліджувати всі можливі шляхи та знайти рішення вглиб.
BFS краще підходить для знаходження найкоротшого шляху в графі без ваг, оскільки він досліджує всі вузли на кожному рівні перед переходом до наступного.
В алгоритмі Дейкстри використовуються ваги ребер, тому він знайде найкоротші шляхи з урахуванням ваг, тоді як BFS знаходить найкоротший шлях за кількістю кроків.