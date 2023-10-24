
import re


def parser():
    n=0
    pap=1

    #  files/unzipped/2022-3-source/04/ref-s-eng.tex
    # files/unzipped/2018-1-source/06/lit-ra.tex
    # files/unzipped/2019-3-source/04/ref-s-eng.tex
    # files/unzipped/2022-1-source/07/ref-s-eng.tex
    # sources/2020-2-source/09/ref-s.tex про кавычки
    f = open('sources/2019-4-source/16/ref-s-eng.tex', 'r') #path c файлом
    worda=""
    wordb = ""
    wordc=""
    with f as myfile:
        lines = myfile.readlines()
        while not f"{pap}. " in lines[n] or not f"{{pap}}":
            if "References" in lines[n]:
                print("<div><strong>References</strong></div>")
            if "Литература" in lines[n]:
                print("<div><strong>Литература</strong></div>")
            n += 1

        i=n



        pap+=1
        while i<len(lines)-1 and not "\\vskip" in lines[i] :
            a=re.search(r"\"\{.\}", lines[i])
            b=re.search(r"\'\{.\}", lines[i])
            c = re.search(r"\\c{.\}", lines[i])
            if a!=None:
                worda=(lines[i][a.span()[0]+2])
                # print(f"\\\"{{{worda}}}")
            if b!=None:
                wordb=(lines[i][b.span()[0]+2])
                # print(f"\\\"{{{wordb}}}")
            if c!=None:
                wordc=lines[i][c.span()[0]+3]

            #  Д о к а з а т е л ь с т в о
            lines[i]=lines[i].replace("Д о к а з а т е л ь с т в о","Доказательство")

            #регексы
            lines[i] = lines[i].replace("\$\$.*?\$\$", "")
            lines[i] = lines[i].replace("\$.*?\$", "")


            # замена иноязычных символов
            lines[i]=lines[i].replace(f"\\\"{{{worda}}}",f"&{worda}uml;") # две точки сверху
            lines[i]=lines[i].replace(f"\\\'{{{wordb}}}",f"&{wordb}acute;") # штрих сверху
            lines[i]=lines[i].replace(f"\\c{{{wordc}}}",f"&{wordc}cedil;") # штрих снизу


            lines[i]=lines[i].replace("\linebreak\\newpage\\noindent","")# тэги для перехода на новую страницу в ""

            #курсив

            if ("textit" in lines[i] or "emph" in lines[i] or "\\it" in lines[i] or "\\itshape" in lines[i]) and "{" in lines[i]:
                if lines[i].find("{") < lines[i].find("textit") or lines[i].find("{") > lines[i].find("emph") or lines[i].find("{") > lines[i].find("\\it") or lines[i].find("{") > lines[i].find("\\itshape"):
                    lines[i]=lines[i].replace("\\textit{","<em>")
                    lines[i]=lines[i].replace("\\emph{","<em>")
                    lines[i] = lines[i].replace("{\it", "<em>")
                    lines[i] = lines[i].replace("{\itshape", "<em>")
                    lines[i]=lines[i].replace("}","</em>")
                    lines[i]=lines[i].replace("\\itshape","<em>")
                    lines[i] = lines[i].replace("\\upshape", "</em>")
                else:
                    lines[i] = lines[i].replace("{", "")
                    lines[i] = lines[i].replace("}", "")

            elif "{" in lines[i]:
                lines[i] = lines[i].replace("{","")
                lines[i]= lines[i].replace("}","")
            else:
                lines[i] = lines[i].replace("\\textit{", "<em>")
                lines[i] = lines[i].replace("\\emph{", "<em>")
                lines[i] = lines[i].replace("{\it", "<em>")
                lines[i] = lines[i].replace("{\itshape", "<em>")
                lines[i] = lines[i].replace("}", "</em>")
                lines[i] = lines[i].replace("\\itshape", "<em>")
                lines[i] = lines[i].replace("\\upshape", "</em>")


            #спецсимволы
            lines[i] = lines[i].replace("---", "&mdash;")
            if lines[i].find("~")>0 and lines[i][lines[i].find("~")-1]!="\\":
                lines[i]=lines[i].replace("~", "&nbsp;")
            else:
                lines[i]=lines[i][0:(lines[i].find("~")-1)]+lines[i][lines[i].find("~"):]
            lines[i]=lines[i].replace("--","&ndash;")
            lines[i]=lines[i].replace("\\-","")

            #http
            if lines[i].find("http")!=-1:
                if lines[i][len(lines[i])-1]!=" ":
                    lines[i]+=" "
                if lines[i].find("http")!=0:
                    lines[i]=lines[i][0:lines[i].find("http")-1]+" <em>"+ lines[i][lines[i].find("http"):].replace(" ","</em> ")
                else:
                    lines[i] = lines[i][0:lines[i].find("http")] + " <em>" + lines[i][
                                                                                 lines[i].find("http"):].replace(" ",
                                                                                                                 "</em> ")

            if lines[i]!="\n" and  not "%\bibitem"  in lines[i]:
                # убираю лишние \ и $
                lines[i]=lines[i].replace("\\\\","").replace("$","").replace("\\","",1000)

                print("<div class=\"ref\">"+lines[i]+"</div>")
            i+=1





if __name__ == '__main__':
    parser()



