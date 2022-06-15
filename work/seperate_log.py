# 로그를 하루 단위로 분리
import re
import pandas as pd

path = "/data/log_data/source_data/access_log_Jul95" # 원본 데이터의 경로

pattern = re.compile('(\S+) - - \[(.*)\] "(.*)" (\S+) (\S+)$')

def parse_access_log(path):
    for line in open(path, 'rb'):
        line = line.decode(encoding='ascii', errors='ignore')
        for m in pattern.finditer(line):
            yield m.groups()
columns = ["host", 'time', 'request', 'status', 'bytes']
df = pd.DataFrame(parse_access_log(path), columns = columns)
df.time = pd.to_datetime(df.time, format='%d/%b/%Y:%X', exact=False)
count_df = df.groupby(df.time.dt.day).count()
counts = list(count_df["host"])

i = 0
for day, cnt in enumerate(counts):
    save_path = "/data/log_data/data/day" + "%02d" %(day + 1) + ".log"
    with open(save_path, "wb") as day_log:
        for _ in range(cnt):
            day_log.write(lines[i])
            i += 1