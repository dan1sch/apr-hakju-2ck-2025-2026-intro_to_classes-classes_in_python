"""
Übung 3: Song mit Listen

Aufgabe:
Erstelle eine Klasse `Song` mit:
- Konstruktor mit Parametern: titel (String) und interpreten (Liste, z.B. ["Artist1", "Artist2"])
- Methode interpret_hinzufuegen(name) mit Parameter:
  - Fügt einen neuen Interpreten zur Liste hinzu
  - Gibt aus "🎤 {name} wurde hinzugefügt"
- Methode zeige_info() ohne Parameter:
  - Zeigt Titel und alle Interpreten an
- Methode anzahl_interpreten() ohne Parameter:
  - Gibt die Anzahl der Interpreten zurück
- Methode play() ohne Parameter:
  - Gibt aus "▶️ Song '{titel}' wird gespielt..."

Erstelle einen Song mit einem Titel und 2 Interpreten deiner Wahl,
zeige die Info, füge einen weiteren Interpreten hinzu, zeige die Anzahl und die Info nochmal.
Spiele dann den Song ab.

💡 Tipps:
- self.interpreten.append(name) fügt ein Element zur Liste hinzu
- len(self.interpreten) gibt die Anzahl der Elemente zurück
- Mit einer for-Schleife kannst du alle Interpreten ausgeben
- Du kannst beliebige Interpreten und Titel verwenden!

Beispiel Ergebnis:
🎵 Song: Summer Vibes
   Interpreten: DJ Max, Sarah Sound
🎤 Beat Producer wurde hinzugefügt
👥 Anzahl Interpreten: 3
🎵 Song: Summer Vibes
   Interpreten: DJ Max, Sarah Sound, Beat Producer
▶️ Song 'Summer Vibes' wird gespielt...
"""

# TODO: Erstelle hier die Klasse Song
class song:
    def __init__(self, titel, interpreten):
        self.titel = titel
        self.interpreten = interpreten
        print(f"Neuer Song mit Titel {self.titel} & Interpreten {self.interpreten} wurde erstellt.")

    def zeige_info(self):
        print(f"Neuer Song mit Titel {self.titel} & Interpreten {self.interpreten} wurde erstellt.")
    
    def interpret_hinzufuegen(self, neuer_interpret):
        self.interpreten.append(neuer_interpret)
        print(f"{neuer_interpret} wurde hinzugefügt")
        print(f"Allke Interpreten: {self.interpreten}")

    def anzahl_interpreten(self):
        return len(self.interpreten)
    
    def play_song(self):
        print(f"Song {self.titel} wird gespielt")
       
# TODO: Erstelle einen Song mit einem Titel und 2 Interpreten deiner Wahl
song_1 = song(titel="Die with a smile", interpreten= ["Bruno Mars", "Lady Gaga"])
song_2 = song(titel = "Zombie", interpreten= ["Cranberries"])
song_3 = song(titel = "My Only Angel", interpreten= ["Yungblud", "Aerosmith"])

# TODO: Zeige die Song-Info
song_1.zeige_info()

# TODO: Füge einen weiteren Interpreten hinzu
song_2.interpret_hinzufuegen("DJ Lenzi")
song_1.interpret_hinzufuegen("Katja")


# TODO: Zeige die Anzahl der Interpreten
number_artists = song_1.anzahl_interpreten()
print(number_artists)

# TODO: Zeige die Song-Info erneut
song_1.zeige_info()

# TODO: Spiele den Song ab
song_1.play_song()