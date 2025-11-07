import unittest
from statistics_service import StatisticsService
from player import Player
from statistics_service import main

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_main(self):
        main()

    def test_get_player(self):
        nimi = self.stats.search("Kurri")         
        self.assertEqual(nimi.name, "Kurri")

    def test_get_only_real_player(self):
        nimi = self.stats.search("Rantanen")
        self.assertIsNone(nimi)

    def test_get_players_in_team(self):
        pelaajat = self.stats.team("EDM")
        self.assertEqual(len(pelaajat), 3)
    
    def test_unknown_team(self):
        pelaajat = self.stats.team("MIN")
        self.assertEqual(pelaajat, [])

    def test_top_players(self):
        parhaat = self.stats.top(3)
        self.assertEqual(len(parhaat), 3)

    def test_ordered_by_points(self):
        parhaat = self.stats.top(3)
        pisteet = [p.points for p in parhaat]
        self.assertEqual(pisteet, sorted(pisteet, reverse=True))

    def test_best_player_most_points(self):
        paras = self.stats.top(1)[0]
        self.assertEqual(paras.name, "Gretzky")
    
    def test_return_all_players(self):
        pelaajat = self.stats.top(100)
        self.assertEqual(len(pelaajat), 5)
