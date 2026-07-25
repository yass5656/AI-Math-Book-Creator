class Watermark:

    def __init__(self, text="Smart Start © Yasser Elsaady"):
        self.text = text

    def apply(self, page):
        page["watermark"] = self.text
        return page
