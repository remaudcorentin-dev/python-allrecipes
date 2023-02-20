# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib.parse
import urllib.request

import re
import ssl


class AllRecipes(object):

	@staticmethod
	def search(search_string):
		"""
		Search recipes parsing the returned html data.
		"""
		base_url = "https://allrecipes.com/search?"
		query_url = urllib.parse.urlencode({"q": search_string})

		url = base_url + query_url

		req = urllib.request.Request(url)
		req.add_header('Cookie', 'euConsent=true')

		handler = urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
		opener = urllib.request.build_opener(handler)
		response = opener.open(req)
		html_content = response.read()

		soup = BeautifulSoup(html_content, 'html.parser')

		search_data = []
		articles = soup.findAll("a", {"class": "mntl-card-list-items"})

		articles = [a for a in articles if a["href"].startswith("https://www.allrecipes.com/recipe/")]

		for article in articles:
			data = {}
			try:
				data["name"] = article.find("span", {"class": "card__title"}).get_text().strip(' \t\n\r')
				data["url"] = article['href']
				try:
					data["rate"] = len(article.find_all("svg", {"class": "icon-star"}))
					try:
						if len(article.find_all("svg", {"class": "icon-star-half"})):
							data["rate"] += 0.5
					except Exception:
						pass
				except Exception as e0:
					data["rate"] = None
				try:
					data["image"] = article.find('img')['data-src']
				except Exception as e1:
					try:
						data["image"] = article.find('img')['src']
					except Exception as e1:
						pass
					if "image" not in data:
						data["image"] = None
			except Exception as e2:
				pass
			if data:
				search_data.append(data)

		return search_data

	@staticmethod
	def _get_name(soup):
		return soup.find("h1", {"id": "article-heading_2-0"}).get_text().strip(' \t\n\r')

	@staticmethod
	def _get_rating(soup):
		return float(soup.find("div", {"id": "mntl-recipe-review-bar__rating_2-0"}).get_text().strip(' \t\n\r'))

	@staticmethod
	def _get_ingredients(soup):
		return [li.get_text().strip(' \t\n\r') for li in soup.find("div", {"id": "mntl-structured-ingredients_1-0"}).find_all("li")]

	@staticmethod
	def _get_steps(soup):
		return [li.get_text().strip(' \t\n\r') for li in soup.find("div", {"id": "recipe__steps_1-0"}).find_all("li")]

	@staticmethod
	def _get_times_data(soup, text):
		return soup.find("div", {"id": "recipe-details_1-0"}).find("div", text=text).parent.find("div", {"class": "mntl-recipe-details__value"}).get_text().strip(' \t\n\r')

	@classmethod
	def _get_prep_time(cls, soup):
		return cls._get_times_data(soup, "Prep Time:")

	@classmethod
	def _get_cook_time(cls, soup):
		return cls._get_times_data(soup, "Cook Time:")

	@classmethod
	def _get_total_time(cls, soup):
		return cls._get_times_data(soup, "Total Time:")

	@classmethod
	def _get_nb_servings(cls, soup):
		return cls._get_times_data(soup, "Servings:")

	@classmethod
	def get(cls, url):
		"""
		'url' from 'search' method.
		 ex. "/recipe/106349/beef-and-spinach-curry/"
		"""
		# base_url = "https://allrecipes.com/"
		# url = base_url + uri

		req = urllib.request.Request(url)
		req.add_header('Cookie', 'euConsent=true')

		handler = urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
		opener = urllib.request.build_opener(handler)
		response = opener.open(req)
		html_content = response.read()

		soup = BeautifulSoup(html_content, 'html.parser')

		elements = [
			{"name": "name", "default_value": ""},
			{"name": "ingredients", "default_value": []},
			{"name": "steps", "default_value": []},
			{"name": "rating", "default_value": None},
			{"name": "prep_time", "default_value": ""},
			{"name": "cook_time", "default_value": ""},
			{"name": "total_time", "default_value": ""},
			{"name": "nb_servings", "default_value": ""},
		]

		data = {"url": url}
		for element in elements:
			try:
				data[element["name"]] = getattr(cls, "_get_" + element["name"])(soup)
			except:
				data[element["name"]] = element["default_value"]

		return data
