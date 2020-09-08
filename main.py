from bs4 import BeautifulSoup, SoupStrainer, Tag
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ROOT = 'http://courses.duytan.edu.vn'
url_search = 'http://courses.duytan.edu.vn/Modules/academicprogram/CourseResultSearch.aspx'
parameters = {
    'keyword2': 'cs 316',
    'scope': '1',  # hoc ky 1
    'hocky': '70', # hoc ky thu 70
    't': '1596604349555'
}
user_input = 'CS316202001020'
r = requests.get(url_search, parameters)
soup = BeautifulSoup(r.text, 'lxml')
url_to_subject = soup.find_all(class_='hit')[2]['href']


def get_url_subject_page(sub_id: str) -> str:
    """This function returns a url which accesses to the subject page"""
    r = requests.get(url_search, parameters)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup.find_all(class_='hit')[2]['href']


def get_page_source(url: str) -> str:
    """This function returns a `string` which contains the html of page."""
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    return soup.prettify()


def find_id(html: str, id_: str) -> Tag:
    def filter_subid(tag: Tag):
        return str(tag.find_all('td')[1].a.get_text()).strip() == id_
    soup_trainer = SoupStrainer('tr')
    soup = BeautifulSoup(html, 'lxml', parse_only=soup_trainer)
    list_lop = soup.find_all(attrs={'class': 'lop'})
    return list(filter(filter_subid, list_lop))[0]


def show_info(row: Tag):
    td_list = row.find_all('td')
    lop = td_list[0].a.get_text().strip()
    ma = td_list[1].a.get_text().strip()
    loai_hinh = td_list[2].get_text().strip()
    try:
        cho_con_lai = td_list[3].div.get_text().strip()
    except:
        cho_con_lai = td_list[3].get_text().strip()
    han_dang_ky_start = td_list[4]('div')[0].get_text().strip()
    han_dang_ky_end = td_list[4]('div')[0].get_text().strip()
    tuan_hoc = td_list[5].get_text().strip()



    print('Tên lớp:',lop)
    print('Mã lớp học:', ma)
    print('Loai hinh:', loai_hinh)
    print('Cho con lai:', cho_con_lai)
    print('Co the dang ky tu {} den {}'.format(han_dang_ky_start, han_dang_ky_end))
    print('Tuan hoc:', tuan_hoc)



if __name__ == '__main__':
    # r = get_page_source(str(url_to_subject).replace('../..', ROOT))
    # r = requests.get(str(url_to_subject).replace('../..', ROOT))
    # with open('testok.html','w',encoding='utf-8') as f:
    #     f.write(r.text)
    # with open('test.html','r',encoding='utf-8') as f:
    #     html = f.read()
    # row = find_id(r.text, user_input)
    # show_info(row)

    print(str(url_to_subject).replace('../..', ROOT))

    # http://courses.duytan.edu.vn/Modules/academicprogram/CourseClassResult.aspx?courseid=55&semesterid=70&timespan=70&t=1596694155446