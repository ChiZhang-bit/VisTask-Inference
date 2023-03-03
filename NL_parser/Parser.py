import nltk
from nltk.tree import Tree
from stanfordcorenlp import StanfordCoreNLP


class Parser(object):
    def __init__(self, text: str, nlp: StanfordCoreNLP):
        self.text = text
        self.word_token = nlp.word_tokenize(self.text)  # 分词结果
        self.parse = nlp.parse(self.text)  # str: 语法分析的结果
        self.parse_tree = Tree.fromstring(self.parse)  # tree : 构建形成语法分析树的形式
        self.dependency = nlp.dependency_parse(self.text)  # 句法依存分析
        self.pos_tag = nlp.pos_tag(self.text)  # 词性标注
        self.ner = nlp.ner(self.text)  # 命名实体识别
        self._keyword_map()

    def _keyword_map(self):
        """
        定义 Vis Task Keywords, 用于映射
        :return:
        """
        self.keyword_dict = {
            "characterize_distribution": ["distribution", "frequency"],
            "correlation": ["relationships", "relationship", "correlation", "changes"],
            "sort": ["sort", "rank"],
            "deviation": ["deviation", "disparity"],
            "compare": ["difference", "differ", "comparison"],
            "find_anomalies": ["anomalies", "outlier"],
            "compute_derived_value": ["sum", "average", "max", "min", "mean"],
            "magnitude": ["comparison"],
            "part_to_whole": ["proportion", "part"],
            "trend": ["trend"],
            "range": ["range"]
        }

    def _vis_keyword_map(self):
        self.vis_keyword_dict = {
            "bar_chart": ["bar chart", "bar"],
            "strip_plot": [],
            "pie_chart": [],
            "radial_plot": [],
            "box_plot": [],
            "stacked_bar_chart": [],
            "line_chart": [],
            "multi_series_line_chart": [],
            "scatter_plot": [],
            "horizon_graph": [],
            "ranged_dot_plot": [],
            "parallel_coordinate_plot": [],
            "2D_histogram_heatmap": [],
            "2D_histogram_scatter_plot": [],
            "cell_plot": []
        }

    def draw(self):
        self.parse_tree.draw()

    # 分析属于什么任务, 先把ytj的整合上去吧
    def infer_task(self, parse_tree=None):
        """
        这段由于递归调用的原因，parse_tree单独列出来了一个函数，调用该函数的时候：
        Parser.infer_task()
        :param parse_tree: 递归使用的树，一开始调用的应该是self.parse_tree
        :return:
        """
        # 初次进入递归时使用parse_tree is None
        if parse_tree is None:
            parse_tree = self.parse_tree

        inferred_task_list = []
        if parse_tree.height() == 2:
            if parse_tree.label() in [
                "NN", "IN", "NNS", "NNP", "NNPS", "NR", "NT",
                "RBR", "RBJJ", "JJS", "JJR",
                "VB", "VBS", "VBD", "VBG", "VBN", "VBP", "VBZ"
            ]:
                leaf = parse_tree.leaves()[0]
                task = self.keyword_mapping(leaf)
                if task is not None:
                    inferred_task_list.append(task)
            return inferred_task_list

        elif parse_tree.height() > 2:
            for i in range(len(parse_tree)):
                i_tree = parse_tree[i]
                if i_tree.label() in ["ROOT", "S", "PP", "NP", "VP", "NN", "NR", "NT"]:
                    inferred_task_list.extend(self.infer_task(i_tree))
            return inferred_task_list

    def keyword_mapping(self, leaf):
        """
        根据leaf的值，查找是否有与Keyword匹配的内容
        :param leaf:
        :return: Key or None
        """
        for key in self.keyword_dict.keys():
            if leaf in self.keyword_dict[key]:
                return key
        return None

    def __str__(self):
        return f"The natural language is {self.text}\n" \
               f"The pos_tag is {self.pos_tag}\n" \
               f"The parse result is \n{self.parse}\n"

    def infer_task_new(self):
        """
        推断该对象的自然语言表征的是什么样的任务
        :return:
        """
        pass
