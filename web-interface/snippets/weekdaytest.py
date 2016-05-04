from django.http import HttpResponse
import json
import pandas as pd
from pandas import Timestamp
from datetime import datetime

end = "2016-03-01"
period = 30
activities = "Safari"

periodDate = end.replace("-", "")
period = pd.date_range((Timestamp(periodDate) +pd.DateOffset(days=int(period)*-1)), Timestamp(periodDate))

print period

period = period.tolist()
for date in period:
    print date.weekday()
newPeriod = [str(month)[:10] for month in period]

