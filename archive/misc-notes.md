# A little Record of Everything
Author G.Yuan 2018/08/23

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

## Software Engineering
* How about build a library name minunit? or what's the best pratice to write unit test in large project?
	 > Why: Large project always comes with a large amount of unit test cases and complex functional test cases. It's hard to maintain the consistence with codebase. A little change in code may cause a lot of changes in unit test cases. We need a way to min the code of unit, but how?

    ![image](https://user-images.githubusercontent.com/20035835/157248738-43730153-10bc-4551-b357-fd300ea2bfd1.png)

* Before you deploy your branch into feature env, please wait the CI passed.
	 > Why: Deploy just pull image from docker hub, but the image will only update after your branch passed CI.
* You could find the details about the new image builded by CI with your branch, including the libraries version you changed in requirement.txt
* Comment only when it must. Code speaks themselves.

## What can be learned from NewRelic Gevent Tracing Issue?
> **Backgroud**
> 2018/08/21 We use NewRelic Python Agent v2.62.0.47 to trace Mircroserive-remote-call time cost with FunctionTrace context manager in gevent spawn coroutines. But the agent lose the transaction in gevent and when we keep the current transaction and application object in flask request to provide a access in gevent. The agent actually throws exceptions and WE NEVER TRY TO CATCH IT, **then online crashed**:

* If some problems happend with a 3rd party library or framework, try to find info and solutions on their official channel.
* IMPORT: If a new version or update availiable, try it first.
* If official cannot solve the problems, try others.
* Before we make sure ourself solution is OK. Add most general expection try-catch with the untest code to protect the production env from unexpected crash.

## Python Problems
* pycrypto & pycryptodome will conflict. Both of them will use installed the `Crypto` package directory.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjMxMzUyNzMzLDExNTg0NzE0NjgsMTg1Nj
Q4ODA2MywtNDE1OTUxNDU1XX0=
-->


