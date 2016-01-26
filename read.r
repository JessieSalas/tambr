library(syuzhet)

filename <- "macbeth.txt"

book = gsub( "[\r\n]", " ", readChar(filename, file.info(filename)$size) )

sentences <- get_sentences(book)

sentiment_vector <- get_sentiment( sentences, method="afinn" )


# plot( sentiment_vector, type="l",  main="Example Plot Trajectory",  xlab = "Narrative Time", ylab= "Emotional Valence" )

ft_values <- get_transformed_values(sentiment_vector, low_pass_size = 3, x_reverse_len = 100,scale_vals = TRUE,scale_range = FALSE)

percent_vals <- get_percentage_values(sentiment_vector)
#plot(percent_vals, type="l", main="Sentiment Arches in Macbeth", xlab = "Narrative Time", ylab= "Emotional Valence", col="red")

#var(sentiment_vector)
plot(ft_values, type ="h", main ="Sentiment Arches in Shakespeare's Macbeth", xlab = "Narrative Time", ylab = "Emotional Valence", col = "red")
