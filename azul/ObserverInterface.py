from azul.interfaces import ObserverInterface as ObserverSimpleInterface


class ObserverInterface(ObserverSimpleInterface):
    def notify(
            self,
            new_state: str,
    ) -> None:
        print(new_state)
