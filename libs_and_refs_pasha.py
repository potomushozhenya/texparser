import re

import os

def parser(fRead, fWrite):
    n = 0
    pap = 1
    with fRead as myfile:



        lines = myfile.readlines()


        while not f"{pap}. " in lines[n] and not f"{{{pap}}}. " in lines[n] and not f"{pap}.~" in lines[n] and not f"{pap}.\\" in lines[n] and n<len(lines)-1:
            if "References" in lines[n]:
                fWrite.write("<div><strong>References</strong></div>")
            if "Литература" in lines[n]:
                fWrite.write("<div><strong>Литература</strong></div>")
            n += 1
        i = n
        pap += 1
        while i < len(lines) - 1 and not "\\vskip" in lines[i]:

            if re.search("\$\$.*?\$\$",lines[i]+lines[i+1])!=None:
                lines[i]=re.sub("\$\$.*?\$\$","",lines[i])

            if re.search("\$\$.*?",lines[i]+lines[i+1])!=None:
                lines[i]=re.sub("\$\$.*?","",lines[i])
            if re.search(".*?\$\$", lines[i] + lines[i + 1]) != None:
                lines[i]=re.sub(".*?\$\$","",lines[i])

            if re.search("\$.*?\$", lines[i] + lines[i + 1]) != None:
                lines[i]=re.sub("\$.*?\$","",lines[i])
            if re.search("\$.*?", lines[i] + lines[i + 1]) != None:
                lines[i] = re.sub("\$.*?", "", lines[i])
            if re.search(".*?\$", lines[i] + lines[i + 1]) != None:
                lines[i] = re.sub(".*?\$", "", lines[i])



            while True:
                a=re.search(r"\"\{.\}", lines[i])
                if a == None:
                    break
                worda = (lines[i][a.span()[0] + 2])
                lines[i] = lines[i].replace(f"\\\"{{{worda}}}", f"&{worda}uml;")  # две точки сверху

                # print(f"\\\"{{{worda}}}")
            while True:
                b = re.search(r"\'\{.\}", lines[i])
                if b == None:
                    break

                wordb = (lines[i][b.span()[0] + 2])
                lines[i] = lines[i].replace(f"\\\'{{{wordb}}}", f"&{wordb}acute;")  # штрих сверху

                # print(f"\\\"{{{wordb}}}")
            while True:
                c = re.search(r"\\c{.\}", lines[i])
                if c == None:
                    break
                wordc = lines[i][c.span()[0] + 3]
                lines[i] = lines[i].replace(f"\\c{{{wordc}}}", f"&{wordc}cedil;")  # штрих снизу

            while True:
                d = re.search(r"\\v{.\}", lines[i])
                if d == None:
                    break
                wordd = lines[i][d.span()[0] + 3]
                lines[i] = lines[i].replace(f"\\v{{{wordd}}}", f"&{wordd}caron;")  # галочка снизу
            while True:
                e = re.search(r"\\\".", lines[i])
                if e == None:
                    break
                worde = lines[i][e.span()[0] + 2]

                lines[i] = lines[i].replace(f"\\\"{worde}", f"&{worde}uml;")  # две точки сверху
            while True:
                f = re.search(r"\\\'.", lines[i])
                if f == None:
                    break
                wordf = lines[i][f.span()[0] + 2]

                lines[i] = lines[i].replace(f"\\'{wordf}", f"&{wordf}acute;")  # две точки сверху

            while True:
                g = re.search(r"{\\.}", lines[i])
                if g == None:
                    break
                wordg = lines[i][g.span()[0] + 2]

                lines[i] = lines[i].replace(f"{{\\{wordg}}}", f"&{wordg}strok;")  # две точки сверху
            while True:
                g = re.search(r"\\~.", lines[i])
                if g == None:
                    break
                wordg = lines[i][g.span()[0] + 2]

                lines[i] = lines[i].replace(f"\\~{wordg}", f"&{wordg}tilde;")  # две точки сверху

            # if e != None:
            #     for j in e.span():
            #         worde = lines[i][j]

            #  Д о к а з а т е л ь с т в о
            lines[i] = lines[i].replace("Д о к а з а т е л ь с т в о", "Доказательство")



            #спецсимволы

            lines[i] = lines[i].replace("{\\textquoteright}", "'")
            lines[i] = lines[i].replace("%\end{thebibliography}", "")
            # lines[i] = lines[i].replace("%\\", "")


            # замена иноязычных символов

            # lines[i] = lines[i].replace(f"\\\"{{{worda}}}", f"&{worda}uml;")  # две точки сверху

            if lines[i].find("%")!=-1 and lines[i][lines[i].find("%")-1]!="\\":
                lines[i]=lines[i][:lines[i].find("%")]




            lines[i] = lines[i].replace("\linebreak\\newpage\\noindent", "")  # тэги для перехода на новую страницу в ""

            # курсив
            # while ("textit" in lines[i] or "emph" in lines[i] or "\\it" in lines[i] or "\\itshape" in lines[i]) or re.search("/[textit\\\emph]/g{/[\\\]/g",lines[i])!=None:
            if ("textit" in lines[i] or "emph" in lines[i] or "\\it" in lines[i] or "\\itshape" in lines[i] or "\\mbox{" in lines[i] or "\\textnormal{" in lines[i] or  "{\\em" in lines[i]) and re.search(r'(?<![textit/emph]){(?!\\)', lines[i]) != None:
                if (re.search(r'(?<![textit/emph]){(?!\\)', lines[i]).span()[0] > lines[i].find("textit") and lines[i].find("textit") != -1) or (re.search(r'(?<![textit/emph]){(?!\\)', lines[i]).span()[0] > lines[i].find("emph") and lines[i].find("emph") != -1) or (re.search(r'(?<![textit/emph]){(?!\\)', lines[i]).span()[0] > lines[i].find("\\it") and lines[i].find("\\it") != -1) or (re.search(r'(?<![textit/emph]){(?!\\)', lines[i]).span()[0] > lines[i].find("\\itshape") and lines[i].find("\\itshape") != -1) or (re.search(r'(?<![textit/emph]){(?!\\)', lines[i]).span()[0] > lines[i].find("\\textnormal{") and lines[i].find("\\textnormal{") != -1) or (re.search(r'(?<![textit/emph]){(?!\\)', lines[i]).span()[0] > lines[i].find("emph") and lines[i].find("emph") != -1)or (re.search(r'(?<![textit/emph]){(?!\\)', lines[i]).span()[0] > lines[i].find("{\\em") and lines[i].find("{\\em") != -1):
                    lines[i] = lines[i].replace("\\textit{", "<em>")
                    lines[i] = lines[i].replace("\\emph{", "<em>")
                    lines[i] = lines[i].replace("{\it", "<em>")
                    lines[i] = lines[i].replace("{\itshape", "<em>")
                    lines[i] = lines[i].replace("}", "</em>")
                    lines[i] = lines[i].replace("\\itshape", "<em>")
                    lines[i] = lines[i].replace("\\upshape", "</em>")
                    lines[i] = lines[i].replace("\\mbox{", "<em>")
                    lines[i] = lines[i].replace("\\textnormal{", "<em>")
                    lines[i] = lines[i].replace("{\\em", "<em>")
                else:
                    lines[i] = lines[i].replace("{", "")
                    lines[i] = lines[i].replace("}", "")

            elif re.search(r'(?<![textit/emph]){(?!\\)', lines[i]) != None:
                lines[i] = lines[i].replace("{", "")
                lines[i] = lines[i].replace("}", "")
            else:
                lines[i] = lines[i].replace("\\textit{", "<em>")
                lines[i] = lines[i].replace("\\emph{", "<em>")
                lines[i] = lines[i].replace("{\it", "<em>")
                lines[i] = lines[i].replace("{\itshape", "<em>")
                lines[i] = lines[i].replace("}", "</em>")
                lines[i] = lines[i].replace("\\itshape", "<em>")
                lines[i] = lines[i].replace("\\upshape", "</em>")
                lines[i] = lines[i].replace("\\mbox{", "<em>")
                lines[i] = lines[i].replace("\\textnormal{", "<em>")
                lines[i] = lines[i].replace("{\\em", "<em>")


            # спецсимволы
            lines[i] = lines[i].replace("---", "&mdash;")


            if lines[i].find("~")!=-1:
                if lines[i].find("~") > 0 and lines[i][lines[i].find("~") - 1] != "\\":
                    lines[i] = lines[i].replace("~", "&nbsp;",20)
                else:
                    lines[i] = lines[i][0:(lines[i].find("~") - 1)] + lines[i][lines[i].find("~"):]
            lines[i] = lines[i].replace("--", "&ndash;")
            lines[i] = lines[i].replace("\\-", "")

            # http
            if lines[i].find("http") != -1:
                if lines[i][len(lines[i]) - 1] != " ":
                    lines[i] += " "
                if lines[i].find("http") != 0:
                    lines[i] = lines[i][0:lines[i].find("http") - 1] + " <em>" + lines[i][lines[i].find("http"):].replace(" ", "</em> ")
                else:

                    lines[i] = lines[i][0:lines[i].find("http")] + " <em>" + lines[i][lines[i].find("http"):].replace(" ", "</em> ")
                    if lines[i].find("</em>")==-1:
                        lines[i]+="</em>"

            if lines[i] != "\n" and not "bibitem" in lines[i]:
                # убираю лишние \ и $
                lines[i] = lines[i].replace("\\\\", "").replace("$", "").replace("\\", "", 1000)

                fWrite.write("<div class=\"ref\">" + lines[i] + "</div>")
            i += 1
