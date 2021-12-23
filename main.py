from urllib.request import urlopen
from bs4 import BeautifulSoup

print("\nhttps://quasarzone.com/bbs/qb_tsy\n")

html = urlopen("https://quasarzone.com/bbs/qb_tsy")
bs_object = BeautifulSoup(html, "html.parser")

titles = bs_object.select('span.ellipsis-with-reply-cnt')

index = 0
for i in titles:
    index += 1
    print(str(index) + ", " + i.text)
    if index >= 5:
        break

print("\nhttps://quasarzone.com/bbs/qb_saleinfo?_method=post&type=&page=1&_token=d9SsVDLwl08Wao7RlTuhAQ2giLhF3LdlWsu1KPtg&category=&popularity=&kind=subject&keyword=3070&sort=num%2C+reply&direction=DESC\n")

html2 = urlopen("https://quasarzone.com/bbs/qb_saleinfo?_method=post&type=&page=1&_token=d9SsVDLwl08Wao7RlTuhAQ2giLhF3LdlWsu1KPtg&category=&popularity=&kind=subject&keyword=3070&sort=num%2C+reply&direction=DESC")
bs_objec2 = BeautifulSoup(html2, "html.parser")

titles2 = bs_objec2.select('span.ellipsis-with-reply-cnt')

index2 = 0
for i in titles2:
    index2 += 1
    print(str(index2) + ", " + i.text)
    if index2 >= 5:
        break