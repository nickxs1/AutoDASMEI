import asyncio
from selenium import webdriver

async def Ativar_Selenium():
    # Configurar o URL WebSocket
    websocket_url = "ws://localhost:9222/devtools/page/E48B0E674FAF737E4E9F11860EEE518C"
    
    # Iniciar o driver do Selenium com a opção --headless
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    
    # Conectar ao navegador Chrome em execução
    driver = webdriver.Remote(command_executor=websocket_url, desired_capabilities={}, options=options)
    
    # Abrir uma nova guia
    driver.execute_script("window.open('about:blank','_blank');")
    
    # Alternar para a nova guia
    driver.switch_to.window(driver.window_handles[-1])
    
    # Execute o código JavaScript na nova guia
    driver.get('https://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao')
    
    script = """
    var novaJanela = window.open('https://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao');
    novaJanela.addEventListener('load', function() {
        novaJanela.document.querySelector('#cnpj').value = '43.253.733/0001-40';
        novaJanela.document.querySelector('#continuar').click();
    });
    """
    driver.execute_script(script)

    # Aguarde algum tempo
    await asyncio.sleep(10)

    # Feche a nova guia
    driver.close()
    
    # Encerre o driver
    driver.quit()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Ativar_Selenium())
