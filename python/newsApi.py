from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='0c0d7d15b5e74591b1c6a9c16a10545c')
# To recieve the top headlines.

top_headlines = newsapi.get_top_headlines(q='{}}',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='en')
return requests.post
