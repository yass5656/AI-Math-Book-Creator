from core.models.book_request import BookRequest


class BookPlanner:

    def build(self, request: BookRequest):

        return {

            "title": f"{request.curriculum} Stage {request.stage} Term {request.term}",

            "book_type": request.book_type,

            "theme": request.theme,

            "units": [

                {
                    "unit": 1,
                    "pages": []
                }

            ]

        }
