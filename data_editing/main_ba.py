#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import re
import csv
def process_text(input_text, is_activism, file_to_write, category, post_id):
    # Verwende reguläre Ausdrücke, um den Text in Abschnitte zu unterteilen
    sections = re.split(r'\w+\sProfilbild\n', input_text)

    # Entferne leere Abschnitte
    sections = [section.strip() for section in sections if section.strip()]
    # print(sections)
    likes = []

    # Den regulären Ausdruck definieren, um die zweite ganze Zahl zu finden
    number_pattern = r'\d+\sWo\.Gefällt\s([\d.]+)\sMalAntworten'

    # Iteriere durch das ursprüngliche Array
    for section in sections:
        # Führe hier die gewünschten Operationen durch und füge den gewünschten Teil in das neue Array ein
        # In diesem Fall nehmen wir an, dass wir nur die Anzahl der Likes (Gefällt) speichern möchten
        parts = section.split('\n')
        if len(parts) > 1:
            # Mit re.search den regulären Ausdruck im Text suchen
            match = re.search(number_pattern, parts[1])
            if match:
                second_number = match.group(1)
                likes.append(second_number)
            else: 
                likes.append(0)
        else:
            likes.append(0)

    # Das neue Array enthält die gewünschten Daten
    print(len(likes))

    # Entferne Zeilenumbrüche aus jedem Abschnitt und alles, was dahinter kommt
    cleaned_sections = [re.sub(r'\n.*', '', section) for section in sections]
    print(len(cleaned_sections))

    # Prüfe, ob die CSV-Datei bereits existiert
    file_exists = os.path.isfile(file_to_write)

    #print(cleaned_sections)

    #Öffne die CSV-Datei zum Schreiben oder Anhängen
    with open(file_to_write, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Wenn die Datei neu erstellt wird, schreibe die Header-Zeile
        if not file_exists:
            writer.writerow(['ID', 'Text', 'Is_Activism', "Category", "Post_Id", "Like_Count"])

        # Bestimme die ID des letzten Eintrags in der vorhandenen CSV
        id_counter = 1
        if file_exists:
            with open(file_to_write, mode='r', newline='', encoding='utf-8') as read_file:
                reader = csv.reader(read_file)
                # Prüfe, ob die ID-Zeile bereits existiert, und überspringe sie
                header = next(reader, None)
                if header and header[0] == 'ID':
                    id_counter = max(int(row[0]) for row in reader) + 1

        for index, value in enumerate(cleaned_sections):
            # Prüfe, ob die Zeile "Gefällt" enthält
            if is_activism == "true":
                is_activism = True
            else:
                is_activism = False

            # Schreibe die Daten in die CSV-Datei
            writer.writerow([id_counter, value, is_activism, category, post_id, likes[index]])

            # Inkrementiere die ID
            id_counter += 1


## read text from txt file
with open("comments.txt", "r") as file:
    text = file.read()


## if brand-activism
process_text(text, "true", "files/ups.csv", "workplace", "CusEwArgnsF")
