# 使用的函数
characterize_distribution_keywords = ["distribution", "frequency"]
correlation_keywords = ["relationships","relationship","correlation","changes","with"]
sort_and_ranking_keywords=["rank"]
deviation_keywords=["deviation","disparity"]
compare_keywords=["difference","differ","comparison"]
find_anomalies_keywords=["anomalies"]
compute_derived_value_keywords=["compute","sum", "average", "max", "min", "mean"]
magnitude_keywords=["comparison"]
part_to_whole_keywords=["count","proportion"]
trend_keywords=["wave","trend"]
range_keywords=["range"]
typestr='none'

def dfs(tree):
    if tree.height()==2:
        if tree.label() in ["NN","IN","NNS","NNP","NNPS","NR","NT",
                            "RBR","RBJJ","JJS","JJR",
                            "VB","VBS","VBD","VBG","VBN","VBP","VBZ"]:
            lef = tree.leaves()[0]
            typestr=findtype(lef)
            print(typestr)
            return

    elif tree.height()>2:
        #h=tree.height()-1
        # for s in tree.subtrees(lambda tree: tree.height() == h):
        for i in range(len(tree)):
            i_tree=tree[i]
            flag=0   #判断该词的位置是否是关键位置
            if i_tree.label() in ["ROOT","S","PP","NP","VP","NN","NR","NT"]:
                flag=1
            if (flag==1):
                dfs(i_tree)
        return

def findtype(leave):
    str_r="none"
    if leave in characterize_distribution_keywords:
        str_r="Task: characterize distribution"
    elif leave in correlation_keywords:
        str_r="Task: correlation "
    elif leave in sort_and_ranking_keywords:
        str_r="Task: sort_and_ranking"
    elif leave in deviation_keywords:
        str_r="Task: deviation "
    elif leave in compare_keywords:
        str_r="Task: compare"
    elif leave in find_anomalies_keywords:
        str_r="Task: find_anomalies"
    elif leave in compute_derived_value_keywords:
        str_r="Task: compute_derived_value"
    elif leave in magnitude_keywords:
        str_r="Task: magnitude"
    elif leave in  part_to_whole_keywords:
        str_r="Task: part_to_whole"
    elif leave in trend_keywords:
        str_r="Task: trend"
    elif leave in range_keywords:
        str_r="Task: range"
    return str_r
