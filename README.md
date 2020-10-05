- Tạo project: Mở CMD nhập: scrapy startproject <i>ProjectName</i>
- Vào file items.py nhập vào các trường mình sẽ crawl
- Tạo nhện: scrapy genspider <i>spidername</i> <i>tên miền sẽ crawl</i>
- Vào nhện, sửa list start_urls, sửa hàm parse để nó lấy dữ liệu
- Chạy project:
	+ Crawl: scrapy crawl <i>spidername</i> 
	+ Crawl giới hạn số item: scrapy crawl <i>spidername</i> -s CLOSESPIDER_ITEMCOUNT=<i>x</i> 
		(x  là số item giới hạn)
	+ Crawl test trên 1 trang web: scrapy parse --spider=<i>spidername</i> <i>url</i>