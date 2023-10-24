
import re


def parser(fRead, fWrite):
    n=0
    pap=1
    fWrite.write("<div><strong>Литература</strong></div>")
    #path c файлом
    worda=""
    wordb = ""
    wordc=""
    with fRead as myfile:
        lines = myfile.readlines()
        while not f"{pap}. " in lines[n]:
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
            lines[i]=lines[i].replace("\\textit{","<em>")
            lines[i]=lines[i].replace("\\emph{","<em>")
            lines[i] = lines[i].replace("{\it", "<em>")
            lines[i] = lines[i].replace("{\itshape", "<em>")
            lines[i]=lines[i].replace("}","</em>")
            lines[i]=lines[i].replace("\\itshape","<em>")
            lines[i] = lines[i].replace("\\upshape", "</em>")

            #спецсимволы
            lines[i] = lines[i].replace("---", "&mdash;")
            lines[i]=lines[i].replace("~", "&nbsp;")
            lines[i]=lines[i].replace("--","&ndash;")
            lines[i]=lines[i].replace("\\-","")

            #http
            if lines[i].find("http")!=-1:
                lines[i]=lines[i][0:lines[i].find("http")-1]+" <em>"+ lines[i][lines[i].find("http"):].replace(" ","</em> ")
            if lines[i]!="\n":
                # убираю лишние \ и $
                lines[i]=lines[i].replace("\\","").replace("$","").replace("\\\\","")

                fWrite.write("<div class=\"ref\">"+lines[i]+"</div>")
            i+=1
