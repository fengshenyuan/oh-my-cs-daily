# Python HTTP2 Ecosystem
*  The Reason we need to care about the Python HTTP2 Ecosystem can be referred to `The War between HTTP RESTful & RPC`. 
*  We try to find a solution so that we never need to consider grpc/dubbo/thrift/brpc/... as options in future.

## Basic Resource
- [http2-spec](https://github.com/http2/http2-spec)
- [awesome-http2](https://github.com/vigneshshanmugam/awesome-http2)
- [awesome-http-benchmark](https://github.com/denji/awesome-http-benchmark)
- [Web Framework Benchmarks](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7)
- [Introduction to HTTP/2 - From Google](https://developers.google.com/web/fundamentals/performance/http2)

## Python Impl
- [httplib2](https://github.com/httplib2/httplib2)
- [hyper](https://github.com/python-hyper/hyper): Has well-architectured components, such as hyper-h2, hyperlink, hyperframe, hpack..

## Other Languages Impl
- [h2o](https://github.com/h2o/h2o): Write in C, we can bind it to Python.
- [nghttp2](https://github.com/nghttp2/nghttp2): Write in C, providing a Python Bind
- [gPRC-python,gPRC-go](https://github.com/grpc/grpc): Since gPRC supports Python, it means gPRC must have an impl for Python with HTTP2.

## Python Framework Supporting
- [Tornado](https://github.com/tornadoweb/tornado)
- [Flask](https://github.com/pallets/flask)
- [Sanic](https://github.com/huge-success/sanic)
- [Hug/Falcon](https://github.com/hugapi/hug)
- [quart](https://github.com/pgjones/quart): Supported
- [hypercorn](https://github.com/pgjones/hypercorn)
- [httpx](https://github.com/encode/httpx): A next generation HTTP client for Python
- [starlette](https://github.com/encode/starlette)
- [uvicorn](https://github.com/encode/uvicorn)
- [aiohttp](https://github.com/aio-libs/aiohttp): Not Yet
- [requets](https://requests.readthedocs.io/en/master/)
- [fastapi](https://github.com/tiangolo/fastapi)

## People & Orgs Worth to Follow
- [encode](https://github.com/encode): who writes httpx, starlette, uvicorn..
- [Hyper](https://github.com/python-hyper)
- [pgjones](https://gitlab.com/pgjones)
- [aio-libs](https://github.com/aio-libs)
- [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio)
- [magicstack](https://github.com/MagicStack)

## How to build MS-Arch with the Python HTTP2 Ecosystem

### Server side
- xxx

### Client side
- xxx

### Load Balancer
*  Nginx??
