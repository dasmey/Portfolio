## Have total emissions from PM2.5 decreased in the Baltimore City from 1999 to 2008? 
## Use the base plotting system to make a plot answering this question.
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
## Subsetting
Balt <- subset(NEI, fips == "24510")
## Using tapply to sum our PM25 emissions for each year available
sum <- with(Balt, tapply(Emissions, year, sum))
## Creating a new dataframe
Baltsum <- data.frame(Year.Observation = names(sum), Sum.Emissions = sum)
## Barploting
plot2 <- with(Baltsum, barplot(height = Sum.Emissions, names.arg = Year.Observation, xlab = "Years recorded", ylab = "PM25 Emissions in tons", main = "Total of PM25 Emitted from 1999 to 2008 in Baltimore City", density = 25, angle = 12.5, col = "brown"))
## Saving graphic
dev.copy(png, "plot2.png", width = 480, height = 480)
dev.off()