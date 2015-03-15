      _____       _                          _                 
     / ____|     | |                        | |                
    | (___   ___ | | __ _ _ __ ___ _   _ ___| |_ ___ _ __ ___  
     \___ \ / _ \| |/ _` | '__/ __| | | / __| __/ _ \ '_ ` _ \ 
     ____) | (_) | | (_| | |  \__ \ |_| \__ \ ||  __/ | | | | |
    |_____/ \___/|_|\__,_|_|  |___/\__, |___/\__\___|_| |_| |_|
                                   __/ |                      
                                  |___/       

# Table of contents

1. Angabe
2. Known Bugs
3. TODO/ Quellen

## Angabe

"Wir wollen nun unser Wissen aus Medientechnik und SEW nützen um eine etwas kreativere Applikation zu erstellen.

Eine wichtige Library zur Erstellung von Games mit 3D-Grafik ist Pygame. Die 3D-Unterstützung wird mittels PyOpenGL erreicht.

Die Kombination ermöglicht eine einfache und schnelle Entwicklung.

Während pygame sich um Fensteraufbau, Kollisionen und Events kümmert, sind grafische Objekte mittel OpenGL möglich.

Die Aufgabenstellung:

Erstellen Sie eine einfache Animation unseres Sonnensystems:

In einem Team (2) sind folgende Anforderungen zu erfüllen.

Ein zentraler Stern
Zumindest 2 Planeten, die sich um die eigene Achse und in elliptischen Bahnen um den Zentralstern drehen
Ein Planet hat zumindest einen Mond, der sich zusätzlich um seinen Planeten bewegt
Kreativität ist gefragt: Weitere Planeten, Asteroiden, Galaxien,...
Zumindest ein Planet wird mit einer Textur belegt (Erde, Mars,... sind im Netz verfügbar)
Events:

Mittels Maus kann die Kameraposition angepasst werden: Zumindest eine Überkopf-Sicht und parallel der Planentenbahnen
Da es sich um eine Animation handelt, kann diese auch gestoppt werden. Mittels Tasten kann die Geschwindigkeit gedrosselt und beschleunigt werden.
Mittels Mausklick kann eine Punktlichtquelle und die Textierung ein- und ausgeschaltet werden.
Schatten: Auch Monde und Planeten werfen Schatten.
Hinweise:

Ein Objekt kann einfach mittels glutSolidSphere() erstellt werden.
Die Planten werden mittels Modelkommandos bewegt: glRotate(), glTranslate()
Die Kameraposition wird mittels gluLookAt() gesetzt
Bedenken Sie bei der Perspektive, dass entfernte Objekte kleiner - nahe entsprechende größer darzustellen sind.
Wichtig ist dabei auch eine möglichst glaubhafte Darstellung. gluPerspective(), glFrustum()
Für das Einbetten einer Textur wird die Library Pillow benötigt! Die Community unterstützt Sie bei der Verwendung.

Tutorials:
Pygame: https://www.youtube.com/watch?v=K5F-aGDIYaM
Viel Erfolg! " [1]

## TODO/ Known Bugs

- Unter Python 3.4 ist die Performance deutlich schlechter, als unter Python 3.3
- Das Licht ist nicht richtig positioniert
- Die Umlaufbahn der Planeten ist noch zu verbessern

## Quellen

[1]	https://elearning.tgm.ac.at/mod/assign/view.php?id=31709, zuletzt aufgerufen am 16.03.2015