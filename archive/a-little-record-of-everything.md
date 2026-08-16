# <center>A little Record of Everything</center>
<center>Author G.Yuan 2018/08/23</center>

## Everything
* Example Google Style Python Docstrings(NumPy Style)
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
* Kenneth Reitz, the author of requests and other libraries.
https://www.kennethreitz.org/
* GitHub Marketplace
https://github.com/marketplace
* A little book 《Personal Smart Assistant for Digital Media and Advertisement》AI Related, Voice Interactive
https://pdfs.semanticscholar.org/bb1b/0763356dfeb975138cd33d2d0af288bddfb9.pdf
* A good explain about Python Object & Type & Metaclass
Python 的 type 和 object 之间是怎么一种关系？ - jeff kit的回答 - 知乎 https://www.zhihu.com/question/38791962/answer/78172929
* Gunicorn Design Note Docs
http://docs.gunicorn.org/en/stable/design.html
* [What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)
The Answer is a real good example of how to write a doc.
* Python open file mode
https://stackoverflow.com/questions/1466000/python-open-built-in-function-difference-between-modes-a-a-w-w-and-r
* Should always keep to output file or data in UTF-8 encoding of our System.
* Click the link from vscode  may cause a encoded url change to a unencoded url. This has token me a big effort to debug the s3 presigned url retrivel issue. Here is the example
	```
	# If you click the link in vscode directly
	# and vscode redirect you to your browser.
	# The link will change to second one.
	# The %x has been decoded in the process.
	# But that's not we want.
	https://s3.amazonaws.com/xxx/bulk_data_poc/Metrics/est_download__sum.US.Overall.ios-phone.weekly.2018-08-04.data.csv

	https://s3.amazonaws.com/xxx/bulk_data_poc/Metrics/est_download__sum.US.Overall.ios-phone.weekly.2018-08-04.data.csv
	```
	**For url encode and decode, we should always keep the output of our system is a valid url(encode the url before we use it). Never paste a encoded url into the address bar of a browwer. The browser will try to encode the url to its own standard!!**
	>Reference: http://www.ruanyifeng.com/blog/2010/02/url_encoding.html

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMzg2NjAwODQsLTEwMDk0NDI5ODgsLT
ExMTg2NDkxMTIsLTc0MTg1NzgxMywtMTk4NDkyMywxNTg3NTM2
MzA2LC0xNzU3ODU0MTg4LDIxMTE4MjQ1MzgsLTE0NjY3NzE2OD
BdfQ==
-->
