request <- GET("https://api.github.com/users/jtleek/repos", gtoken)
stop_for_status(req)
output <- content(req)
