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
|  |
|  |- problems 
|  |  |- template.tex (обертка для условий с input)
|  |  |- republic-math-2014-problems.tex
|  |  |- republic-math-2014-problems.pdf
|  |  |- ...
|  |
|  |- results
|  |  |- template.tex  (обертка для результатов input)
|  |  |- republic-math-2014-results.tex
|  |  |- republic-math-2014-results.pdf
|  |  |- ...

============================

Как добавлять новую олимпиаду:
- problems/republic-math/2020.tex - условия
- results/republic-math/2020.tex - результаты
- republic.tex
   добавить строки
	\head{VI олимпиада}{Казахский национальный университет имени аль-Фараби}{Алматы}{27 марта}{2020}
	\input{problems/republic-math/2020.tex}

	\result
	\input{results/republic-math/2020.tex}
	\newpage
- year by year/list.txt
	добавить строку
	republic-math, 2020, 27 марта 2020, XX Республиканская студенческая предметная олимпиада по направлению \\ <<Математика>>, Казахский национальный университет имени аль-Фараби, г. Алматы 


============================

Выполнить:
1) pdflatex republic.tex
2) cd /year\ by\ year
3) python3 generate.py < list.txt
