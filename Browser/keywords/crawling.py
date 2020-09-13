from robotlibcore import keyword  # type: ignore

from Browser.base import LibraryComponent


class Crawling(LibraryComponent):
    @keyword(tags=["Crawling"])
    def crawl_site(self, url):
        pass
