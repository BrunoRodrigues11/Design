# Manipulando XML de uma NFe e exibindo os resultados em um Data Frame
import xml.etree.ElementTree as ET  # XML Element Tree
from lxml import etree, objectify  # IXML


def clearNamespace():
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
