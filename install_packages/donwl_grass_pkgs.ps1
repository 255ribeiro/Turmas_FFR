$url = 'https://github.com/255ribeiro/intro_revit/raw/master/docs/revit/DADOS/projeto_revit/pastas_do_projeto.zip'
$downZip = 'D:\gitrepos\Turmas_FFR\zipfile.zip'

Invoke-WebRequest $url -OutFile $downZip

# $webConect = New-Object -TypeName System.Net.WebClient
# $webConect.DownloadFile($url, $downZip)

$extDir = 'D:\gitrepos\Turmas_FFR\extract' # diretório precisa exixtir
$extractor = New-Object -ComObject Shell.Application
$files = $extractor.NameSpace($downZip).Items()
$extractor.NameSpace($extDir).CopyHere($files)
