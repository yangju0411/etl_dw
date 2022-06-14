# ETL and Data Warehousing Project
웹 액세스 로그를 ETL을 거쳐 데이터 웨어하우스에 적재하는 프로젝트입니다.

[데이터 파이프라인 프로젝트](https://github.com/yangju0411/datapipeline)를 진행하던 중 전통적인 ETL 과정과 웨어하우스 설계에 집중하는 부분을 따로 두고 싶어서 프로젝트를 분화시켰습니다.

따라서 이 프로젝트에서는 파이썬을 통한 데이터의 변환과 RDBMS로 설계된 데이터웨어하우스의 적재에 관한 부분만 다룹니다. 이 프로젝트 이후 자세한 파이프라인 설계는 상기한 데이터 파이프라인 프로젝트에서 진행할 예정입니다.

## 데이터 소스
데이터 소스는 NASA에서 공개한 1995년 웹 액세스 로그를 사용합니다.
해당 데이터는 1995년 7월 한 달 간의 웹 액세스 로그를 저장한 파일입니다.

원본 파일 링크: ftp://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html

# 문제 상황 가정
웹 액세스 로그가 로그 파일에 저장되며 하루마다 새로운 로그 파일을 생성해주고 로그를 새로 기록합니다.
이전 일자의 로그 파일은 추출, 변환을 거쳐 DW에 적재해야 하는 상황을 가정합니다.


# REFERENCE
## DW
[타다 (TADA) 서비스의 데이터 웨어하우스 : 태초부터 현재까지](https://speakerdeck.com/vcnc/tada-tada-seobiseuyi-deiteo-weeohauseu-taecobuteo-hyeonjaeggaji?slide=29)

[웹로그 분석을 위한 데이터 웨어하우스 시스템 구축](http://koreascience.kr/article/CFKO201035751420664.page?&lang=ko)

[데이터웨어 하우스의 차원 데이터 모델 – 예제가 포함 된 자습서](https://ko.myservername.com/dimensional-data-model-data-warehouse-tutorial-with-examples)

팩트 테이블 - 빅데이터를 지탱하는 기술 p.80, p.119

[데이터 웨어하우스 모델링 기본 개념 잡기 1편(Fact, Dimension 테이블)](https://datalibrary.tistory.com/43)

[스타 스키마와 눈송이 스키마.](https://snowturtle93.github.io/posts/%EC%8A%A4%ED%83%80-%EC%8A%A4%ED%82%A4%EB%A7%88%EC%99%80-%EB%88%88%EC%86%A1%EC%9D%B4-%EC%8A%A4%ED%82%A4%EB%A7%88/)

[데이터웨어 하우스 모델링의 스키마 유형](https://ko.myservername.com/schema-types-data-warehouse-modeling-star-snowflake-schema)
## ERD
[ERD 그리는 사이트](https://www.erdcloud.com/)

[아파치 웹서버 로그 파일 상세 분석](http://www.linuxlab.co.kr/docs/00-09-6.htm)

[팩트 테이블 채우기](https://dwbi1.wordpress.com/2015/02/09/populating-fact-tables/)

## Python
[webserver-log-file-analysis](https://www.kaggle.com/code/eliasdabbas/webserver-log-file-analysis)

[GeoIP](https://rielouo.tistory.com/13)