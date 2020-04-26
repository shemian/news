class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title 
        
class Category:
    '''
    Class that instantiates objects of the news
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
        
class Source:
    '''
    Class that that defines the type of source object
    '''
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
class Headline:
    '''
    Class that instantiates objects of the headlines categories objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title

    
        
        