## 보안 이슈 자동화 정리
- 보안뉴스라는 매체의 한국 보안 이슈들을 자동으로 크롤링하여 제목과, url을 자동으로 크롤링하여 엑셀파일에 저장하는 프로그램 제작.

## 사전 install 모듈 및 명령어
-  ```pip install openpyxl```
-  ```pip install requests```
-  ```pip install bs4```
-  ```pip install lxml```

## 모듈화
- Crwaling.py : 보안뉴스 사이트를 크롱링을 담당할 모듈 제작코드.
- ExcelAuto.py : 크롤링한 데이터 값으로 자동제작할 excel파일 제작코드.

## 시현
> <img width="456" alt="스크린샷 2023-11-27 오전 12 54 52" src="https://github.com/hanmin0512/auto_security_news/assets/37041208/b4cf0f5b-3519-4697-8d3a-4587de679302">
> <img width="661" alt="스크린샷 2023-11-27 오전 12 55 26" src="https://github.com/hanmin0512/auto_security_news/assets/37041208/d92b8d3c-728f-468a-bab2-1379919f00d9">
