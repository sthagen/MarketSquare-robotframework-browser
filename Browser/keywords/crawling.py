from typing import Set

from robotlibcore import keyword  # type: ignore

from Browser.base import LibraryComponent

from ..utils import logger


class Crawling(LibraryComponent):
    @keyword(tags=["Crawling"])
    def crawl_site(self, url):
        """
        Take screenshots from all urls inside a specific site.
        """
        self.library.new_page()
        self._crawl(url, url, set())

    def _crawl(self, href: str, baseurl: str, crawled: Set[str]):
        if not href.startswith(baseurl):
            return
        if href in crawled:
            return
        logger.info(f"Crawling url {href}")
        logger.console(f"Crawling url {href}")
        self.library.go_to(href)
        self.library.take_screenshot()
        crawled.add(href)
        links = self.library.get_elements("//a[@href]")
        child_hrefs = [self.library.get_attribute(link, "href") for link in links]
        for child_href in child_hrefs:
            self._crawl(child_href, baseurl, crawled)
