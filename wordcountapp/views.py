from django.shortcuts import render
from django.http import HttpResponse
import re
from collections import Counter

globalResult = {}


def index(request):
    print(locals)
    return render(request, "index.html", locals())


def calculate(request):
    if request.method == "POST":
        showWords = request.POST.get("show_words")
        textInput = request.POST.get("text_input")

        if (showWords == "") or (textInput == "") or (textInput == "0"):
            return HttpResponse("Bad request, please do not leave empty fields!")

        global globalResult
        result = analyze(textinput=textInput, wordsInAnalysis=int(showWords))
        globalResult = result

    return render(request, "index.html", locals())


def analyze(textinput, wordsInAnalysis):

    # Remove anything that is not a word:
    dictResult = {}
    dictResult["initial"] = textinput
    textinput = re.sub("[^a-zA-Z]", " ", textinput)
    textinput = textinput.split()
    words = [
        word for word in textinput if len(word) > 3]
    dictResult["all"] = words
    # print("\n\n")

    TopWordsNumber = 0

    TopDictionary = Counter(words).most_common(wordsInAnalysis)
    dictResult["top"] = TopDictionary
    for i in TopDictionary:
        TopWordsNumber += int(words.count(i[0]))

    TotalWords = len(words)
    DiffWordsTotal = len(set(words))
    PercentUniqueWordsOverAllUnique = int(
        (wordsInAnalysis / DiffWordsTotal) * 100)
    PercentUniqueWordsUsedInTime = int((TopWordsNumber / len(words)) * 100)
    dictResult["TotalWords"] = TotalWords
    dictResult["DiffWordsTotal"] = DiffWordsTotal
    dictResult["TopWordsNumber"] = TopWordsNumber
    dictResult[
        "PercentUniqueWordsOverAllUnique"] = PercentUniqueWordsOverAllUnique
    dictResult["PercentUniqueWordsUsedInTime"] = PercentUniqueWordsUsedInTime
    dictResult["wordsInAnalysis"] = wordsInAnalysis

    return dictResult
