import json
import webbrowser

from youtube_search import YoutubeSearch


class YouTube_Automation:
    def __init__(self, search_query, results_no):
        results = YoutubeSearch(search_query, max_results=results_no).to_json()
        self.video_list = json.loads(results)["videos"]

    def get_urls(self):
        urls = []
        for details in self.video_list:
            url = "https://www.youtube.com{}".format(details["url_suffix"])
            urls.append(url)
        return urls

    def info(self):
        for details in self.video_list:
            title = details["title"]
            url = "https://www.youtube.com{}".format(details["url_suffix"])
            duration = details["duration"]
            views = details["views"]
            channel = details["channel"]
            result = """

            Title : {}
            Duration : {}
            Views : {}
            Channel : {}
            Url : {}

            """.format(
                title, duration, views, channel, url
            )
            print(result)

    def play(self):
        for item in self.get_urls():
            webbrowser.open_new_tab(item)


if __name__ == "__main__":
    query = str(input("Enter the Query: "))
    num = int(input("Enter the number of Videos: "))
    video = YouTube_Automation(query, num)
    prompt = """
    
        [1] Play in Browser
        [2] Print the videos Information
    """
    print(prompt)
    option = int(input("Enter the Mode: "))

    if option == 1:
        video.play()
    if option == 2:
        video.info()
    else:
        print("Invalid Mode")
