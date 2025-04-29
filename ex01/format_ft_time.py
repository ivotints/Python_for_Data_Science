import time
import datetime

cur_time = time.time()

print(f"Seconds since January 1, 1970: {cur_time:,.4f}", end="")
print(f" or {cur_time:.2e} in scientific notation")
print(datetime.datetime.fromtimestamp(cur_time).strftime("%b %d %Y"))
