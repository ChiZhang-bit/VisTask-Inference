import nltk
from nltk.tokenize import sent_tokenize
from nltk.tree import Tree
from stanfordcorenlp import StanfordCoreNLP
from treenode.node import *

a = zcnode(1)
a.print_value()

characterize_distribution_keywords = ["distribution", "frequency"]

nlp = StanfordCoreNLP(r'F:\stanford-corenlp-4.5.1', lang='en')

sentence = 'Video becomes a new way of communication between Internet users with the proliferation of sensor-rich mobile devices.'
print('分词:', nlp.word_tokenize(sentence))

token = nlp.word_tokenize(sentence)
for i in token:
    if i.lower() in characterize_distribution_keywords:
        print("Task: characterize distribution")
        break
input()

print('词性标注：', nlp.pos_tag(sentence))
# print('命名实体分析', nlp.ner(sentence))

tree1 = nlp.parse(sentence)
print('解析语法\n', tree1)
Tree.fromstring(tree1).draw()


print('解析语法关系', nlp.dependency_parse(sentence))



nlp.close()
