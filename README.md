# ETL and Data Warehousing Project
웹 액세스 로그를 ETL을 거쳐 데이터 웨어하우스에 적재하는 프로젝트입니다.

[데이터 파이프라인 프로젝트](https://github.com/yangju0411/datapipeline)를 진행하던 중 전통적인 ETL 과정과 웨어하우스 설계에 집중하는 부분을 따로 두고 싶어서 프로젝트를 분화시켰습니다. 

## 데이터 소스
데이터 소스는 캐글에 공개되어 있는 웹 액세스 로그 데이터를 사용합니다.

이란의 인터넷 쇼핑몰 zanbil.ir의 액세스 로그라고 합니다.

[원본 파일 링크](https://www.kaggle.com/datasets/eliasdabbas/web-server-access-logs)

# REFERENCE
## DW
[타다 (TADA) 서비스의 데이터 웨어하우스 : 태초부터 현재까지](https://speakerdeck.com/vcnc/tada-tada-seobiseuyi-deiteo-weeohauseu-taecobuteo-hyeonjaeggaji?slide=29)

[웹로그 분석을 위한 데이터 웨어하우스 시스템 구축](http://koreascience.kr/article/CFKO201035751420664.page?&lang=ko)

[데이터웨어 하우스의 차원 데이터 모델 – 예제가 포함 된 자습서](https://ko.myservername.com/dimensional-data-model-data-warehouse-tutorial-with-examples)

팩트 테이블 - 빅데이터를 지탱하는 기술 p.80, p.119

[데이터 웨어하우스 모델링 기본 개념 잡기 1편(Fact, Dimension 테이블)](https://datalibrary.tistory.com/43)

[스타 스키마와 눈송이 스키마.](https://snowturtle93.github.io/posts/%EC%8A%A4%ED%83%80-%EC%8A%A4%ED%82%A4%EB%A7%88%EC%99%80-%EB%88%88%EC%86%A1%EC%9D%B4-%EC%8A%A4%ED%82%A4%EB%A7%88/)
## ERD
[ERD 그리는 사이트](https://www.erdcloud.com/)

[아파치 웹서버 로그 파일 상세 분석](http://www.linuxlab.co.kr/docs/00-09-6.htm)

## Python
[webserver-log-file-analysis](https://www.kaggle.com/code/eliasdabbas/webserver-log-file-analysis)

[GeoIP](https://rielouo.tistory.com/13)