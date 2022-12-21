#install.packages("httr")
#install.packages("rvest")
#install.packages("dplyr")
library(httr)
library(rvest)
library(dplyr)
# Need to figure out how to loop this for each companies ID number. this example is Twitter "2198"
URL = "https://www.1stock1.com/1stock1_2198.htm"
link = read_html(URL)
# node = How do I find the ".F1251" identifier for each companies HTML page?
Comp_Name = link %>% html_nodes(".F1251") %>% html_text()
Year = link %>% html_nodes("tr+ tr b") %>% html_text()
Gain_Loss = link %>% html_nodes("tr+ tr td:nth-child(5) > div > span , .F1251 div div > div span, td:nth-child(5) > div > div > span") %>% html_text(trim = T)
Data = data.frame(Comp_Name, Year, Gain_Loss)
write.csv(Data, "Data.CSV")
