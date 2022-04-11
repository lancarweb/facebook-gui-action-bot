from .driver.driver import *
from copypaste import copy, paste


class Watchstory:
    def __init__(self, messages):
        self.messages = messages

    def action(self):
        # buka daftar story
        drivers.execute_script(
            'document.getElementsByClassName("oajrlxb2 qu0x051f esr5mh6w e9989ue4 r7d6kgcz nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x i1ao9s8h esuyzwwr f1sip0of abiwlrkh p8dawk7l lzcic4wl bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv j83agx80 taijpn5t jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 qypqp5cg q676j6op hn33210v m7msyxje m9osqain")[0].click()')

        # click story mulai dari putaran ke-2 -> default
        drivers.execute_script(
            'document.getElementsByClassName("j83agx80 qu0x051f esr5mh6w e9989ue4 r7d6kgcz beltcj47 p86d2i9g aot14ch1 kzx2olss nhd2j8a9 ihxqhq3m kvgmc6g5 oi9244e8 oygrvhab h676nmdw hzawbc8m cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr pdl3lqly gfay22hk")[2].click()')

        # click field comment story
        drivers.find_element(
            By.XPATH, '//*[@class="p1ueia1e ni8dbmo4 stjgntxs k4urcfbm"]').click()

        # copy
        copy(self.messages)

        # paste
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).send_keys(
            'V').key_up(Keys.CONTROL).perform()

        # enter
        action = ActionChains(driver)
        action.key_down(Keys.ENTER).perform()
