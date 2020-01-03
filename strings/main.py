from extrator_argumentos_url import ExtratorArgumentosUrls

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"

# url = ""

argumento = ExtratorArgumentosUrls(url)

print(argumento.extrai_argumentos())