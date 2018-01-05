"""LA Times Articles Preprocessing"""
import sys
from sklearn.feature_extraction.text import CountVectorizer
from itertools import groupby

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


def build_word_counts(docs):
    # Initialize an fit CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(docs).T.tocoo() # Transpose matrix and set appropiate format
    # Get vocabulary
    words = cv.get_feature_names()
    # Build finall structure
    result = {}
    sorted_occurrences = sorted(zip(X.row, X.col, X.data), key=lambda x: x[0])
    groups = groupby(sorted_occurrences, key=lambda x: x[0])
    for w_id, w_list in groups:
        w_list = [(x[1], x[2]) for x in w_list]
        result[words[w_id]] = list(w_list)
    return result


def main():
    """Main"""
    path = sys.argv[1]
    with open(path) as (xmlfile):
        docs = parse_xml(xmlfile)
        build_word_counts(docs)

if __name__ == '__main__':
    main()
