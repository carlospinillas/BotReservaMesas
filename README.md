# grupomp
laguna-ai grupomp
bot cotización buses grupomp
r
Instrucciones de Instalación Rasa 3.0

https://www.youtube.com/watch?v=RVoFqxmG8p0&ab_channel=Rasa
# crear entorno
conda create -n rasa3 python=3.8
conda activate rasa3
# update pip
python -m pip uninstall pip
python -m ensurepip
python -m pip install -U pip

# instalar rasa con todas las dependencias incluido spacy
pip install rasa[full]

# proyecto de prueba, se puede omitir
rasa init

# instalar modelos mediano y modelo de precision (lento), spacy news español
python -m spacy download es_core_news_md
python -m spacy download es_dep_news_trf


# snippets de VS code para etiquetado en yml y otros
# permitir snippets en strings, modificar settings.json modificando flag "strings" : true
{
    "workbench.colorTheme": "Default Dark+",
    "window.zoomLevel": 1,
    "editor.smoothScrolling": true,
    "workbench.list.smoothScrolling": true,
    "editor.quickSuggestions":
    {
        "strings": true
    }
} 

# comando para correr rasa en modo debug (todos los mensajes)
rasa shell --debug

# comando para correr solo nlu
rasa shell nlu