# This program categorizes a word as positive or negative.
# It also categorizes a user’s tweets as positive or negative.
# Background:-
# "Sentiment analysis," otherwise known as "opinion mining," involves inference of sentiment (i.e., #opinion) from text. For instance, movie reviews on Rotten Tomatoes are often positive or negative. #So are product reviews on Amazon. Similarly do opinions underlie many tweets on Twitter.
#
#Some words tend to have positive connotations (e.g., "love"), while some words tend to have negative #connotations (e.g., "hate"). And so, if someone were to tweet "I love you", you might infer positive #sentiment. And if someone were to tweet "I hate you", you might infer negative sentiment. Of course, #individual words alone aren’t always reliable, as "I do not love you" probably isn’t a positive #sentiment, but let’s not worry about those cases. Some words, meanwhile, have neither positive nor  # negative connotations (e.g., "the").
#
# A few years back, Dr. Minqing Hu and Prof. Bing Liu of the University of Illinois at Chicago kindly # put together lists of 2006 positive words and 4783 negative words. We’ll use those to classify      #  tweets! But first a tour.