# RecommendationSystem
该推荐系统主要是基于web日志挖掘的个性化学习推荐平台。主要使用R语言，配合css，搭建的一个shiny应用程序。课程图片以及课程链接均从百度传课爬取获得的。主要实现的功能如下：
## 热点课程推荐
通过对日志中课程访问的次数，将访问次数较多的课程在首页进行推荐。
## 课程搜索
搜索功能主要是通过正则表达式进行模糊搜索。
## 课程分类
通过人工的方法对课程进行添加标签。但在实际工作生活中，当客户上传视频时会自主添加标签。
## 个性化推荐
个性化推荐算法主要是应用spark ALS算计进行推荐。
## 热点分析
热点分析包括两点：热词分析和地理热图分析。

## -------------------------------使用方法-------------------------------
## -----------查询已安装的R包-----------
search()

## -----------安装各种包-----------
install.packages("各种R包")，例如install.packages("shiny")

（linux比windows安装R包复杂，win几乎是一键完成）


## ------------装载安装好的包(保证任意一个都不能有问题)----------
library("shiny")

library("shinydashboard")

library("shinyBS")

library("shinyjs")

library("htmltools")

library("markdown")

library("dplyr")

library("stringr")

library("RMySQL")

library(jiebaR)

library(wordcloud2)

library("REmap")

REmap还需要依赖：install.packages("devtools")    library("devtools")    install_github('lchiffon/REmap')

## ------------路径-----------
查看当前路径：getwd()

设置路径：setwd("C:\\Users\\guoen\\Desktop\\Rworkspace")

setwd到你克隆下来的项目的父目录，例如我的Rworkspace下面就是我clone下来的项目了。

## -------------运行程序--------------
library("shiny")

runApp("RecommendationSystem-master")

## -------------登录login--------------需要先在MySQL数据库中创建elearn数据库，users表(userid,password)
用户id：104126

密码：12345

数据库中能查到这条记录，在APP中就可以用这个用户名密码登录了。

问我这个id和pd哪来的？在Rworkspace\RecommendationSystem-master\data\recommend.csv这个文件下，第二个字段对应id，密码自己随意写。


## -------------------------调试过程中可能遇到的问题------------------------
问题：不断开启APP，连续开启了16个数据库连接，超过数据库最大连接数

Error in .local(drv, ...) : 

  Cannot allocate a new connection: 16 connections already opened
  
解决：断开所有MySQL数据库连接

lapply(dbListConnections(MySQL()), dbDisconnect)
