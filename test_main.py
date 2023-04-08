import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_h1():
    driver = webdriver.Chrome()
    driver.get("https://plataformavirtual.itla.edu.do/login/index.php")
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    loginbtn = driver.find_element(By.ID, "loginbtn")


    username.send_keys("20212102")
    password.send_keys("1217Abel-")
    loginbtn.click()
    driver.find_element(By.LINK_TEXT, "Mis cursos").click()
    driver.find_element(By.LINK_TEXT, "Mis cursos").click()
    driver.find_element(By.LINK_TEXT, "César Enrique Carrasco Santana").click()
    driver.find_element(By.LINK_TEXT, "Cerrar sesión").click()
    driver.save_screenshot('img.png')
    driver.close()

