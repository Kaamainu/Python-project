#Convertir md en html
#crée une page html
#ouvrir le md et le lire 
#écrire dans le html 
#faire la convertion
#détection des cas spéciaux
    #Si dans ma variable "mot" '#' alors 'mot' = h1
def convertiseur():

    mdFile = open('file.md','r')

    htmlText = []
    verifyUl = False
    jumpLine = False

    lines = mdFile.read().splitlines()

    for line in lines:

        line = line.encode("latin1").decode("utf-8")

        if jumpLine :
            jumpLine = False
            htmlText.append("<br>")

        line = line.replace("**", "<b>")

        if line.startswith("# "):
            htmlText.append("<h1>" + line[2:] + "</h1>")

        elif line.startswith("## "):
            htmlText.append("<h2>" + line[3:] + "</h2>")

        elif line.startswith("### "):
            htmlText.append("<h3>" + line[4:] + "</h3>")

        elif line.startswith("http://") or line.startswith("https://"):
            htmlText.append("<a href=\"" + line + "\">" + line + "</a>")
            jumpLine = True

        elif line.startswith("- "):

            if not verifyUl:
                htmlText.append("<ul>")
                verifyUl = True

            htmlText.append("<li>" + line[2:] + "</li>")

        elif not line.startswith("- ") and (line != "" or line != None) and verifyUl:
            htmlText.append("</ul>")
            verifyUl = False

        else :
            htmlText.append(line)

    htmlFile = open("result.html", "a")

    htmlFile.close()

    htmlFile = open('result.html','w')

    for line in htmlText:
        htmlFile.write(line)
    htmlFile.close()

convertiseur()
    
