import requests
import bs4

URL = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

new = html.find("div", {'class' : 'num knum5'})
new_count = new.find("p", {'class':'counter'})
korea = html.find("div", {'class' : 'num knum1'})
korea_count = korea.find("p", {'class':'counter'})
healing = html.find("div", {'class' : 'num knum4'})
healing_count = healing.find("p", {'class':'counter'})

finished = html.find("div", {'class' : 'num knum3'})
finished_count = finished.find("p", {'class':'counter'})
dead = html.find("div", {'class' : 'num knum2'})
dead_count = dead.find("p", {'class':'counter'})
print("신규확진자수:"+ new_count.text + "   총확진자수:"+ korea_count.text + "  치료중: " + healing_count.text + "   퇴원수: "+ finished_count.text + "   사망수: " + dead_count.text)
