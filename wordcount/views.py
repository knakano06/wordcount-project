from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # go to home.htm and output whatever is in home.htm
    #, {"hithere": "this is me"}
    return render(request, "home.htm")

#def eggs(request):
#    return HttpResponse("Eggs are great!")

def count(request):
    # should give back whatever we have after "fulltext" in the URL
    # i.e. the phrase user entered
    fulltext = request.GET["fulltext"]

    # splits the word into lists at the space
    wordlist = fulltext.split()

    # worddictionary is equal to an empty dictionary
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # increase the number
            worddictionary[word] += 1
        else:
            # add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.htm", {"fulltext": fulltext, "count":len(wordlist), "sortedwords":sortedwords})


def about(request):
    return render(request, "about.htm")
