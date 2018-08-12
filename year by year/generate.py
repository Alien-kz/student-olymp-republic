#! /bin/python3

import os
def replace_by_template(input_file, output_file, template, value):
	try:
		input_tex_file = open(input_file, 'r')
	except IOError:
		print("Could not open file:" + input_tex_file)
		return False
	with input_tex_file:
		text = input_tex_file.read()
		template = template.replace("<Дата>", value[0])
		template = template.replace("<Олимпиада>", value[1])
		template = template.replace("<ВУЗ>", value[2])
		template = template.replace("<Город>", value[3])
		template = template.replace("<Текст>", text)
		with open(output_file, 'w') as output_tex_file:
			output_tex_file.write(template)
		quite = " 1>/dev/null"
#		quite = ""
		return os.system("pdflatex " + output_file + quite) == 0
	return False

def make_pdf(directory, olymp, suffix):
	print(directory)
	os.chdir(directory)
	with open('template.tex', 'r') as temp_file:
		template = temp_file.read()
		for key, value in olymp.items():
			input_file = "../../" + directory + "/" +  key + suffix + ".tex"
			output_file = directory + "-" + key + ".tex"
			print(output_file, end="\t")
			print(replace_by_template(input_file, output_file, template, value))
	os.system("rm *log *aux")
	os.chdir("..")

math_rep = "Республиканская студенческая предметная олимпиада по направлению \\\\ <<Математика>>"
mcm_rep = "Республиканская студенческая предметная олимпиада по направлению \\\\ <<Математическое и компьютеное моделирование>>"

olymp = dict()
olymp["2014-rep-math"] = "27 марта 2014", "VI " + math_rep, "Казахский национальный университет имени аль-Фараби", "г. Алматы"
olymp["2015-rep-math"] = "26 марта 2015", "VII " + math_rep, "Казахский национальный университет имени аль-Фараби", "г. Алматы"
olymp["2016-rep-math"] = "01 апреля 2016", "VIII " + math_rep, "Казахстанский филиал МГУ имени М. В. Ломоносова", "г. Астана"
olymp["2017-rep-math"] = "13 апреля 2017", "IX " + math_rep, "Казахстанский филиал МГУ имени М. В. Ломоносова", "г. Астана"
olymp["2018-rep-math"] = "03 апреля 2018", "X " + math_rep, "Казахстанско-Британский технический университет", "г. Алматы"

olymp["2014-rep-mcm"] = "27 марта 2014", "VI " + mcm_rep, "Казахский национальный университет имени аль-Фараби", "г. Алматы"
olymp["2015-rep-mcm"] = "26 марта 2015", "VII " + mcm_rep, "Казахский национальный университет имени аль-Фараби", "г. Алматы"
olymp["2016-rep-mcm"] = "01 апреля 2016", "VIII " + mcm_rep, "Казахстанский филиал МГУ имени М. В. Ломоносова", "г. Астана"
olymp["2017-rep-mcm"] = "14 апреля 2017", "IX " + mcm_rep, "Назарбаев Университет", "г. Астана"
olymp["2018-rep-mcm"] = "20 апреля 2018", "X " + mcm_rep, "Назарбаев Университет", "г. Астана"


make_pdf("problems", olymp, "")
make_pdf("results", olymp, "-res")
# make_pdf("solutions", olymp, "-sol")
