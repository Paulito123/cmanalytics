from pytrends.request import TrendReq
import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360)

# build payload
kw_list = ["Parsiq"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m')

#1 Interest over Time
data = pytrends.interest_over_time()
data = data.reset_index()

# print(f"{data}")

# fig = px.line(data, x="date", y=kw_list, title='Keyword Web Search Interest Over Time')
# fig.show()

# relq = pytrends.related_queries()
# print(f"{relq}")

reltop = pytrends.related_topics()
print(f"{reltop}")

# categories = pytrends.categories()
# print(f"{categories}")
