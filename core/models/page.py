class Page:

    def __init__(
        self,
        number=None,
        title="",
        content=None,
        page_type="practice"
    ):
        self.number = number
        self.title = title
        self.content = content or {}
        self.page_type = page_type
        self.exercises = []

    def display(self):
        return {
            "page": self.number,
            "title": self.title,
            "type": self.page_type,
            "content": self.content
        }
