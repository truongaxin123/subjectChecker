from bs4 import BeautifulSoup
import requests
import re
from io import BytesIO


def get_url_page_course(ma_mon: str, hoc_ky: str, hoc_ky_thu: str) -> str:
    parameters = {
        'keyword2': ma_mon,
        'scope': hoc_ky,  # hoc ky 1
        'hoc_ky': hoc_ky_thu,  # hoc ky thu 70
        't': '1596604349555'
    }
    r = requests.get('http://courses.duytan.edu.vn/Modules/academicprogram/CourseResultSearch.aspx', parameters)
    print(str(BytesIO.read(BytesIO(r.content)).decode('utf-8')))
    soup = BeautifulSoup(r.text, 'lxml')
    return soup.find_all(class_='hit')

def get_url_full_html(url_page_course: str) -> str:
    'http://courses.duytan.edu.vn/Modules/academicprogram/CourseClassResult.aspx?courseid=592&semesterid=70&timespan=70&t=1596880419589'

if __name__ == '__main__':
    print(get_url_page_course('es 271', '1', '70'))