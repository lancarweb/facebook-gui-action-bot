from .driver.driver import *


class Watchvideo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def action(self):
        # klik ulangi 2 x untuk membuka video
        drivers.execute_script(
            'document.getElementsByClassName("i09qtzwb rq0escxv n7fi1qx3 pmk7jnqg j9ispegn kr520xx4 nhd2j8a9")[0].click()')
