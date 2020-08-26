from time import sleep
import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import URL


usuario_facebook = input("Digite aqui seu email de acesso ao Facebook: ")
senha = getpass.getpass("Entre com sua senha: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
print(" - Abrindo o Facebook")
sleep(1)

campo_usuario = driver.find_element_by_id('email')
campo_usuario.send_keys(usuario_facebook)
print(" - Inserindo usuário no campo de e-mail")

campo_senha = driver.find_element_by_id('pass')
campo_senha.send_keys(senha)
print(" - Inserindo a senha do usuário")

botao_login = driver.find_element_by_id('loginbutton')
botao_login.click()
print(" - Completando o acesso")
input(" - Pressione qualquer tecla para sair")
sleep(1)
driver.quit()
print("FINALIZADO")