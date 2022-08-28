# ETL and Data Warehousing Project
https://mixed-speedboat-0ce.notion.site/ETL-6cf0666216734eb9b78793ab4eb48566

웹 액세스 로그를 ETL을 거쳐 데이터 웨어하우스에 적재하는 프로젝트입니다.

[데이터 파이프라인 프로젝트](https://github.com/yangju0411/datapipeline)를 진행하던 중 전통적인 ETL 과정과 웨어하우스 설계에 집중하는 부분을 따로 두고 싶어서 프로젝트를 분화시켰습니다.

따라서 이 프로젝트에서는 파이썬을 통한 데이터의 변환과 RDBMS로 설계된 데이터웨어하우스의 적재에 관한 부분만 다룹니다. 인프라 구성에 대한 부분은 다루지 않으며 py와 sql 파일만을 결과물로 내놓을 것입니다.

이 프로젝트 이후 자세한 파이프라인 설계는 상기한 데이터 파이프라인 프로젝트에서 진행할 예정입니다.

![etl](/attached/etl.JPG)

## 데이터 소스
데이터 소스는 직접 제작한 [로그 생성기](https://github.com/yangju0411/log_generator) 파이썬 라이브러리를 통해 제작합니다.

```
{ip_address} - - {date} "{method} {path}" {status} {size} "{user_agent}"
...
```
데이터는 위와 같은 형태로 생성됩니다. 한 줄에 요청이 하나입니다.

본 프로젝트는 하루에 한 번 쌓여 있는 하루치 로그를 일괄로 처리하여 DW에 적재하는 상황을 가정하기 때문에 하루치 로그를 생성하여 하나의 파일로 저장합니다.

## 데이터베이스 스키마
![erd](/attached/erd.png)

DB 구조는 팩트 테이블과 디멘션 테이블의 스타 스키마로 구성하였습니다.

Visit 팩트 테이블이 각 디멘션 테이블을 참조하는 형태로 조인 연산을 수행하여 명확하게 로그를 조회할 수 있게 설계했습니다.

현 프로젝트에서는 DW를 일반적인 RDBMS인 PostgreSQL을 사용하였지만 만약 데이터 집계에 최적화된 열 지향 MPP 데이터베이스에 적용한다면 더 대용량의 데이터를 다루는데에도 적합해질 것입니다.

## WORK
### DDL
[DDL](work/ddl.sql)
DDL은 MariaDB용 SQL로 ERD 내보내기 후 수정하였습니다.
### ETL
[ETL](work/etl.ipynb)
정리하기 쉽게 Interactive Python Notebook으로 나타내었습니다.

# REFERENCE
## DW
[타다 (TADA) 서비스의 데이터 웨어하우스 : 태초부터 현재까지](https://speakerdeck.com/vcnc/tada-tada-seobiseuyi-deiteo-weeohauseu-taecobuteo-hyeonjaeggaji?slide=29)

[웹로그 분석을 위한 데이터 웨어하우스 시스템 구축](http://koreascience.kr/article/CFKO201035751420664.page?&lang=ko)

[데이터웨어 하우스의 차원 데이터 모델 – 예제가 포함 된 자습서](https://ko.myservername.com/dimensional-data-model-data-warehouse-tutorial-with-examples)

팩트 테이블 - 빅데이터를 지탱하는 기술 p.80, p.119

[데이터 웨어하우스 모델링 기본 개념 잡기 1편(Fact, Dimension 테이블)](https://datalibrary.tistory.com/43)

[스타 스키마와 눈송이 스키마.](https://snowturtle93.github.io/posts/%EC%8A%A4%ED%83%80-%EC%8A%A4%ED%82%A4%EB%A7%88%EC%99%80-%EB%88%88%EC%86%A1%EC%9D%B4-%EC%8A%A4%ED%82%A4%EB%A7%88/)

[데이터웨어 하우스 모델링의 스키마 유형](https://ko.myservername.com/schema-types-data-warehouse-modeling-star-snowflake-schema)

[AWS Redshift](https://mktg-apac.s3-ap-southeast-1.amazonaws.com/AWS+Summit+Online+Korea/Track5_Session5_Data+Lake+%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C+Amazon+Redshift+Spectrum%EC%9D%84+%EC%9D%B4%EC%9A%A9%ED%95%9C+%EB%8C%80%EB%9F%89+%EB%8D%B0%EC%9D%B4%ED%84%B0+%ED%99%9C%EC%9A%A9+-+%EC%8A%A4%EB%A7%88%ED%8A%B8%ED%8C%A9%ED%86%A0%EB%A6%AC+%EC%9B%A8%EC%96%B4%ED%95%98%EC%9A%B0%EC%8A%A4+%EA%B5%AC%EC%B6%95+%EC%82%AC%EB%A1%80+%EC%86%8C%EA%B0%9C.pdf)

[오픈소스 그린플럼 소개](http://www.itdaily.kr/news/articleView.html?idxno=89798)

[COPY 충돌 방지하는 법](https://int-i.github.io/sql/2022-02-20/postgres-copy-from-conflict-record/)

## ERD
[ERD 그리는 사이트](https://www.erdcloud.com/)

[아파치 웹서버 로그 파일 상세 분석](http://www.linuxlab.co.kr/docs/00-09-6.htm)

[팩트 테이블 채우기](https://dwbi1.wordpress.com/2015/02/09/populating-fact-tables/)

[내 서버에는 누가 들어오는 걸까 - Apache 액세스 로그를 Elastic Stack으로 분석하기](https://d2.naver.com/helloworld/3585246)

## Python
[webserver-log-file-analysis](https://www.kaggle.com/code/eliasdabbas/webserver-log-file-analysis)

[GeoIP](https://rielouo.tistory.com/13)

[User Agent Parser](https://blog.naver.com/wideeyed/222087593906)
