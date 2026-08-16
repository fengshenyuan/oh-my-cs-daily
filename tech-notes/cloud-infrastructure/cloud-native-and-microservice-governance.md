# Cloud Native & Microservice Governance

## K8S

- How to build the internal networking of Cluster?（如何搭建集群内网?）
- K8S落地实战？
- K8S如何解决服务注册与发现问题？
- K8S的object是到底是如何工作的？
- CoreDNS、Envoy、Linkerd是怎样与K8S配合工作的？
- 局域网与DNS到底是怎么回事儿？
- PaaS平台到底是个什么东西？与K8S的区别是什么？K8S怎么与PaaS平台结合协作起来？
- K8S对研发工作人员的影响是什么？
- 容器docker，容器运行时标准?
- K8S如何做日志收集与处理？fluentd？
- K8S包管理器与发行版？

## K8S是什么

- [Kubernetes 效应](https://www.infoq.cn/article/kubernetes-effect) 本片文章中谈到将k8s视为一组分布式应用的抽象原语，从语言视角提供了切入点，重点涉及到了基于k8s的cloud native程序设计原则和设计模式.
- [一文让你了解Kubernetes架构](https://juejin.im/post/5d86db1be51d4557ca7fde07) 本文将k8s的核心架构使用几张令人影响深刻的图片表现出来，明确了在cloud native体系中k8s的编排作用.
- [我花了10个小时，写出了这篇K8S架构解析！](https://cloud.tencent.com/developer/article/1543623) 本文包含了一个tomcat + mysql的服务构建实例, 说明了如何在k8s部署内部应用和服务以及将内部服务暴露给外网用户.
- [谈 Kubernetes 的架构设计与实现原理](https://draveness.me/understanding-kubernetes) 对以上文章进行了一些细节上的补充，使得k8s在云原生的生态中所起的作用、职责更为清楚.
- [一篇文章带你了解kubernetes各组件间的通信机制](https://zhuanlan.zhihu.com/p/82314737) 使用了比较多的动图来进行解释说明


## HTTP RESTful vs gRPC
Why people choose gRPC? Mostly, they want performance!

Why people choose HTTP RESTful solutions? Mostly, they want decoupled Architecture!

### Major Difference
* service register and discovery

### Thinking 
* What if someway HTTP RESTful's performance is capable of gRPC? Do we still need gPRC solution?

### How to combine the benefits of these two solutions together?
Since gPRC actually is based on HTTP2, which means HTTP RESTful could have a capable performance with gPRC in theory. 
* The real point is to improve performance and reduce the complexity of HTTP's future version, such as HTTP3. And
* Provide real HTTP2/HTTP3/.. supported and high-performance binding client/server implementations in every language. (Actually, this is what gPRC has been done by providing the auto-generated client-side and server-side stub codes!)


### 微服务
- [微服务架构的应用集成：服务网格并不是 ESB](https://www.infoq.cn/article/9xVioj0JCM-0BwVkIXDL)

### API Gateway & Service Proxy & Service Mesh
Proxy is usually what we called the data plane. To leverage the service mesh, we still need a control plane.
Envoy is a CNFG-Graduate service proxy - a graduate data plane.
- [What is Service Mesh?](https://kuma.io/docs/1.1.2/overview/what-is-a-service-mesh/)
- [Service Mesh Comparison](https://servicemesh.es/)
- [Service Mesh Ultimate Guide: Managing Service-to-Service Communications in the Era of Microservices](https://www.infoq.com/articles/service-mesh-ultimate-guide/)
- [服务网格比较： Istio 与 Linkerd](https://cloudnative.to/blog/service-mesh-comparison-istio-vs-linkerd/)
- [Meshery:A multi-mesh manager](https://layer5.io/service-mesh-management/meshery/operating-service-meshes)

### API Gateway
- [Nginx](https://www.nginx.com/)
- [OpenResty: Scalable Web Platform by Extending NGINX with Lua](https://openresty.org/en/)
- [Kong: The world’s most popular API gateway](https://docs.konghq.com/enterprise/)
![image](https://user-images.githubusercontent.com/20035835/157273682-49ef48ef-b279-4ae8-ae97-a68033e77655.png)
- [Træfik: A modern HTTP reverse proxy and load balancer made to deploy microservices with ease](https://doc.traefik.io/traefik/v1.4/)
