from datetime import datetime
from zoneinfo import ZoneInfo

t = datetime.now(ZoneInfo("Asia/Colombo"))

print(t.strftime("%I:%M:%S %p"))
