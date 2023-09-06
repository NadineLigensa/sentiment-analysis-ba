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

    # Entferne Zeilenumbrüche aus jedem Abschnitt und alles, was dahinter kommt
    cleaned_sections = [re.sub(r'\n.*', '', section) for section in sections]

    # Prüfe, ob die CSV-Datei bereits existiert
    file_exists = os.path.isfile(file_to_write)

    # Öffne die CSV-Datei zum Schreiben oder Anhängen
    with open(file_to_write, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Wenn die Datei neu erstellt wird, schreibe die Header-Zeile
        if not file_exists:
            writer.writerow(['ID', 'Text', 'Is_Activism', "Category", "Post_Id"])

        # Bestimme die ID des letzten Eintrags in der vorhandenen CSV
        id_counter = 1
        if file_exists:
            with open(file_to_write, mode='r', newline='', encoding='utf-8') as read_file:
                reader = csv.reader(read_file)
                # Prüfe, ob die ID-Zeile bereits existiert, und überspringe sie
                header = next(reader, None)
                if header and header[0] == 'ID':
                    id_counter = max(int(row[0]) for row in reader) + 1

        for section in cleaned_sections:
            # Prüfe, ob die Zeile "Gefällt" enthält
            if is_activism == "true":
                is_activism = True
            else:
                is_activism = False

            # Schreibe die Daten in die CSV-Datei
            writer.writerow([id_counter, section, is_activism, category, post_id])

            # Inkrementiere die ID
            id_counter += 1


## read text from txt file
with open("comments.txt", "r") as file:
    text = file.read()


## if not brand-activism
process_text(text, "true", "files/patagonia.csv", "Environmental", "CvfJSnmrDE-")
