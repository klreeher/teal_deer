---
title: Syntax Highlight Demo
author: Anonymus
summary: Code Syntax Demo
keywords: code
category: articles
tags: demo
---

## Python Syntax Highlighting

There are two ways to specify the identifier:

    :::python
    print("The triple-colon syntax will *not* show line numbers.")

To display line numbers, use a path-less shebang instead of colons:

    #!python
    print("The path-less shebang syntax *will* show line numbers.")


## YAML Syntax Highlighting


	#!yaml
	language: python
	python:
	  - '3.8'
	# command to install dependencies
	install: "make"
	# command to run tests
	script:
	  - |
	    make init
	    make publish
	#    make github
	deploy:
	  provider: pages
	  github_token: $GITHUB_ACCESS
	  target_branch: gh-pages
	  local_dir: output
	  skip_cleanup: true
	  on:
	    branch: master


## JSON 


	#!json
	{
		"id": "0001",
		"type": "donut",
		"name": "Cake",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" },
						{ "id": "1003", "type": "Blueberry" },
						{ "id": "1004", "type": "Devil's Food" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5007", "type": "Powdered Sugar" },
				{ "id": "5006", "type": "Chocolate with Sprinkles" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	}