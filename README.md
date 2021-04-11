# Lotto_Project_Python (개발 진행중)

Environment :
 - Google Chrome.
 - Pycharm or Python(IDLE)

Usage :
 1. Install Chromedriver.
 2. Install Module (Selenium)
 3. Install Module (OpenPyXl)


Explain :
 - 크롬 개발자도구 DOM 상의 XML Element 를 ChromeDriver & Selenium 을 이용해 Parsing.
 - Parsing 된 값은 OpenPyXl 모듈을 이용해 엑셀로 저장 ( 임시 DB로 활용 )
 - 저장된 값을 참조하여 니즈에 맞는 연산에 따라 로또번호를 추첨.


To Make Progress :
1. dhlottery 홈페이지의 최신회차 (단일 1 페이지) 에 대한 Parsing 완료.
2. 복수 페이지 (과거회차) 에 대한 Parsing 코딩중.
  - URL Query Data Testing.
