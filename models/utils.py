'''
Created on Jan 12, 2012

@author: charliezhang
'''
from xml.dom.minidom import parse, parseString

TEXT_DATA = '#text'

def node_to_dict(parent):
    obj = {}

    for i in range(0, parent.attributes.length):
        attr = parent.attributes.item(i)
        obj[attr.name] = attr.value

    for node in parent.childNodes:
        key = node.nodeName
        if node.nodeType == node.TEXT_NODE:
            textdata = node.data.strip()
            if textdata == None or textdata == '': continue
            obj[key] = node.data
        elif node.nodeType == node.CDATA_SECTION_NODE:
            key = TEXT_DATA
            obj[key] = node.wholeText.strip()
        else:
            value = node_to_dict(node)
            if not obj.has_key(key):
                obj[key] = value
            elif obj.has_key and type(obj[key]) != list:
                obj[key] = [obj[key], value]
            else: obj[key].append(value)
    
    return obj
    
def xml_to_obj(xml, root_tag_name):
    dom = parseString(xml)
    roots = dom.getElementsByTagName(root_tag_name)
    #root = dom.getDocumentElement()
    objs = []
    for root in roots:
        obj = node_to_dict(root)
        objs.append(obj)
        
    return objs
