from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import csv
import os
from transformers import pipeline

# Ermitteln Sie das aktuelle Arbeitsverzeichnis (wo sich Ihre Python-Datei befindet)
aktuelles_verzeichnis = os.getcwd()

sentiment_analyse = pipeline("sentiment-analysis")

# Pfad zur CSV-Datei
csv_datei_pfad = os.path.join(aktuelles_verzeichnis, "files", "exxon.csv")

# Öffnen Sie die CSV-Datei im Lesemodus
with open(csv_datei_pfad, 'r', newline='') as csv_datei:
    csv_reader = csv.reader(csv_datei)
    
    # Schleife zum Lesen der Zeilen in der CSV-Datei
    for zeile in csv_reader:
        print(zeile)
        # Analysieren Sie das Sentiment
        ergebnis = sentiment_analyse(zeile[1])

        # Zeigen Sie das Ergebnis an
        print(ergebnis)

