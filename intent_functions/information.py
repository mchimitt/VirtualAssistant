import wikipedia as wiki

#def wikiSearch(text):


try:
    print(wiki.summary("potato", sentences=1, auto_suggest=False))

except:
    print("Hmm I was not able to find anything.")
