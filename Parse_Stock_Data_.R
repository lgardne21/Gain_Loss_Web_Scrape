library(httr)
library(rvest)
library(dplyr)
library(XML)

columns = c("Year", "Gain_Loss")
df0 = data.frame(matrix(nrow =0, ncol = length(columns)))
colnames(df0) = columns

main_url = "https://www.1stock1.com/1stock1_112.htm"
resource = GET(main_url)
parse = htmlParse(resource)
links = xpathSApply(parse, path = "//a", xmlGetAttr, "href")
for (i in 1:length(links)) {
  w = paste("https://www.1stock1.com/",links[12], sep = "")
  x = read_html(w)
  y = GET(w)
  z = htmlParse(y)
  links2 = xpathSApply(z, path = "//a", xmlGetAttr, "href")
  for (i in 1:length(links2)) {
    read = read_html("https://www.1stock1.com/", links2[i])
      # node = How do I find the ".F1251" identifier for each companies HTML page?
    #Comp_Name = read %>% html_nodes(".F1251") %>% html_text()
    Year = read %>% html_nodes("tr+ tr b") %>% html_text()
    if (identical(Year, character(0))) {
      Year = 0
    } else {
      Year = read %>% html_nodes("tr+ tr b") %>% html_text()
    }
    Gain_Loss = read %>% html_nodes("td:nth-child(5) span span") %>% html_text(trim = T)
    if (identical(Gain_Loss, character(0))) {
      Gain_Loss = 0
    } else {
      Gain_Loss = read %>% html_nodes("td:nth-child(5) span span") %>% html_text(trim = T)
    }
    dfa = paste("df",i, sep = "")
    dfb = paste("df",i+1, sep = "")
    dfc = paste("df", i-1, sep = "")
    
    dfa = data.frame(Year, Gain_Loss)
    dfb = rbind(dfc, dfa)
    write.csv(dfb, "Data.CSV")
  }
}
