Структура:

math
|- republic.tex (сборник)
|
|- problems (данные)
|  |- 2014-rep-math.tex
|  |- 2015-rep-math.tex
|  |- ...
|
|- results (данные)
|  |- 2014-rep-math-res.tex
|  |- 2015-rep-math-res.tex
|  |- ...
|
|- year by year (по годам)
|  |- generate.py (скрипт, генерирующий обертку для каждого года)
|  |
|  |- problems 
|  |  |- template.tex (обертка для условий с input)
|  |  |- problems-2014.tex
|  |  |- problems-2014.pdf
|  |  |- ...
|  |
|  |- results
|  |  |- template.tex  (обертка для результатов input)
|  |  |- results-2014.tex
|  |  |- results-2014.pdf
|  |  |- ...

============================

Как добавлять новую олимпиаду:
- problems/2020-rep-math.tex - условия
- results/2020-rep-math.tex - результаты
- republic.tex
   добавить строки
	\head{VI олимпиада}{Казахский национальный университет имени аль-Фараби}{Алматы}{27 марта}{2020}
	\input{problems/2020-rep-math.tex}

	\result
	\input{results/2020-rep-math.tex}
	\newpage
- year by year/generate.py
    добавить строки
    	olymp["2020-rep-math"] = "20 декабря 2020", math_rep;

============================

Выполнить:
1) cd math
2) pdflatex math.tex
3) cd /year\ by\ year
4) python3 generate.py
