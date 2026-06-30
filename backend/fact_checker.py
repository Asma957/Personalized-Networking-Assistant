import wikipedia

def fact_check(query: str) -> dict:
    try:
        wikipedia.set_lang("en")
        search_results = wikipedia.search(query, results=3)
        if not search_results:
            return {"found": False, "query": query, "summary": "No information found.", "source": None, "related_topics": []}
        try:
            page = wikipedia.page(search_results[0], auto_suggest=False)
            summary = wikipedia.summary(search_results[0], sentences=3, auto_suggest=False)
            return {"found": True, "query": query, "title": page.title, "summary": summary, "source": page.url, "related_topics": search_results[1:3]}
        except wikipedia.exceptions.DisambiguationError as e:
            page = wikipedia.page(e.options[0], auto_suggest=False)
            summary = wikipedia.summary(e.options[0], sentences=3, auto_suggest=False)
            return {"found": True, "query": query, "title": page.title, "summary": summary, "source": page.url, "related_topics": e.options[1:3]}
        except wikipedia.exceptions.PageError:
            return {"found": False, "query": query, "summary": "Page not found.", "source": None, "related_topics": search_results[1:3]}
    except Exception as e:
        return {"found": False, "query": query, "summary": f"Error: {str(e)}", "source": None, "related_topics": []}