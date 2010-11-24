import unittest
from barrel import BarrelOfMonkeys


class BarrelTestCase(unittest.TestCase):

    def test_get_xml_returns_a_string(self):
        barrel = BarrelOfMonkeys()
        self.assertEqual(type(barrel.get_xml()), str)

    def test_parse_returns_a_list(self):
        barrel = BarrelOfMonkeys()
        xml = barrel.get_xml()
        self.assertEqual(type(barrel.parse(xml)), list)

    def test_first_song_returns_the_first_song(self):
        barrel = BarrelOfMonkeys()
        first_song = barrel.first_song()
        self.assertEqual(first_song, 'Caught Up In You')

    def test_next_song_starts_with_last_letter(self):
        barrel = BarrelOfMonkeys()
        first_song = barrel.first_song()
        second_song = barrel.next_song(first_song)
        self.assertEqual(first_song[-1].lower(),
                         second_song[0].lower())

    def test_playlist(self):
        barrel = BarrelOfMonkeys()
        first_song = barrel.first_song()
        playlist = barrel.playlist(first_song, 10)
        # Starts at the second song
        for song in playlist[1:]:
            last_char = first_song[-1].upper()
            first_song = song
            self.assertEqual(last_char,
                             first_song[0].upper())
