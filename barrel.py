"""
Dojo-POA, Fande, 9 de Outubro de 2010
=====================================

Problema: http://www.rubyquiz.com/quiz30.html

Participantes
-------------

  - Dorneles Tremea, @dorneles, dorneles@tremea.com
  - Gabriel Engel, @gabrielengel, gabriel@fande.com.br
  - Leandro Nunes, --, leandron85@gmail.com
  - Guilherme Ruduit, @gruduit, guiruduit@gmail.com
  - Miguel Grazziotin, @miguelgraz, miguelgraz@gmail.com

Pontos Positivos
----------------

  - Pringles :-)
  - Ambiente massa na Fande!
  - Bem divertido!
  - Variedade de topicos abordados na linguagem
  - Uso de modulos extra: os, urllib, random, minidom, gzip
  - Zeh Marreta (Controle de tempo): http://is.gd/fVgy6
  - Bom problema, pode ser explorado de varias formas
  - Resolvemos o problema (sort of...)

Pontos Negativos
----------------

  - Pouca gente
  - Faltou Coca-Cola
  - Muito tempo em cima da documentacao dos modulos
  - Faltou teste para tratamento de caracteres nao alfabeticos
  - Metodos sem docstring
"""

import os, gzip, random, urllib
from xml.dom import minidom


class BarrelOfMonkeys(object):

    def __init__(self, url="http://rubyquiz.com/SongLibrary.xml.gz",
                 filename='songs.xml.gz'):
        self.url = url
        self.filename = filename
        self.songs = self.parse(self.get_xml())

    def download(self):
        url_handler = urllib.urlopen(self.url)
        content = url_handler.read()
        url_handler.close()
        file_handler = file(self.filename, 'w')
        file_handler.write(content)
        file_handler.close()

    def get_xml(self):
        # Check if already downloaded, time saving!
        if not os.path.exists(self.filename):
            self.download()
        gzip_handler = gzip.open(self.filename)
        xml_content = gzip_handler.read()
        gzip_handler.close()
        return xml_content

    def parse(self, xml):
        results = []
        tree = minidom.parseString(xml)
        library = tree.firstChild
        songs_tags = library.getElementsByTagName('Song')
        for song in songs_tags:
            results.append(song.getAttribute('name'))
        return results

    def first_song(self):
        return self.songs[0]

    def random_song(self):
        return random.choice(self.songs)

    def next_song(self, current_song):
        last_letter = current_song[-1].lower()
        for song in self.songs:
            if song[0].lower() == last_letter:
                self.songs.remove(song)
                return song

    def playlist(self, first_song, total):
        results = []
        results.append(first_song)
        while len(results) < total:
            first_song = self.next_song(first_song)
            results.append(first_song)
        return results


if __name__ == '__main__':
    barrel = BarrelOfMonkeys()
    a_song = barrel.random_song()
    playlist = barrel.playlist(a_song, 10)
    for song in playlist:
        print song
