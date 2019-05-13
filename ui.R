# 用户界面 端http://shiny.rstudio.com/articles/css.html
library(shiny)
library(shinydashboard)
library(shinyBS)
library(htmltools)
# library(shinyjs)
# library(markdown)

dashboardPage(
  dashboardHeader(title = "个性化课程推荐系统"
                  ),# dashboardHeader
  # 侧边栏
  dashboardSidebar(
  # 加载各种脚本文件
    includeCSS("www/styles.css"),
    includeScript("www/d3.v3.min.js"),
    includeScript("www/d3-tip.js"),
    includeScript("www/echarts-all.js"),
    includeScript("www/echarts.js"),
    
    sidebarUserPanel("暮色",
                     subtitle = a(href="#",icon("circle",class="text-success"),"online"),
                     image = "dist/img/user7-128x128.jpg"), #表示头像的图像
    sidebarSearchForm(textId="searchText", buttonId="searchButton", icon = icon("search")),
    sidebarMenu(id="tabs",
	  # 表示菜单的图像（icon）
      menuItem("首页", icon = icon("calendar"), tabName = "widgets"),
      menuItem("搜索", icon = icon("search"), tabName = "searchresult"),
      menuItem("分类", icon = icon("th"), tabName = "category",
               menuSubItem("办公",tabName="office",icon = icon("briefcase")),
               menuSubItem("考试",tabName="exam",icon = icon("graduation-cap")),
               menuSubItem("外语",tabName="language",icon = icon("language")),
               menuSubItem("建造",tabName="construction",icon = icon("building")),
               menuSubItem("金融",tabName="financial",icon = icon("bank")),
               menuSubItem("求职",tabName="job",icon = icon("wrench")),
               menuSubItem("管理",tabName="management",icon = icon("wrench")),
               menuSubItem("医疗",tabName="medical",icon = icon("briefcase")),
               menuSubItem("计算机",tabName="computer",icon = icon('laptop')),
               menuSubItem("社会科学",tabName="socialscience",icon = icon("share-square")),
               menuSubItem("生活教育",tabName="life",icon = icon("life-ring")),
               menuSubItem("软件教程",tabName="software",icon = icon("graduation-cap")),
               menuSubItem("文化艺术",tabName="culture",icon = icon("music"))
               ),
      menuItem("login", tabName = "login",
               icon = icon("user-circle")),
      menuItem("Hotspot Analysis", icon = icon("fire"), tabName = "hot"),
	  menuItem("MOOC Data Analysis",icon = icon("table"),tabName = "analysis"),
      menuItem("About", tabName = "about",
               icon = icon("info-circle", lib="font-awesome"))
    )
    ),# dashboardSidebar
	# 身体
   dashboardBody(
     tabItems(
       tabItem(tabName="widgets",
               uiOutput("titles")
       ),
       tabItem(tabName = "about",
               box(width = 12,
                   includeHTML("www/about.html")
               )
               ),
       tabItem(tabName = "login",
               # HTML("<div class='login-logo'>
               #        你的<b>专属推荐课程</b></a>
               #      </div>"),
               htmlOutput("page")
               ),
       tabItem(tabName = "office",
               uiOutput("office")),
       tabItem(tabName = "exam",
         uiOutput("exam")
       ),
       tabItem(tabName = "language",
               uiOutput("language")
       ),
       tabItem(tabName = "construction",
               uiOutput("construction")
       ),
       tabItem(tabName = "financial",
               uiOutput("financial")
       ),
       tabItem(tabName = "job",
               uiOutput("job")
       ),
       tabItem(tabName = "management",
               uiOutput("management")
       ),
       tabItem(tabName = "medical",
               uiOutput("medical")
       ),
       tabItem(tabName = "computer",
               uiOutput("computer")
       ),
       tabItem(tabName = "socialscience",
               uiOutput("socialscience")
       ),
       tabItem(tabName = "life",
               uiOutput("life")
       ),
       tabItem(tabName = "software",
               uiOutput("software")
       ),
       tabItem(tabName = "culture",
               uiOutput("culture")
       ),
       tabItem(tabName = "hot",
               h2("搜索热词"),
               wordcloud2Output("wordcloud2"),
               h2("地理热图"),
               div(img(src="hotmap.png",class='hot')),
			   h2("课程名热度词云"),
			   div(img(src="pythonDataAnalysis/1.png",class="hot")),
			   h2("大学开课数"),
			   div(img(src="pythonDataAnalysis/2.jpg",class="hot")),
			   h2("课程被选人数"),
			   div(img(src="pythonDataAnalysis/3.jpg",class="hot")),
			   h2("课程分类比例"),
			   div(img(src="pythonDataAnalysis/4.jpg",class="hot"))
       ),
	   #tabItem(tabName = "analysis",
			   #h2("课程名热度词云"),
			   #div(img(src="pythonDataAnalysis/1.png",class="image1"))
			   #h2("大学开课数"),
			   #div(img(src="pythonDataAnalysis/2.jpg",class="image2")),
			   #h2("课程被选人数"),
			   #div(img(src="pythonDataAnalysis/3.jpg",class="image3")),
			   #h2("课程分类比例"),
			   #div(img(src="pythonDataAnalysis/4.jpg",class="image4"))
	   #),
       tabItem(tabName = "searchresult",uiOutput("searchresult"))
       )# tabItems
     )
   )
# 如果图片在本地，则需要放在www的文件夹 且图片名不能是中文