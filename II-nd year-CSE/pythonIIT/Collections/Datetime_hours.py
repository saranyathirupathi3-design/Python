from collections import Counter
from datetime import datetime

hours = [datetime.strptime(i,"%Y-%m-%d %H:%M").hour for i in logins]

c = Counter(hours)
print(c.most_common(1))
