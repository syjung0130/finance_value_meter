from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import chardet

'''
아래 패키지 설치 필요
pip install chardet
'''

class HtmlRequest():
    def __init__(self):
        print("__init__, HtmlRequest")

    def set_url(self):
        '''
        https://finance.naver.com/item/coinfo.nhn?code=089010&target=finsum_more
        '''
        self.str_total_word = "https://finance.naver.com/item/coinfo.nhn?code=089010&target=finsum_more"
        print(self.str_total_word)

    # 검색결과를 요청해서 html로 가져옴
    def get_html_page(self):
        self.str_html = ""
        try:
            print('=== scrapper ===')
            self.html = urlopen(self.str_total_word).read()
            print("success..()")
            # print(self.html)

            print('*** encoding type: {0}'.format(chardet.detect(self.html)))
            encoding_type = chardet.detect(self.html)
            self.str_html = self.html.decode(encoding_type['encoding'], 'ignore')
            # print('type: {0}, html: \n{1}'.format(type(self.str_html), self.str_html))

        except HTTPError as e:
            print("exception 1")
            print(e.code)
        except URLError as e:
            print("exception 2")
            print(e.code)
    
    def get_html_str(self):
        return self.str_html
    
    def print_html(self):
        print(self.str_html)
    
    def dump_html_file(self):
        html_file = open("html_dump.html", "w")
        html_file.write(self.str_html)
        html_file.close()


    
if __name__ == "__main__":
    req = HtmlRequest()
    req.set_url()
    req.get_html_page()
    req.dump_html_file()