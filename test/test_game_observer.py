import unittest
from azul.game_observer import GameObserver


class TestGameObserver(unittest.TestCase):

    def setUp(self) -> None:
        self.game_observer = GameObserver()
                
    def test_game_observer(self) -> None:
        self.game_observer.register_observer(GameObserver())
        self.assertEqual(len(self.game_observer._observers),1)

        self.game_observer.register_observer(GameObserver())
        self.assertEqual(len(self.game_observer._observers),2)

        observer = GameObserver()
        self.game_observer.register_observer(observer)
        self.assertEqual(len(self.game_observer._observers),3)
        self.game_observer.cancel_observer(observer)
        self.assertEqual(len(self.game_observer._observers),2)


if __name__ == '__main__':

    unittest.main()
