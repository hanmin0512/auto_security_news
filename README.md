# 보안 이슈 자동화 정리
- 보안뉴스라는 매체의 한국 보안 이슈들을 자동으로 크롤링하여 제목과, url을 자동으로 크롤링하여 엑셀파일에 저장하는 프로그램 제작.

# 사전 install 모듈 및 명령어
- openpyxl ```pip install openpyxl```
- openpyxl ```pip install requests```
- openpyxl ```pip install bs4```

# 모듈화
- Crwaling.py : 보안뉴스 사이트를 크롱링을 담당할 모듈 제작코드.
- ExcelAuto.py : 크롤링한 데이터 값으로 자동제작할 excel파일 제작코드.

