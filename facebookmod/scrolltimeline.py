# scroll Time Lines
def scrolltimelines(driver, By, Keys):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
