# Copyright (c) 2017 Civic Knowledge. This file is licensed under the terms of the
# MIT License, included in this distribution as LICENSE

""" App Urls and generators for  accessing  static files from census.gov"""

from publicdata.census.appurl import CensusUrl
from publicdata.census.util import sub_geoids, sub_summarylevel
from rowgenerators import AppUrlError

class CensusFile(CensusUrl):

    """
    A URL that references row data from American Community Survey files

    census://2016/5/US/tract/B17001

    The general form is:

        census://year/release/geo_containment/summary_level/table

    """

    def __init__(self, url=None, downloader=None, **kwargs):
        super().__init__(url, downloader, **kwargs)

        self._parts # Will raise on format errors

    def _match(cls, url, **kwargs):
        return url.scheme.startswith('census')

    @property
    def _parts(self):
        if not self.netloc:
            # If the URL didn't have ://, there is no netloc
            parts = self.path.strip('/').split('/')
        else:
            parts = tuple([self.netloc] + self.path.strip('/').split('/'))

        if len(parts) != 5:
            raise AppUrlError("Census reporters must have three path components. Got: '{}' ".format(parts)+
                              "Format is census://year/release/geo_containment/summary_level/table ")

        return parts

    @classmethod
    def _match(cls, url, **kwargs):
        return url.scheme.startswith('census')

    @property
    def year(self):
        return self._parts[0]

    @property
    def release(self):
        return self._parts[1]

    @property
    def geoid(self):
        return sub_geoids(self._parts[2])

    @property
    def summary_level(self):
        return sub_summarylevel(self._parts[3])

    @property
    def tableid(self):
        return sub_geoids(self._parts[4])

    def join(self, s):
        raise NotImplementedError()

    def join_dir(self, s):
        raise NotImplementedError()

    def join_target(self, tf):
        raise NotImplementedError()