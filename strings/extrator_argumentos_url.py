class ExtratorArgumentosUrls:

    def __init__(self, url):
        if not self.url_valida(url):
            raise LookupError("URL inválida")
        self.url = url

    def url_valida(self, url):
       return url

    def extrai_argumentos(self):

        busca_moeda_origem = "moedaorigem"

        busca_moeda_destino = "moedadestino"

        indice_inicial_moeda_destino = self.url.find(busca_moeda_destino) + len(busca_moeda_destino) + 1

        indice_inicial_moeda_origem = self.url.find(busca_moeda_origem) + len(busca_moeda_origem) + 1
        indice_final_moeda_origem = self.url.find("&")

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:]

        return moeda_origem, moeda_destino