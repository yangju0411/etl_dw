from log_generator import generate_log
from datetime import timedelta
from dateutil.parser import parse
import concurrent.futures

td = timedelta(seconds = 4)
pool = concurrent.futures.ThreadPoolExecutor()

def doubled(i, s):
    return i, generate_log(s)

now = parse("1997-04-11 00:00:00")
threads = []
logs = []
i = 0
while now < parse("1997-04-11 00:01:00"):
    threads.append(pool.submit(doubled, i, now.strftime("%Y-%m-%d %H:%M:%S")))
    now += td
    i += 1
    
for p in concurrent.futures.as_completed(threads):
    logs.append(p.result())

logs.sort()

with open("data/access_970411.log", "w") as log_file:
    for i, log in logs:
        log_file.write(log)
        log_file.write("\n")