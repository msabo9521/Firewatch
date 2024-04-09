
import datetime

ticks = 1151946221*.01

converted = datetime.timedelta(microseconds=ticks)
print(converted)

days, remainder = divmod(ticks, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"{int(days)} days {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds")