#This is the first tutorial using Python 

#importing scrapy
import scrapy

#scrapy.Spider is the sub class of Spider
class QuotesSpider(scrapy.Spider):
    name = "quotes" #identity of the spider
    
    #start_requests is the function which provides iterable requests to the spider on which links to crawl
    def start_requests(self):
        urls=['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
     
    #parse() handles all theresponses downloaded from the ulr links       
    def parse(self,response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' %page
        with open(filename,'wb') as f:
            f.write(response.body) #response parameter is an instance of the 'Textresponse' which holds the contents of the page
        self.log('Saved file as %s' % filename)
    
    #parse() parses the response, extracting the scraped data as dicts and also finding new urls to follow and creating new requests from them.
    
#to run the crawler use the following command:
# scrapy crawl quotes