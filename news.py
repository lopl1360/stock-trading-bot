from newsapi import NewsApiClient
import credentials as cred
import pprint
import stock_data_gatherer as sdg
import re
import util
import datetime
import constants as const


class NewsGetter:
    def __init__(self):
        print(cred.NEWS_API_KEY)
        self.api = NewsApiClient(api_key=cred.NEWS_API_KEY)

    def get_news(self, stock):
        search_terms=stock + " " + re.sub(r'[^\w\s]','',sdg.get_stock_company_name(stock))
        from_date = datetime.date.today() - datetime.timedelta(days=const.NEWS_DAYS_AGO)
        articles = self.api.get_everything(from_param=str(from_date), q=stock, qintitle=stock + " OR " + re.sub(r'[^\w\s]','',sdg.get_stock_company_name(stock)), language='en', page_size=100)['articles']
        # qintitle=stock + " OR " + re.sub(r'[^\w\s]','',sdg.get_stock_company_name(stock))
        news_descriptions = []
        print("Checking NEWS for ", stock)
        for news in articles:
            if util.check_overlap(search_terms, news['description']):
                news_descriptions.append(news['description'])
        return news_descriptions
