import grabReviewJSON
from wordcloud import WordCloud, STOPWORDS

reviews = grabReviewJSON.get_n_reviews('814540',2000)
reviewList = [x['review'] for x in reviews]
collapsedList = ' '.join(reviewList)
STOPWORDS.update(['hr','b','h1','o','u', 'game'])
wordcloud = WordCloud(collocation_threshold = 3, width=1600, height=800).generate(text=collapsedList)
wordcloud.to_file('wordcloud.png')