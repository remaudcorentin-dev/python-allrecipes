
from bs4 import BeautifulSoup

import urllib.parse
import urllib.request

import re


class AllRecipes(object):

	@staticmethod
	def search(query_dict):
		"""
		Search recipes parsing the returned html data.
		"""
		base_url = "https://allrecipes.com/search/results/?"
		query_url = urllib.parse.urlencode(query_dict)

		url = base_url + query_url

		html_content = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html_content, 'html.parser')

		search_data = []
		articles = soup.findAll("article", {"class": "grid-col--fixed-tiles"})

		iterarticles = iter(articles)
		next(iterarticles)
		for article in iterarticles:
			data = {}
			try:
				data["name"] = article.find("h3", {"class": "grid-col__h3 grid-col__h3--recipe-grid"}).get_text().strip(' \t\n\r')
				data["description"] = article.find("div", {"class": "rec-card__description"}).get_text()
				data["url"] = article.find("a", href=re.compile('^/recipe/'))['href']
				try:
					data["image"] = article.find("a", href=re.compile('^/recipe/')).find("img")["data-original-src"]
				except Exception as e1:
					pass
			except Exception as e2:
				pass
			search_data.append(data)

		return search_data

	@staticmethod
	def get(uri):
		"""
		'url' from 'search' method.
		 ex. "/recipe/106349/beef-and-spinach-curry/"
		"""
		base_url = "https://allrecipes.com/"
		url = base_url + uri

		html_content = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html_content, 'html.parser')

		ingredients = soup.findAll("li", {"class": "checkList__line"})
		steps = soup.findAll("span", {"class": "recipe-directions__list--item"})

		data = {"ingredients": [],
						"steps": []}

		for ingredient in ingredients:
			str_ing = ingredient.find("span", {"class": "recipe-ingred_txt"}).get_text()
			if str_ing and str_ing != "Add all ingredients to list":
				data["ingredients"].append(str_ing)

		for step in steps:
			str_step = step.get_text()
			if str_step:
				data["steps"].append(str_step)

		return data
