
# <center>A little Summary about Daily Work</center>
<center>Author G.Yuan 2018/07/05</center>

## Software Engineering
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
