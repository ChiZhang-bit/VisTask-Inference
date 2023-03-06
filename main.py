from stanfordcorenlp import StanfordCoreNLP
from NL_parser import *
from utils import *

if __name__ == "__main__":
    path_LX = r"F:\stanford-corenlp-4.5.1"
    path_Linc = r"D:\stanford-corenlp-4.5.2"
    nlp = StanfordCoreNLP(path_LX, lang='en')

    sentence = 'Show the relationship between budget and rating for Action and Adventure movies that ' \
               'grossed over 100M. '
    sentence = "Show me the part of the whole using bar chart"
    parser = Parser(text=sentence, nlp=nlp)
    # print(parser)
    # print(parser.infer_task())
    # print(parser.infer_visualization())
    print(parser.inference())

    nlp.close()
