from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles, search_article


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources()
    title = 'Home - Welcome to IJNews, Your one stopshop for all the latest news updates'

    query_article = request.args.get('article_query')

    if query_article:
        return redirect(url_for('.search',article_name = query_article))
    else:
        return render_template('index.html', title = title, news_sources = news_sources )

@main.route('/source/<source_name>')
def source(source_name):
    '''
    View function to display the search results
    '''
    articles = get_articles(source_name)
    title = source_name
    query_article = request.args.get('article_query')

    if query_article:
        return redirect(url_for('.search',article_name = query_article))
    else:
        return render_template('source.html',title = title , news_articles = articles)



@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'Search results for {article_name}'
    name = article_name
    query_article = request.args.get('article_query')

    if query_article:
        return redirect(url_for('.search',article_name = query_article))
    else:
        return render_template('search.html',title = title,name = name , news_articles = searched_articles)
