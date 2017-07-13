import requests
import re

def GetHTML(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoing = r.apparent_encoding
        return r.text[:400]
    except:
        return ""
        
def parsePAGE(ilt,html):
    try:
        raw_name = re.findall(r'<title>.{2,3}',html)
        name = raw_name[0].split('>')[1]
        ilt.append(name)
    except:
        print("error1")

def printTEACHER(ilt):
    mode = "{:4}\t{:6}"
    print(mode.format("序号","姓名"))
    count = 0
    for g in ilt:
        count = count +1
        print(mode.format(count,g))

def main():

    depth     = 2
    start_url = "http://info.ruc.edu.cn/academic_professor.php?teacher_id="
    infolist  = []
    for i in range(depth):
        try:
            url  = start_url + str(i+22)
            html = GetHTML(url)
            parsePAGE(infolist,html)
        except:
            continue
    printTEACHER(infolist)

main()
        
        
        
        

