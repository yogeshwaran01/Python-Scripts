"""
Usage:
-----
    python instagram_hashtags_post.py
    
Input:
-----
    Enter The Hashtag Names: cat dog python
    Enter the number of Post in each Hashtag upto 65: 5
    
        [1] Download
        [2] Open    

    Enter the mode: 1
    Done!
    
"""
import webbrowser

from instagramy import InstagramHashTag
import requests


class Bulk_HashTag_Post_Download:
    """
    Class Download or Open top 65 posts from Instagram Hashtag
    """

    def __init__(self, hashtag_name_list: list, limit=None):

        self.hashtags = hashtag_name_list
        self.limit = limit

    def get_info(self, hashtag):

        tag = InstagramHashTag(hashtag)

        if self.limit:
            return tag.top_posts[: self.limit]

        return tag.top_posts

    def write(self, posts_info):

        url = posts_info["display_url"]
        _id = posts_info["shortcode"]
        file_name = "{}.jpeg".format(_id)
        r = requests.get(url, stream=True)
        if r.ok:
            file = open(file_name, "wb")
            file.write(r.content)
            return True
        else:
            return False

    def download(self):

        if type(self.hashtags) is list:

            for i in self.hashtags:
                for j in self.get_info(i):
                    self.write(j)

        else:

            for i in self.get_info(self.hashtags):
                self.write(i)

        return True

    def open_in_browser(self):

        if type(self.hashtags) is list:

            for i in self.hashtags:
                for j in self.get_info(i):
                    webbrowser.open(j["display_url"])

        else:

            for i in self.get_info(self.hashtags):
                webbrowser.open(i["display_url"])

        return True


if __name__ == "__main__":

    prompt = """
        [1] Download
        [2] Open 
    """

    query = input("Enter The Hashtag Names: ").split()
    limit = int(input("Enter the number of Post in each Hashtag upto 65: "))
    print(prompt)
    mode = int(input("Enter the mode: "))

    t = Bulk_HashTag_Post_Download(query, limit=limit)
    if mode == 1:
        t.download()
        print("Done!")
    else:
        t.open_in_browser()
        print("Done!")
