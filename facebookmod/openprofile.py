from .scrolltimeline import *
from time import sleep


class Actionprofile:
    def __init__(self):
        pass

    def action_profile(self, username, notifyProgress, target, driver, By, Keys, message, timeout=1, comment=True, emoji=True, like=True):
        message = message
        timeout = timeout
        comment = comment
        emoji = emoji
        like = like

        # open_target_user | loading
        while True:
            sleep(1)
            try:
                driver.find_element(
                    By.XPATH, '//*[@class="ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 hpfvmrgz qt6c0cv9 jb3vyjys l9j0dhe7 du4w35lb bp9cbjyn btwxx1t3 dflh9lhu scb9dxdr nnctdnn4"]')
                break
            except:
                pass

        # getProfiles
        # driver.get(target)

        # scroll
        scroll_op = 0
        while True:
            sleep(1)
            if scroll_op == 10:
                break
            try:
                scrolltimelines(driver, By, Keys)
                notifyProgress.emit(
                    "{}-> scrolling the page..".format(username))
            except:
                pass

            scroll_op += 1

        # wait
        while True:
            sleep(0.5)
            try:
                commelms = driver.find_elements(
                    By.XPATH, '//p[@class="hcukyx3x oygrvhab cxmmr5t8 kvgmc6g5"]')

                break
            except:
                pass

        # comments
        n = 0
        for comm in commelms:
            print(n)
            try:
                if comment:
                    # comment
                    sleep(timeout)
                    comm.click()
                    sleep(timeout)
                    comm.send_keys(str(message))

                if emoji:
                    # emoji
                    sleep(timeout)
                    driver.execute_script(
                        "document.getElementsByClassName('o6r2urh6 l9j0dhe7 b3i9ofy5 e72ty7fz qlfml3jp inkptoze qmr60zad rt8b4zig n8ej3o3l agehan2d sk4xxmp2 j83agx80 buofh1pr bkfpd7mw')[{}].getElementsByClassName('oajrlxb2 gs1a9yip mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o tgvbjcpo hpfvmrgz i1ao9s8h esuyzwwr f1sip0of du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql btwxx1t3 abiwlrkh p8dawk7l lzcic4wl dwo3fsh8 g5ia77u1 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 pq6dq46d kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 pzggbiyp pkj7ub1o bqnlxs5p kkg9azqs c24pa1uk ln9iyx3p fe6kdd0r ar1oviwq l10q8mi9 sq40qgkc s8quxz6p pdjglbur')[0].click()".format(str(n)))

                    sleep(timeout)
                    driver.find_element(By.XPATH, '//img[@alt="😀"]').click()

                if like:
                    # like
                    sleep(timeout)
                    driver.execute_script(
                        'document.getElementsByClassName("rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw i1fnvgqd gs1a9yip owycx6da btwxx1t3 ph5uu5jm b3onmgus e5nlhep0 ecm0bbzt nkwizq5d roh60bw9 mysgfdmx hddg9phg")[{}].getElementsByClassName("rq0escxv l9j0dhe7 du4w35lb j83agx80 rj1gh0hx buofh1pr g5gj957u hpfvmrgz taijpn5t bp9cbjyn owycx6da btwxx1t3 d1544ag0 tw6a2znq jb3vyjys dlv3wnog rl04r1d5 mysgfdmx hddg9phg qu8okrzs g0qnabr5")[0].click()'.format(str(n)))
                notifyProgress.emit(
                    "{}-> Reactions | Comment | Emoji | Like".format(username))
                n += 1
            except:
                pass
