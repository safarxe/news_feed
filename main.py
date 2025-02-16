import json
import requests
from feedgen.feed import FeedGenerator

# API açarını buraya əlavə et
API_KEY = "351b300755044665b2173891b6d175af"

# Google News API linki
URL = f"https://newsapi.org/v2/top-headlines?language=az&apiKey={API_KEY}"

# API-dən xəbərləri çəkmək
response = requests.get(URL)
data = response.json()

# Xəbər siyahısı
news_list = data.get("articles", [])

# RSS Feed Generator
fg = FeedGenerator()
fg.id("https://news-feed-gules.vercel.app/")
fg.title("Mənim Xəbər RSS Feedim")
fg.link(href="https://news-feed-gules.vercel.app/", rel="self")
fg.description("Bu feed avtomatik olaraq Google News API-dən yaradılıb.")
fg.language("az")

# Xəbərləri RSS-ə əlavə etmək
for news in news_list:
    fe = fg.add_entry()
    fe.id(news["url"])
    fe.title(news["title"])
    fe.link(href=news["url"])
    fe.description(news["description"] if news["description"] else news["title"])
    fe.pubDate(news["publishedAt"])
    
# RSS faylına yazmaq
rss_feed = fg.rss_str(pretty=True).decode('utf-8')  # bytes-dən str-ə çevirmək
with open("news_feed.xml", "w", encoding="utf-8") as f:
    f.write(rss_feed)

print("✅ RSS feed yaradıldı: news_feed.xml")

