from sample.entity.Keyword import Keyword


class User:

    def __init__(self, user):
        self.db_user = user
        self.email = user["email"]
        self.keyword_list = []
        if user["keyword_list"]:
            for item in user["keyword_list"]:
                self.keyword_list.append(Keyword(item["search_text"], item["key"], item["checked_key"]))

    def append_user_search_text(self, search_text, key, checked_key):
        for item in self.keyword_list:
            if item.search_text == search_text: raise ValueError('Keyword already exist')

        self.keyword_list.append(Keyword(search_text, key, checked_key))

    def update_keyword(self, search_text, key, checked_key):
        for item in self.keyword_list:
            if item.search_text == search_text: item.key = key

    def save(self):
        self.db_user["email"] = self.email
        self.db_user["keyword_list"] = []
        for item in self.keyword_list:
            self.db_user["keyword_list"].append({'search_text': item.search_text, 'key': item.key, 'checked_key': item.checked_key})

        self.db_user.save()
