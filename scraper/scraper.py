#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import Utils

__author__ = 'prs-watch'

class Scraper(object):
	DELIMITER = '/'
	BASE_URL = 'http://gd2.mlb.com/components/game/mlb'
	YMD_FORMAT = 'year_{year}/month_{month}/day_{day}'
	PARSER = 'lxml'

	def __init__(self, timestamp, box):
		"""
		init
		:param timestamp: day
		:param box: game no to check boxscore
		"""
		self.params = {
			'year'	:	timestamp[0:4]
		,	'month'	:	timestamp[4:6]
		,	'day'	:	timestamp[6:8]
		}

		self.box = box

	def _get_games(self):
		base_url = self.DELIMITER.join([
				self.BASE_URL
			,	self.YMD_FORMAT.format(**self.params)
			,	'epg.xml'
			])
		html = Utils.get_content(base_url,self.PARSER)
		return Utils.find_all_tags(html,'game')