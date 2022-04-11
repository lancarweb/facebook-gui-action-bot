from .driver.driver import *


class Readnotification:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def action(self):
        # click open button notif
        drivers.execute_script(
            'document.getElementsByClassName("oajrlxb2 qu0x051f esr5mh6w e9989ue4 r7d6kgcz nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x i1ao9s8h esuyzwwr f1sip0of abiwlrkh p8dawk7l lzcic4wl bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv j83agx80 taijpn5t jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 qypqp5cg q676j6op tdjehn4e")[1].click()')

        # filter notif masuk
        drivers.execute_script(
            "document.getElementsByClassName('pq6dq46d is6700om cyypbtt7 fwizqjfa s45kfl79 emlxlaya bkmhp75w spb7xbtv qu0x051f esr5mh6w e9989ue4 r7d6kgcz')[0].click()")

        # click list notif
        drivers.execute_script(
            'document.getElementsByClassName("ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 hpfvmrgz qt6c0cv9 jb3vyjys l9j0dhe7 du4w35lb bp9cbjyn btwxx1t3 dflh9lhu scb9dxdr nnctdnn4")[0].click()')
