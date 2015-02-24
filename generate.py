#!/usr/bin/env python
import calendar
import subprocess

#TODO: get year as parameter
year=2015

#TODO: get Day/Month names via Locale
days = ["Lunedi", "Martedi", "Mercoledi", "Giovedi", "Venerdi", "Sabato", "Domenica"]
months = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
notices = "Notizie"
#days_de = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

#TODO: get start of week as parameter
calObj = calendar.Calendar()
cal = calObj.yeardatescalendar(year, 12)

def generateAndWrite ():
    tex = generateTex()
    outputFile = open('calendar.tex', 'w')
    outputFile.write(tex)
    subprocess.call(["pdflatex", "calendar.tex"])

def generateTex ():
    tex = documentHeader()
    tex += generateYear(2015)
    tex += '\end{document}'
    return tex

def documentHeader ():
    tex="""\documentclass[a4paper]{minimal}

\\newenvironment{tightcenter}{%
  \setlength\\topsep{0pt}
  \setlength\parskip{0pt}
  \\begin{center}
}{%
  \end{center}
}

\\usepackage[
  top=15mm,
  bottom=15mm,
]{geometry}


\\begin{document}
        """
    return tex

def generateYear (year):
    weekNum = 0
    monthNum = 0
    tmpWeek = []
    tex = ''

    for year in cal:
        for month in year:
            monthNum += 1
            for week in month:
                if tmpWeek != week:
                    weekNum += 1
                    tex += generateWeek(monthNum, weekNum, week)
                tmpWeek = week
    return tex

def generateWeek (monthNum, weekNum, week):
    #print('DEBUG generateWeek', monthNum, weekNum, week)
    week1=week[:4]
    week2=week[4:]

    weekTex=''
    weekTex += '\\newpage'

    #front
    weekTex += generatePageHeader(week[0])

    weekTex += '\\begin{flushright}'
    for day in week[:4]:
        weekTex += generateDay(day)
    weekTex += '\end{flushright}'
    weekTex += '\\newpage'

    #back
    weekTex += generatePageHeader(week[4])
    for day in week[4:]:
        weekTex += generateDay(day)

    weekTex += generateNotices()

    return(weekTex)

def generatePageHeader (firstDay):
    tex = ''
    tex += '\\begin{tightcenter}'
    tex += '{\\fontsize{1cm}{0em}\selectfont ' + months[firstDay.month-1] + ' ' + str(firstDay.year) + '}'
    tex += '\end{tightcenter}'
    return tex

def generateDay (day):
    tex = '\\noindent\\rule{\\textwidth}{1mm}\n'
    tex +='\\\\[1mm]\n'
    tex +='{\\fontsize{1cm}{1em}\selectfont '+ days[day.weekday()] + ' ' + str(day.day) + '}'
    tex += """
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
    """
    return tex

def generateNotices ():
    tex = '\\noindent\\rule{\\textwidth}{1mm}\n'
    tex +='\\\\[1mm]\n'
    tex +='{\\fontsize{1cm}{1em}\selectfont '+ notices + '}'
    tex += """
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
\\noindent\\rule{\\textwidth}{0.01mm}
\\\\[1em]
    """
    return tex

if __name__ == "__main__":
    generateAndWrite()
