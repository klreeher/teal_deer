
# teal deer


[![Build Status](https://travis-ci.org/klreeher/teal_deer.svg?branch=master)](https://travis-ci.org/klreeher/teal_deer)




tl;dr.


## technical choices

- pelican static site
- travis ci build 
- github pages deploy -- see at: 
- pipenv

### pipenv cheat sheet

update: pipenv update --outdated
https://pipenv-fork.readthedocs.io/en/latest/basics.html


### pelican cheat

reserved / default file metadata:

```
	title: 
	date: YYYY-MM-DD HH:SS
	modified: YYYY-MM-DD HH:SS
	tags: Content tags, separated by commas
	keywords: Content keywords, separated by commas (HTML content only)
	category: Content category (one only — not multiple)
	slug: Identifier used in URLs and translations
	author: Content author, when there is only one
	authors: Content authors, when there are multiple
	summary: Brief description of content for index pages
	lang: en
	translation: false #If content is a translation of another (true or false)
	status: [draft, hidden, published]
	template: Name of template to use to generate content (without extension)
	save_as: Save content to this relative file path
	url: URL to use for this article/page
```

other metadata for plugins:
  

## other


https://klreeher.github.io/teal_deer/

WARNING: Feeds generated without SITEURL set properly may not be valid