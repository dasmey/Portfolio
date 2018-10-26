## Have total emissions from PM2.5 decreased in the United States from 1999 to 2008? 
## Using the base plotting system, make a plot showing the total PM2.5 emission from all sources for each of the years 1999, 2002, 2005, and 2008.

## First objective, getting the url
url <- "https://d396qusza40orc.cloudfront.net/exdata%2Fdata%2FNEI_data.zip"
## Then we download the data & unzip
download.file(url, "data.zip", method = "auto")
unzip <- unzip("data.zip")
## Here we use dplyr to store our data in a more easy to read dataframe
library(dplyr)
SCC <- tbl_df(readRDS(unzip[1]))
NEI <- tbl_df(readRDS(unzip[2]))
## checking Nas
sum(is.na(NEI))
## We convert our Year column from integer to date class
Dates <- NEI$year
Dates <- as.Date(as.character(NEI$year), "%Y")
## Using tapply to sum our PM25 emissions for each year available
sum <- with(NEI, tapply(Emissions, year, sum))
## Creating a new dataframe
NEIsum <- data.frame(Year.Observation = names(sum), Sum.Emissions = sum)
## Barploting
plot1 <- with(NEIsum, barplot(height = Sum.Emissions / 1000000, names.arg = Year.Observation, xlab = "Years recorded", ylab = "PM25 Emissions in millions of tons", main = "Total of PM25 Emitted from 1999 to 2008 in the US", density = 25, angle = 12.5, col = "brown"))
## Saving graphic
dev.copy(png, "plot1.png", width = 480, height = 480)
dev.off()
