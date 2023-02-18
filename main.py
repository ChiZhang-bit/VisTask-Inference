from stanfordcorenlp import StanfordCoreNLP
from NL_parser import *
from utils import *

if __name__ == "__main__":
    nlp = StanfordCoreNLP(r'D:\stanford-corenlp-4.5.2', lang='en')

    sentence = 'Show the relationship and distribution between budget and rating for Action and Adventure movies that grossed over 100M.'
    parser = Parser(text=sentence, nlp=nlp)
    # print(parser)
    print(parser.infer_task())
    input()

    # print('分词:', nlp.word_tokenize(sentence))
    # print('词性标注：', nlp.pos_tag(sentence))
    # print('命名实体分析', nlp.ner(sentence))

    tree1 = nlp.parse(sentence)
    print(type(tree1))
    print('解析语法\n', tree1)

    ttree = Tree.fromstring(tree1)
    print(type(ttree))
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

