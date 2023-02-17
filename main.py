import nltk
from nltk.tokenize import sent_tokenize
from nltk.tree import Tree
from stanfordcorenlp import StanfordCoreNLP
from utils import *

nlp = StanfordCoreNLP(r'D:\Homework\nlp\stanford-corenlp-4.5.1', lang='en')

sentence = 'Show the relationship between budget and rating for Action and Adventure movies that grossed over 100M.'
print('分词:', nlp.word_tokenize(sentence))

token = nlp.word_tokenize(sentence)
# for i in token:
#     if i.lower() in characterize_distribution_keywords:
#         print("Task: characterize distribution")
#         break
input()

# print('词性标注：', nlp.pos_tag(sentence))
# print('命名实体分析', nlp.ner(sentence))

tree1 = nlp.parse(sentence)
print('解析语法\n', tree1)
# Tree.fromstring(tree1).draw()
# print('解析语法关系', nlp.dependency_parse(sentence))
ttree = Tree.fromstring(tree1)

dfs(ttree)
nlp.close()
















#
# vp = Tree('VP', [Tree('V', ['saw']),  Tree('NP', ['him'])])
# s = Tree('S', [Tree('NP', ['I']), vp])
# print(s)
#
#
# print(s[1, 1])
#
# t = Tree.fromstring("(S (NP I) (VP (V saw) (NP him she)))")
#
# t[1][1].set_label('X')
#
#
# # t[1][1].children()
# print(t)
#
# t[0], t[1, 1] = t[1, 1], t[0]
# print(t)

