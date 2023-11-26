from bs4 import BeautifulSoup
import requests

class Crwal:
        def __init__(self,url):
                self.title_list = []
                self.url_list = []
                self.url = url # "http://www.boannews.com/"
                self.headers = {
                        'User-Agent': 'Mozilla/5.0',
                        'Content-Type': 'text/html; charset=utf-8'
                }
                self.soup = None
                
                
        def ready(self):
                req = requests.get(self.url, headers = self.headers)
                self.soup = BeautifulSoup(req.text, "lxml")
                
        def crwalTitle(self):                
                tags = self.soup.select("#headline1 > ul > li > p")
                for tag in tags:
                        self.title_list.append(tag.text)
        
        def crwalUrl(self):
                uris = self.soup.select("#headline1 > ul > li")
                for uri in uris:
                        uri_value = uri.get('onclick').split('=')[1:]
                        self.url_list.append(self.url + '='.join(uri_value).replace("'","").strip(";"))
                print(self.url_list)
                             
        
#B = Crwal()
#B.ready()
#B.crwalTitle()
#B.crwalUrl()
#print(B.title_list)
#print(B.url_list)

#https://www.boannews.com/media/view.asp?idx=123991
#https://www.boannews.com/media/view.asp?idx123991