class HtmlGenerator(object):
    def __init__(self,file):
        self.file = file

    def tag(self,inner_html,tags):
        tag = f"<{tags}>{inner_html}</{tags}>" + "\n"
        file = open(self.file,"a")
        file.write(tag)


    def link_tag(self,href,inner_html):
        tag = f"<a href='{href}'>{inner_html}</a>"
        file = open(self.file,"a")
        file.write(tag)

    def img_tag(self,src,alt):
        tag = f"<img src={src} alt={alt}>"
        file = open(self.file,"a")
        file.write(tag)

    def clear(self):
        f = open(self.file,"w")
        f.write("")
        f.close()

    def close(self):
        self.file.close()

class HtmlViewer(object):   
    def __init__(self,file):
        import webbrowser
        import os
        dirs = os.getcwd()
        webbrowser.open("file:///{}/{}".format(dirs,file))
