from typing import List

from azul.ObserverInterface import ObserverInterface


class GameObserver(ObserverInterface):
    _observers: List[ObserverInterface]

    def __init__(self):
        self._observers: List[ObserverInterface] = []

    def register_observer(
            self,
            observer: ObserverInterface,
    ) -> None:
        self._observers.append(observer)

    def cancel_observer(
            self,
            observer: ObserverInterface,
    ) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_everybody(
            self,
            state: str,
    ) -> None:
        for observer in self._observers:
            observer.notify(state)
