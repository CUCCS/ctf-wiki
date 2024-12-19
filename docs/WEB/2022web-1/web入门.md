---
marp: true
---

# WEB 入门

2022.10.19

主讲人：许泽林

---

- **如何去理解Web安全**？
- **哪里会存在Web安全问题**？

<!-- 开始前需要了解整个体系结构和涉及到的相关概念，理清概念可以更好地帮助我们理解web安全。 -->
---

## What is Web?

- 诞生初期：Web静态页面，只是用于向用户单向展示一些信息

- 信息展示的一种新方法（HTML）

  - 目前：综合Web应用程序，实现用户与服务器之间双向的信息交换

- 信息交换的工具

<!-- web广义上来讲就是万维网，往小了讲就是网页或者是因特网上某种类型计算机的程序。但是，要实现信息交换，就要遵循某种协议。 -->

---

## 交换的协议？

- TCP/IP
- HTTP（Hypertext Transfer Protocol）
- HTTPS（Hypertext Transfer Protocol Secure）


<!-- 目前计算机网络广泛使用的模型就是TCP/IP模型

HTTP协议处于TCP/IP协议体系的应用层

HTTPS比HTTP多了个SSL层，运用一些加密方法(RSA)，可以让信息传输更加安全 -->

---

## WEB解题过程：
- 总览全局：大体掌握题目有哪些、哪些可用的功能（怎么写出来的）、以及可能存在的漏洞的功能点
- 步步为营：测试各个功能点，简称fuzz环节。对于有代码的题目，则进行初步的代码审计
- 深入探索：对于可能存在漏洞的地方，深入研究，依据网上已存在的资料进行辅佐，编写poc
- 柳暗花明：对于一般ctf题目，flag都有明确的位置说明，通过正确解题思路一定可以获取到。最通常的flag放置的位置在根目录下，以文件形式存储。

---

## 工具

工欲善其事，必先利其器
  - Burp Suite
    - [下载地址](https://portswigger.net/burp/releases/professional-community-2022-8-5?requestededition=community&requestedplatform=)
    - [使用视频教程](https://www.bilibili.com/video/BV1CL41147vX?p=79) 
  - SwitchyOmega
    - [下载地址](https://github.com/FelisCatus/SwitchyOmega/releases)
  - HackBar

---

## 常见的两种 HTTP 请求方法

- GET
- POST

<!-- 请求方法是web中最核心也是最基础的，一定要理解透彻。 -->

---

## Request header（请求头）

请求头是 `HTTP` 头的一种，它可在 `HTTP` 请求中使用，并且和请求主体无关。

```
GET /home.html HTTP/1.1
Host: developer.mozilla.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://developer.mozilla.org/testpage.html
Connection: keep-alive
Upgrade-Insecure-Requests: 1

```

参考资料：
- [Request header](https://developer.mozilla.org/zh-CN/docs/Glossary/Request_header)
- [Headers](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers)


---

## GET方法

```
/get.php?name1=value1&name2=value2
```

这是一个简单的get请求，可以通过get方法为这个get.php传递所需要的参数。
- `?` 后跟变量参数
- `&` 拼接其余参数

---

## POST方法

```
POST /test/post.php HTTP/1.1
Host: test.com
Content-Type: application/x-www-form-urlencoded

name1=value1&name2=value2

```

与get方法不同的是，post传递的数据在 url 中看不见，一般修改post请求需要抓包改包，或者是构造html表单提交。

**参考资料**
- [POST](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Methods/POST)


---

## 练习

- [攻防世界 weak_auth](https://adworld.xctf.org.cn/challenges/details?hash=f6b4cf7b-678c-4ebd-93ef-ba82b02de2ac_2&task_category_id=3)

- [攻防世界 baby_web](https://adworld.xctf.org.cn/challenges/details?hash=b2d9f749-b29c-4877-950d-117258cb09a4_2&task_category_id=3)

- [攻防世界 get_post](https://adworld.xctf.org.cn/challenges/details?hash=a1711cae-905d-4174-b274-cbc2a922e326_2&task_category_id=3)

- [攻防世界 cookie](https://adworld.xctf.org.cn/challenges/details?hash=24488dcc-cb19-4498-b548-d5a179273eb8_2&task_category_id=3)


---

## 服务

- 服务是由应用提供的
- 举个 🌰 ：LNMP

有了请求方法，总不能每次我们都用手来提交，这时候由应用提供的服务帮我们提交请求，进行数据交换。

<!-- 自己动手搭建过网站的同学肯定很熟悉，是一种常见的架构，如果没搭建过的话，也没关系，上面四个字母代表的具体意思就是下面这些应用的简称。 -->

---

## 应用集合

- Linux、Windows Server
- Nginx HTTP and reverse proxy server、Apache HTTP Server Project、Tomcat …
- MySQL、MSSQL、PostgreSQL、MongoDB …
- PHP、JAVA、Node.js、ASP、ASPX …

<!-- 操作系统的安全漏洞，比如Windows平台永恒之蓝SMB协议漏洞、Linux下各种权限提升，远程溢出。

​Web服务中间件安全漏洞，比如Nginx、apache文件解析漏洞，Tomcat弱口令远程命令执行。

​一些情况下可以通过MySQL或者其他一些数据库应用进行提权。

​代码层面漏洞，比如PHP某些组件溢出的漏洞RCE，又或者是写代码的时候过滤不严。 -->

---

## 信息搜集

- robots.txt
  > robots.txt是一种存放于网站根目录下的文本文件，用于告诉网络搜索引擎的漫游器此网站中的哪些内容是不应被搜索引擎的漫游器获取的。
- .idea 文件夹
  > IDEA 都会在项目根目录有一个.idea文件夹，其中会泄露源码文件名等信息。
- .git 文件夹
  > .git 文件夹包含让 git 能够正常工作所需的所有信息。 


---

- __MACOSX & .DS_store
  
  > 存储当前文件夹在桌面显示相关方面的一些自定义属性，包括文件图标的位置、文件夹上次打开时窗口的大小、展现形式和位置等。

- gedit备份文件

  >格式为 filename~ ，比如index.php~

- vim备份文件

  > 格式为.filename.swp或者*.swo或者*.swn，比如.index.php.swp

除此之外，常见的备份文件后缀名还有：“.svn”、“.bak”、“.bash_history”、“.bkf”

---
## 工具

- [dirsearch](https://github.com/maurosoria/dirsearch)
- [ds_store_exp](https://github.com/lijiejie/ds_store_exp)
- [GitHack](https://github.com/lijiejie/GitHack)

---

## 练习

- [攻防世界 robots](https://adworld.xctf.org.cn/challenges/details?hash=d7b42b9a-50ff-49d2-89b7-a0e7f960f63a_2&task_category_id=3)
- buuoj 粗心的小李
- buuoj 常见的搜集

---

![](./img/1.png)
