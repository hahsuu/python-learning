import xml.etree.cElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()
print(root.tag)


for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print('---->', i.tag, i.text)


for node in root.iter('year'):
    print(node.tag, node.text)


for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('updated', 'yes')

tree.write('test_new.xml')
