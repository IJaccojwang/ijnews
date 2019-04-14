class Source:
    """
    Source class to define News Source objects
    """
    def __init__(self, id, name, description, category):
        self.id = id
        self.name = name
        self.description = description
        self.category = category

class Article:
    """
    Article class to define how articles are rendered
    """
    def __init__(self, title, author, description, imgurl, url, time):
        self.title = title
        self.author = author
        self.description = description
        self.imgurl = imgurl
        self.url = url
        self.time = time
