Структура:


math
|- republic.tex (сборник)
|
|- problems (данные)
|  |- math
|  |  |- 2014.tex
|  |  |- 2015.tex
|  |  |- ...
|  |- mcm
|  |  |- 2014.tex
|  |  |- 2015.tex
|  |  |- ...
|
|- results (данные)
|  |- math
|  |  |- 2014.tex
|  |  |- 2015.tex
|  |  |- ...
|  |- mcm
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
|  |  |- republic-math-2014-problems.png
|  |  |- ...
|  |
|  |- results
|  |  |- republic-math-2014-results.tex
|  |  |- republic-math-2014-results.pdf
|  |  |- ...


============================

Добавить олимпиаду:

1) problems/math/2020.tex - условия
2) solutions/math/2020.tex - решения
3) results/math/2020.tex - результаты
4) yby/2020.txt
	subdirectory, file, date, name, hoster, city
	math, 2020, 27 марта 2020, XII Республиканская студенческая предметная олимпиада по~направлению~<<Математика>>, Назарбаев Университет, г. Астана 
5) cd yby
6) python3 generate.py pdf 2020.txt a4.tex  ../problems/ problems/ republic- -problems
7) python3 generate.py pdf 2020.txt a4.tex  ../solutions/ solutions/ republic- -solutions
8) python3 generate.py pdf 2020.txt a4.tex  ../results/ results/ republic- -results

============================

Добавить в книгу:

1) republic.tex
   добавить строки

\head{XII олимпиада}{Назарбаев Университет}{Астана}{27 марта 2020}{2020}
\input{problems/math/2020.tex}
\result
\input{results/math/2020.tex}
\newpage

2) pdflatex republic.tex

============================

Добавить на сайт

0) cd yby
1) python3 generate.py png 2020.txt olymp-a5.tex  ../problems/ ~/http/mymath.info/math/republic/problems/ republic- -problems
   python3 generate.py pdf 2020.txt olymp-a4.tex  ../problems/ ~/http/mymath.info/math/republic/problems/ republic- -problems
2) python3 generate.py pdf 2020.txt olymp-a4.tex  ../solutions/ ~/http/mymath.info/math/republic/solutions/ republic- -solutions
3) python3 generate.py pdf 2020.txt olymp-a4-land.tex  ../results/ ~/http/mymath.info/math/republic/results/ republic- -results
4) на странице mymath.info/script/run.php сгенерировать результаты
   math/republic/results/republic-math-2020-results
5) исправить mymath.info/math/show.php
	if ($olymp == "republic")
		for ($y = 2014; $y <= 2020; $y++)

============================
