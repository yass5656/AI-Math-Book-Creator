class PageTemplate:

    def create(
        self,
        title,
        content,
        page_type="lesson"
    ):

        return {
            "title": title,
            "type": page_type,
            "content": content,
            "footer": "Smart Start © Yasser Elsaady"
        }

