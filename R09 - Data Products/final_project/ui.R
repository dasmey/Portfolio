library(shiny)


shinyUI(fluidPage(
        titlePanel("Analysis of french population in 2009"),
  
        sidebarLayout(
                sidebarPanel(
                        helpText("Hi, use the first slider to choose a population range, it will display a dataframe on the right with the cities included in this specific range."),
                        sliderInput("cities",
                                "Choose a population range",
                                min = 0,
                                max = 2300000,
                                value = c(10000, 100000),
                                step = 1000),
                        helpText("The second slider will determine how many breaks the histogram will have, the minimum is 10 and maximum is 100"),
                        sliderInput("breaks",
                                "Number of histogram breaks:",
                                min = 10,
                                max = 100,
                                value = 50),
                        helpText("Don't forget to hit the update button to update both dataframe and histogram !!!"),
                        submitButton("Update")
    ),
    
        mainPanel(
                dataTableOutput("df"),
                plotOutput("hist1"))
  )
))
