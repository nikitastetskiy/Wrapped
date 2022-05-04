from app.entities.wrapped import Wrapped


def parse_wrapped(item):

    title = item['title']
    summary = item['summary']
    image = item['image']
    popularity = item['popularity']

    return Wrapped(title, summary, image, popularity)
