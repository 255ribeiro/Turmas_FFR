
import zipfile, io

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('requests')


import requests, zipfile, io
url = 'https://github.com/255ribeiro/intro_revit/raw/master/docs/revit/DADOS/projeto_revit/pastas_do_projeto.zip'
extDir = 'D:\gitrepos\Turmas_FFR\extract'

r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(extDir)