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
        self._keyword_map()
        self._vis_keyword_map()
        self._task_mapping_vis()

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
            "compute_derived_value_sum": ["sum", "summation", "total"],
            "compute_derived_value_avg": ["average", "avg", "mean"],
            "compute_derived_value_max": ["max", "maximum"],
            "compute_derived_value_min": ["min", "minimum"],
            "magnitude": ["comparison"],
            "part_to_whole": ["proportion", "part"],
            "trend": ["trend"],
            "range": ["range"]
        }

    def _vis_keyword_map(self):
        self.vis_keyword_dict = {
            "stacked bar chart": ["stacked bar chart"],  # 这一条要放在barchart前面判断
            "bar chart": ["bar chart", "barchart", "as bar"],
            "strip plot": ["strip plot", "stripplot", "as strip"],
            "pie chart": ["pie chart", "piechart", "as pie"],
            "radial plot": ["radial plot", "radialplot"],
            "box plot": ["box plot", "boxplot", "box diagram"],
            # 同样的下面的这一条要放在line chart 的前面
            "multi series line chart": ["multi series line chart", "multi line chart", "series line chart", "group line chart"],
            "line chart": ["line chart", "linechart", "line graphs", "line graph"],
            "scatter plot": ["scatter plot", "scatterplot"],
            "horizon graph": ["horizon graph",],
            "ranged dot plot": ["ranged dot plot", "range dot plot"],
            "parallel coordinate plot": ["parallel coordinate plot", "parallel plot"],
            "2D_histogram heatmap": ["histogram heatmap", "heatmap", "2D heatmap"],
            "2D_histogram scatter plot": ["histogram scatter plot"],
            "cell plot": ["cell plot", "dot plot", "dotplot", "cellplot"]
        }

    def _task_mapping_vis(self):
        self.task_mapping_vis_dict = {
            "characterize_distribution": ["bar chart", "stacked bar chart", "box plot"],
            "correlation": ["scatter plot", "line chart"],
            "sort": ["line chart"],
            "deviation": ["bar chart"],
            "compare": ["heatmap", "dot plot"],
            "find_anomalies": ["box plot", "strip plot"],
            "compute_derived_value_sum": ["pie chart", "radial plot"],
            "compute_derived_value_avg": ["bar chart"],
            "compute_derived_value_max": ["bar chart"],
            "compute_derived_value_min": ["bar chart"],
            "magnitude": ["pie chart", "parallel coordinate plot"],
            "part_to_whole": ["pie chart", "radial plot"],
            "trend": ["line chart", "multi series line chart"],
            "range": ["ranged dot plot"]
        }

    def draw(self):
        self.parse_tree.draw()

    def infer_visualization(self):
        for key in self.vis_keyword_dict.keys():
            for keyword in self.vis_keyword_dict[key]:
                if keyword in self.text:
                    return key
        return None

    def infer_task(self, parse_tree=None):
        """
        这段由于递归调用的原因，parse_tree单独列出来了一个函数，调用该函数的时候：
        Parser.infer_task()
        :param parse_tree: 递归使用的树，一开始调用的应该是self.parse_tree
        :return:
        """
        # 初次进入递归时使用parse_tree is None
        print("digui ing")
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

    def inference(self):
        # Step1 : 判断有无直接指明vis type:
        vis_type = self.infer_visualization()
        if vis_type is not None:
            return [vis_type]
        # Step2 : 如果vis_type = None, infer_task:
        task_results = self.infer_task()

        # Step3 : 将分析出的task转换成对应的可视化形式
        vis_results = []
        for task in task_results:
            vis_results.extend(self.task_mapping_vis_dict[task])
        return vis_results

    def __str__(self):
        return f"The natural language is {self.text}\n" \
               f"The pos_tag is {self.pos_tag}\n" \
               f"The parse result is \n{self.parse}\n"
