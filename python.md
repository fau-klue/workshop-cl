# Python

## was ist Python?
- Allzweck-Programmiersprache
- muss nicht kompiliert werden (Skriptsprache)
- interaktiver Interpreter
- leicht lesbarer Programmcode
- dynamische Typisierung (duck typing)
- große Standardbibliothek

## Installation
- Python ist auf sinnvollen Betriebssystemen vorinstalliert
- wenn nicht (bspw. MS Windows), siehe [hier](https://www.python.org/downloads/)
- wir verwenden im Folgenden `python3.9`, andere halbwegs neuere Versionen sollten auch kompatibel sein

## Jupyter Notebook
- Web-App, die lokal läuft
- kombiniert Programmcode mit Markdown
- gut geeignet für Analysen und Auswertungen
- Export als HTML für Berichte
- [Installation](https://jupyter.org/install.html) über

        pip install notebook

- nach erfolgreicher Installation kann der Server gestartet werden

        juypter notebook

## Requirements
- in den Notebooks werden die Module benutzt, die im [Requirements-File](requirements.txt) aufgeführt sind
- Installation über

        pip install -r requirements.txt
        
- Zusätzlich sollten folgende Ressourcen heruntergeladen werden:
    + für [SoMeWeTa](https://github.com/tsproisl/SoMeWeTa):
        - [German Newspaper Model](https://corpora.linguistik.uni-erlangen.de/someweta/german_newspaper_2020-05-28.model)
        - [German Web and Social Media Model](https://corpora.linguistik.uni-erlangen.de/someweta/german_web_social_media_2020-05-28.model)
        - [English Newspaper Model](https://corpora.linguistik.uni-erlangen.de/someweta/english_newspaper_2017-09-15.model)
    + für Stanza:
        - englisches Modell: `python3.9 -c 'import stanza; stanza.download("en")'`
    + für spaCy:
        - englisches Modell: `python3.9 -m spacy download en_core_web_sm`

## Entwicklungsumgebungen
- [Übersicht](https://wiki.python.org/moin/PythonEditors)
- Empfehlung:
    + professionelle IDE ([PyCharm](https://www.jetbrains.com/pycharm/)) oder
    + Editor inkl. Shell ([Emacs](https://www.emacswiki.org/emacs/PythonProgrammingInEmacs))

## Virtuelle Umgebungen
- insb. um Versionskonflikte zu vermeiden, ist es sinnvoll, virtuelle Umgebungen zu verwenden
- anlegen, aktivieren, Requirements installieren, deaktivieren (auf Linux):

        python3.9 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        deactivate
    
- für Jupyter-Notebooks verfügbar machen:

        python3.9 -m ipykernel install --user --name=venv

- kann dann beim Anlegen eines Notebooks oder via `Kernel > Change Kernel` ausgewählt werden
