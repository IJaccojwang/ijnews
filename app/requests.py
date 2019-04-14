import urllib.request, json
from .models import Source, Article

api_key = None
base_url = None
source_url = None

def configure_request(app):
    global api_key, base_url, source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    source_url = app.config['NEWS_SOURCE_URL']

def get_sources():
    """
    Function that gets the json response with data on news
    """
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response =json.loads(get_sources_data)
        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')


        source_object = Source(id,name, description, category)
        source_results.append(source_object)

    return source_results

def get_articles(source_id):
    """
    Function that gets json response with data on articles
    """
    get_articles_url = source_url.format(source_id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response =json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(article_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects
    '''
    article_results = []
    for article_item in article_list:
        title = article_item.get('title')
        author = article_item.get('author')
        description = article_item.get('description')
        imgurl = article_item.get('urlToImage')
        url = article_item.get('url')
        time = article_item.get('publishedAt')


        article_object = Article(title, author, description, imgurl, url, time)
        article_results.append(article_object)

    return article_results


def search_article(article_name):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&pageSize=100&apiKey={}'.format(article_name, api_key)

    with urllib.request.urlopen(search_article_url) as url:
        get_articles_data = url.read()
        get_articles_response =json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results
