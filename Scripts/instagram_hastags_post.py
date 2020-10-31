"""
This scripts Automatically scrape the instagram hashtags posts
and open image in webbrowser
"""
from instagramy import InstagramHashTag
from webbrowser import open


def get_tags(tag, no_of_results):

    tags = InstagramHashTag(tag)

    return tags.posts_display_urls[:no_of_results]


if __name__ == "__main__":
    tag = input("Enter the Hashtag Name: ")
    no_of_post = int(input("Enter the number of posts open in browser: "))

    for i in get_tags(tag, no_of_post):
        open(i)
