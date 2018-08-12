Структура:

math
|- republic.tex (сборник)
|
|- problems (данные)
|  |- republic-math
|  |  |- 2014.tex
|  |  |- 2015.tex
|  |  |- ...
|  |- republic-mcm
|  |  |- 2014.tex
|  |  |- 2015.tex
|  |  |- ...
|
|- results (данные)
|  |- republic-math
|  |  |- 2014.tex
|  |  |- 2015.tex
|  |  |- ...
|  |- republic-mcm
|  |  |- 2014.tex
|  |  |- 2015.tex
|  |  |- ...
|
|- year by year (по годам)
|  |- generate.py (скрипт, генерирующий обертку для каждого года)
|  |- template.tex (обертка для условий с input)
|  |- list.txt (список олимпиад)
|  |
|  |- problems 
|  |  |- republic-math-2014-problems.tex
|  |  |- republic-math-2014-problems.pdf
|  |  |- ...
|  |
|  |- results
|  |  |- republic-math-2014-results.tex
|  |  |- republic-math-2014-results.pdf
|  |  |- ...

============================

Как добавлять новую олимпиаду:
1) problems/republic-math/2020.tex - условия
2) results/republic-math/2020.tex - результаты
3) republic.tex
   добавить строки
	\head{VI олимпиада}{Казахский национальный университет имени аль-Фараби}{Алматы}{27 марта}{2020}
	\input{problems/republic-math/2020.tex}

	\result
	\input{results/republic-math/2020.tex}
	\newpage
4) year by year/list.txt
	добавить строку
	republic-math, 2020, 27 марта 2020, XX Республиканская студенческая предметная олимпиада по направлению \\ <<Математика>>, Казахский национальный университет имени аль-Фараби, г. Алматы 


============================

Выполнить:
1) pdflatex republic.tex
2) cd /year\ by\ year
3) python3 generate.py < list.txt

============================

Добавить на сайт
1) mymath.info/math/republic/problems/republic-math-2020-problems.tex
2) mymath.info/math/republic/problems/republic-math-2020-problems.pdf
3) mymath.info/math/republic/results/republic-math-2020-results.tex
4) mymath.info/math/republic/results/republic-math-2020-results.pdf
5) mymath.info/script/run.php
math/republic/results/republic-math-2020-results
6) исправить mymath.info/math/show.php
if ($olymp == "republic")
for ($y = 2014; $y <= 2020; $y++)
