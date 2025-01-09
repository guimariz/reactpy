from reactpy import component, html, run
from base_dados import obras

@component
def Galeria():
    indice_obra = 0

    obra = obras[indice_obra]
    nome = obra["name"]
    artista = obra["artist"]
    descricao = obra["description"]
    imagem_url = obra["url"]

    componente = html.div(
        html.h3(nome), # nome
        html.img({"src":imagem_url, "style": {"height": "200px", "border": "solid"}}), # foto da obra
        html.p(descricao), # descricao
        html.p(f"Artista: {artista}"), # nome do artista
        html.button("Anterior", {"on_click": obra_anterior}), # anterior
        html.button("Próxima", {"on_click": obra_proxima}), # proximo
        html.p(f"Obra {indice_obra + 1}/{len(obras)}"), # Obra
    )
    return componente

@component
def App():
    pagina = html.div(
        html.h1("Obras de Arte"),
        Galeria()
    )
    return pagina

run(App)