import scrapy


class TwitterSpider(scrapy.Spider):
    name = 'twitter_results'
    start_urls = ['http://twitter.com/inraidi']

    def parse(self, response):
        for href in response.css('.tweet .time a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'date': response.css('.tweet ._timestamp.js-short-timestamp::text').extract()[0],
           'tweet': response.css('.tweet p').extract()[0],
            'link': response.url,
        }
# scrapy runspider twitter_scraping.py -o twitter_results.json
