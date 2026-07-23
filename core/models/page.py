class Page:

    def __init__(
        self,
        number,
        title,
        content,
        page_type
    ):
        self.number = number
        self.title = title
        self.content = content
        self.page_type = page_type


    def display(self):

        return {
            "page": self.number,
            "title": self.title,
            "type": self.page_type,
            "content": self.content
        }
