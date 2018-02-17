from selenium import webdriver
import re

def get_avg(url):
    driver.get(url)
    driver.refresh()
    print driver
    elements = driver.find_element_by_xpath("""//*[@id="splitsbody"]""")
    result = re.split(r"Grass|Clay|Hard|Cemented" ,elements.text)
    ace_percent = []
    serve_point_win_perc = []
    reverse_point_win_perc = []
    perentage_element = []
    for i ,data in enumerate(result):
        x = re.findall(r"\d+\.\d+", result[i][:])
        if not x:
            print "No__****__Value"
        else :
            perentage_element.append((x[0] ,x[5] ,x[7]))
    for i ,data in enumerate(perentage_element):
        ace_percent.append(data[0])
        serve_point_win_perc.append(data[1])
        reverse_point_win_perc.append(data[2])
    ace_values = map(lambda x:float(x),ace_percent)
    spw_values = map(lambda x:float(x),serve_point_win_perc)
    rpw_values = [float(x) for x in reverse_point_win_perc]
    if len(perentage_element) == 0:
        avg_ace ,avg_spw ,avg_rpw = 0 ,0 ,0
        return avg_ace ,avg_spw ,avg_rpw
    else :
        avg_ace = sum(ace_values ) /(len(ace_values))
        avg_spw = sum(spw_values ) /(len(spw_values))
        avg_rpw = sum(rpw_values ) /(len(rpw_values))
        print {"Ace_percent" : avg_ace, "spw_perc ": avg_spw, "reverse_point_win_perc " :  avg_rpw}
        return avg_ace ,avg_spw ,avg_rpw


driver = webdriver.Chrome()
#name = Enter from user
name = "DavidGoffin"
url = "http://www.tennisabstract.com/cgi-bin/player.cgi?p="+name+"&f=&view=singles"
print url
x,y,z = get_avg(url)
driver.close()