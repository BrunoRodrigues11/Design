# Manipulando XML de uma NFe e exibindo os resultados em um Data Frame
import xml.etree.ElementTree as ET  # XML Element Tree
from lxml import etree, objectify  # IXML
import pandas as pd  # Pandas

# Remover namespaces do XML
try:
    # Atribuindo o local do arquivo XML a ser manipulado
    metadata = 'nfe.xml'
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(metadata, parser)
    root = tree.getroot()

    for elem in root.getiterator():
        if not hasattr(elem.tag, 'find'):
            continue  # (1)
        i = elem.tag.find('}')
        if i >= 0:
            elem.tag = elem.tag[i+1:]
    objectify.deannotate(root, cleanup_namespaces=True)

    # Salvando o arquivo XML sem os namespaces
    # Pode ser salvo em um arquivo já existente ou em um novo
    tree.write('nfe.xml',
               pretty_print=True, xml_declaration=True, encoding='UTF-8')
except:
    print("Não funcionou")

# Extraindo dados do XML
try:
    # Atribuindo e localizando o XML
    tree = ET.parse("nfe.xml")
    root = tree.getroot()

    # Navegando entre os elementos do XML, em formato cascata
    tag_NFe = root.find("NFe")
    tag_infNFe = tag_NFe.find("infNFe")
    tag_ide = tag_infNFe.find("ide")
    tag_serie = tag_ide.find("serie").text
    tag_nNF = tag_ide.find("nNF").text
    tag_det = tag_infNFe.find("det")
    tag_prod = tag_det.find("prod")
    tag_CFOP = tag_prod.find('CFOP').text
    tag_NCM = tag_prod.find('NCM').text
    tag_xProd = tag_prod.find('xProd').text

    # Exibindo na tela os resultados
    print("funcionou")
except:
    print("Não funcionou")

try:
    info = {'Num NF': [tag_nNF],
            'Série': [tag_serie],
            'Prod': [tag_xProd],
            'CFOP': [tag_CFOP],
            'NCM': [tag_NCM],
            }
    vendas_df = pd.DataFrame(info)
    print(vendas_df)
    print("funcionou")
except:
    print("Não funcionou")
