from .driver.driver import *


class Readmessenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def action(self):
        # click button messenger
        drivers.execute_script(
            'document.getElementsByClassName("oajrlxb2 qu0x051f esr5mh6w e9989ue4 r7d6kgcz nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x i1ao9s8h esuyzwwr f1sip0of abiwlrkh p8dawk7l lzcic4wl bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv j83agx80 taijpn5t jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 qypqp5cg q676j6op tdjehn4e")[2].click()')

        # filter list message masuk
        drivers.execute_script(
            "document.getElementsByClassName('pq6dq46d is6700om cyypbtt7 fwizqjfa s45kfl79 emlxlaya bkmhp75w spb7xbtv qu0x051f esr5mh6w e9989ue4 r7d6kgcz')[0]")

        # click open messenger
        drivers.execute_script(
            'document.getElementsByClassName("oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o tgvbjcpo hpfvmrgz l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb btwxx1t3 abiwlrkh p8dawk7l lzcic4wl ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi a8c37x1j kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr")[0].click()')
