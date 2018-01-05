"""LA Times Articles Preprocessing"""
import sys

def parse_xml(xmlfile):
    """Parse xml and return a list of documents as strings"""
    new_doc = None
    for line in xmlfile:
        if line.strip() == '<text>':
            new_doc = ''
        if line.strip() == '</text>':
            yield new_doc
            new_doc = None
        if new_doc is not None:
            if not line.startswith('<'):
                new_doc += line


def main():
    """Main"""
    path = sys.argv[1]
    with open(path) as (xmlfile):
        docs = parse_xml(xmlfile)


if __name__ == '__main__':
    main()
