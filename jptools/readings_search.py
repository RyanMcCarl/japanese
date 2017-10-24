def search(reading, kanji):
  matches = set()
  for char in kanji.keys():
    readings = set()
    for onyomi in kanji[char]["onyomi"]:
      readings.add(onyomi.strip("[]',"))
    for kunyomi in kanji[char]["kunyomi"]:
      readings.add(kunyomi.strip("[]',"))
    if reading in readings:
      matches.add((kanji[char]["rank"]) + ',' + char)
  matches = list(matches)
  matches.sort()
  return matches
