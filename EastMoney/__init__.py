import bs4, json
from bs4 import BeautifulSoup as soup
import urllib.request

class EastMoney():

        def __init__(self, ticker, market):
                self.ticker = ticker
                self.market = market
                self.getURL()

        def getURL(self):
                self.user_agent='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
                self.headers={'User-Agent':self.user_agent}
                if self.market == 'SZ':
                        self.url="http://f10.eastmoney.com/CompanySurvey/CompanySurveyAjax?code=sz"+self.ticker
                elif self.market == 'SH':
                        self.url="http://f10.eastmoney.com/CompanySurvey/CompanySurveyAjax?code=sh"+self.ticker
                try:
                        self.req=urllib.request.Request(self.url, headers=self.headers)
                        self.response=urllib.request.urlopen(self.req)
                        self.page=self.response.read().decode("utf-8")
                        self.content=json.loads(self.page)
                except Exception:
                        pass
                if self.market == 'SZ':
                        self.url="http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id="+self.ticker+"2"
                elif self.market == 'SH':
                        self.url="http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id="+self.ticker+"1"
                try:
                        self.req=urllib.request.Request(self.url, headers=self.headers)
                        self.response=urllib.request.urlopen(self.req)
                        self.page=self.response.read().decode("utf-8")
                        self.content1=json.loads(self.page[31:-2])
                except Exception:
                        pass

        def getInfo(self):
                try:
                        return {'code':self.content1[1],'price':self.content1[25],'PE':self.content1[38],'marketCap':self.content1[46],'company':self.content1[2],'company_name_en':self.content['jbzl']['ywmc'],'company_name_cn':self.content['jbzl']['gsmc'],'industry':self.content['jbzl']['sshy'],'area':self.content['jbzl']['qy'],'desc':self.content['jbzl']['gsjj']}
                except Exception:
                        return {'code':'N/A','price':'N/A','PE':'N/A','marketCap':'N/A','company':'N/A','company_name_en':'N/A','company_name_cn':'N/A','industry':'N/A','area':'N/A','desc':'N/A'}

        def getPrice(self):
                try:
                        return self.content1[25]
                except Exception:
                        return 'N/A'

        def getName(self):
                try:
                        return self.content1[2]
                except Exception:
                        return 'N/A'
        
        def getCode(self):
                try:
                        return self.content1[1]
                except Exception:
                        return 'N/A'

        def getPE(self):
                try:
                        return self.content1[38]
                except Exception:
                        return 'N/A'

        def getMarketCap(self):
                try:
                        return self.content1[46]
                except Exception:
                        return 'N/A'

        def getCompanyName(self,lang='CN'):
                try:
                        if lang == 'CN':
                                return self.content['jbzl']['gsmc']
                        elif lang == 'EN':
                                return self.content['jbzl']['ywmc']
                        else:
                                return 'N/A'
                except Exception:
                        return 'N/A'

        def getIndustry(self):
                try:
                        return self.content['jbzl']['sshy']
                except Exception:
                        return 'N/A'

        def getLoc(self):
                try:
                        return self.content['jbzl']['qy']
                except Exception:
                        return 'N/A'

        def getDesc(self):
                try:
                        return self.content['jbzl']['gsjj']
                except Exception:
                        return 'N/A'

