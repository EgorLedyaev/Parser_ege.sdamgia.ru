import scrapy

print("Результат программы будет в файле 'dump.json'")

first_id = int(input("Введите начальный id теста"))
last_id = int(input("Введите конечный id теста"))
name_teacher = input("Введите Имя и Фамилию преподавателя")

class CatalogSpider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ['inf-ege.sdamgia.ru']
    start_urls = ['https://inf-ege.sdamgia.ru/']
    pages_count = last_id


    def start_requests(self):
        for page in range(first_id, 1 + self.pages_count):
            url = f'https://inf-ege.sdamgia.ru/test?id={page}'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        item = {
            'url': response.request.url,
            'title': response.css('div.new_header b').extract_first('').strip().replace('</b>','').replace('<b>','').replace('<!--np-->',''),
        }

        if str(item)[((len(name_teacher)*-1)-2):-2] == str(name_teacher):
            yield item