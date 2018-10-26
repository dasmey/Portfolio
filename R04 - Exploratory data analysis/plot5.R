## How have emissions from motor vehicle sources changed from 1999–2008 in Baltimore City?

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

## Now we need to find Vehciles sources in the SCC data
vehicles <- grep("Vehicles", SCC$EI.Sector)
SCC_vehicles_list <- SCC$SCC[vehicles]

## We can now subset from our main data
vehicles <- NEI %>%
        select(fips, SCC, Emissions, year) %>%
        filter((SCC %in% SCC_vehicles_list) & (fips == "24510")) %>%
        group_by(SCC, year) %>%
        summarise(Emissions = sum(Emissions)) %>%
        arrange(year)

## GGPlot time
library(ggplot2)
plot5 <- ggplot(data = vehicles, aes(factor(year), Emissions, fill=year))
plot5 <- plot5 + geom_bar(stat = "identity") + labs(x = "Years recorded", y = "PM25 Emissions in tones", title = "PM25 emissions from motor vehicle sources in Baltimore City from 1999 to 2008") + theme(plot.title = element_text(hjust = 0.5))

## PNG save
dev.copy(png, "plot5.png", width = 720, height = 720)
dev.off()