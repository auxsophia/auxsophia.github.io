AUTHOR = 'Philosopher Scholar'
SITENAME = 'philosopherscholar'
SITEURL = ""

PATH = "content"

# If you want the blog save it as 'blog.html'
INDEX_SAVE_AS = 'blog.html'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'En'

THEME = 'themes/philosopher-theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

# DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DEFAULT_DATE = 'fs'

# Tell Pelican where to look for articles vs static pages
ARTICLE_PATHS = ['_posts']
PAGE_PATHS = ['_pages']
STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
    'images/logo-1.png': {'path': 'favicon.ico'}
}

# Clean URLs for static pages
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Clean URLs for blog articles
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

# Move the chronological blog feed to a subfolder
# if you ever want to link someone to your feed of articles, you can just send them to https://philosopherscholar.com/blog/).
INDEX_URL = 'blog/'
INDEX_SAVE_AS = 'blog/index.html'

# Plugin settings
PLUGINS = ['pelican.plugins.yaml_metadata']

# Tell Pelican to build a 404.html page from the theme templates
DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives', '404']

DELETE_OUTPUT_DIRECTORY = True