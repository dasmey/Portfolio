library(shiny)
library(dplyr)
library(plotly)

shinyServer(function(input, output) {
        
        output$df <- renderDataTable({
                
                mincities <- input$cities[1]
                maxcities <- input$cities[2]
                
                villes <- read.csv("villes_france.csv")
                villes <- villes[, c("Ozan", "X618", "X4.91667", "X46.3833")]
                colnames(villes) <- c("Ville", "Population", "lng", "lat")
                villes2 <- filter(villes, Population >= mincities, Population <= maxcities)
                villes2 <- arrange(villes2, desc(Population))
                villes3 <- villes2[!villes2$lng < -10, ]
                villes4 <- villes3[!villes3$lat < 30, ]
                villes4
        }, options = list(lengthMenu = c(5, 10, 25), pageLength = 10)) 
        
        output$hist1 <- renderPlot({
                mincities <- input$cities[1]
                maxcities <- input$cities[2]
                villes2 <- filter(villes, Population >= mincities, Population <= maxcities)
                villes2 <- arrange(villes2, desc(Population))
                villes3 <- villes2[!villes2$lng < -10, ]
                villes4 <- villes3[!villes3$lat < 30, ]
                villes4
                x <- villes4[, 2]
                breaks <- seq(min(x), max(x), length.out = input$breaks + 1)
                hist1 <- hist(villes4$Population,
                              breaks = breaks,
                              col = 'darkgray',
                              main = "French population histogram",
                              xlab = "Population",
                              border = 'white')
        })
})
