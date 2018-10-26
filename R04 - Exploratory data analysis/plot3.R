## Of the four types of sources indicated by the type (point, nonpoint, onroad, nonroad) variable, which of these four sources have seen decreases in emissions from 1999–2008 for Baltimore City? 
## Which have seen increases in emissions from 1999–2008? 
## Use the ggplot2 plotting system to make a plot answer this question.

## First objective, getting the url
url <- "https://d396qusza40orc.cloudfront.net/exdata%2Fdata%2FNEI_data.zip"
## Then we download the data & unzip
download.file(url, "data.zip", method = "auto")
unzip <- unzip("data.zip")
## Here we use dplyr to store our data in a more easy to read dataframe
library(dplyr)
SCC <- tbl_df(readRDS(unzip[1]))
NEI <- tbl_df(readRDS(unzip[2]))
## We convert our Year column from integer to date class
Dates <- NEI$year
Dates <- as.Date(as.character(NEI$year), "%Y")
## Subsetting and grouping with dplyr
Balt <- NEI %>%
        filter(fips == "24510") %>%
        group_by(type, year) %>%
        summarise(Emissions = sum(Emissions))
## GGPlot time
plot3 <- ggplot(Balt, aes(x = factor(year), Emissions, fill = type))
plot3 <- plot3 + facet_grid(. ~ type) + geom_bar(stat = "identity") + labs(x = "Year Recorded", y = "PM 25 Emissions in tons", title = "PM25 emitted from 1999 to 2008 in Baltimore City by source type") + theme(plot.title = element_text(hjust = 0.5))
## And graphic to finish
dev.copy(png, "plot3.png", width = 480, height = 480)
dev.off()
