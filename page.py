class Page:
    def __init__(self, page_id):
        self.id = page_id
        self.links = []

    def __str__(self):
        return str(self.id) + ' links: ' + str([x.id for x in self.links])

    def get_links(self):
        return self.links

    def get_id(self):
        return self.id

    def add_link(self, link):
        self.links.append(link)

    def add_links(self, links):
        self.links.extend(links)
