## Across the United States, how have emissions from coal combustion-related sources changed from 1999–2008?

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
## Now we need to find coal sources in the SCC data
coal <- grep("Coal", SCC$EI.Sector)
SCC_coal_list <- SCC$SCC[coal]

## We can now subset from our main data
coal_comb <- NEI %>%
        select(SCC, Emissions, year) %>%
        filter(SCC %in% SCC_coal_list) %>%
        group_by(SCC, year) %>%
        summarise(Emissions = sum(Emissions) / 1000000) %>%
        arrange(year)
        
## GGPlot time
library(ggplot2)
plot4 <- ggplot(data = coal_comb, aes(factor(year), Emissions, fill=year))
plot4 <- plot4 + geom_bar(stat = "identity") + labs(x = "Years recorded", y = "PM25 Emissions in millions of tones", title = "PM25 emissions from coal sources in the US from 1999 to 2008") + theme(plot.title = element_text(hjust = 0.5))

## PNG save
dev.copy(png, "plot4.png", width = 480, height = 480)
dev.off()