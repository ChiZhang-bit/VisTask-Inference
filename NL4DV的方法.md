## NL4DV 中使用的分析任务的方法

Task List:

```json
NL4DV主要包含四种Task:

find_extreme:
	MIN
	MAX

filter:
	LT(less than)
	GT(greater than)
	EQ(equal)
	RANGE

derived_value:
	MEDIAN
	AVG
	SUM

distribute:
	None

outlier:
	None

correlation:
	None
	
negation:
	None

Trend:
	None
```



Task Keyword Map:

```json
使用的数据结构：

"rank" : [
    ("find_extremum", "MIN")
]
其中，rank 表示的是关键词， find_extremum表示的是寻找的任务， MIN表示的是对任务的描述。

这个数据的意思是：
对于识别到的rank关键词，判定为find_extremum任务中的MIN子任务
```



Task Analytic Way:

+ 根据Task Keywords Map方法 确定 Task：

+ 根据不同的Task，根据任务，判断对应的方法：

  核心函数：generate_task

  ```python
  def generate_tasks(self, task_name, attributes, query_phrase, operator_phrase, operator, values, inference_type, allow_subset=False):
     	"""
     	主要包含以下操作：
     	0. 得到属性的数据类型
     	1. 判断值是否具有歧义
     	2. 判断属性是否具有歧义
     	3. self.new_task得到本身的task_obj，确定其是否在task_list
     	4. 返回识别的task
     	"""
  ```

  + Correlartion:  at least 1 attribute to make sense:

    + 实际上是判断其中关键词的词性 判断关键词语的之间的关系，如果是连词的话怎样的去处理
    + 判断relevant attribute，相关的属性，把任务和属性联系在一起

  + Derived_value\ Find_extreme\ Trend:

    + 332行：先找到keyword, operator_phrase，
    + 之后判断句法依赖树的词性，同样根据operator和_keyword, 判断task机制。

  + Numerica + Temporal Filters

    ```
    less than 50
    since 1946
    ...
    ```

    + CD 判断是不是数词 - 之后把Keyword 和 amount从句法依赖树中提取出来
    + 判断有无negtive（否定词）提取operator_phrase 以及 keyword
    + 提取keyword，attributes，value，tasks

  + Numeric + Temporal Filters

    ```
    between 5 and 10
    between 2017/12/1 and 2018/1/1
    ```

    + 提取 keyword，from_amount，to_amount, has_nagation, nagation_phrase
    + 之后和上面的是一样的

  + Distribution：

    ```
    Distribution of salaries
    ```

    + 同样

    

总的来说，Task 提取的工作，主要在于得到依赖树之后，根据IF ELSE 设定一定的规则，由于这里没有数据筛选的方式，所以需要判断值的大小，所以数据区域设定的比较复杂。

​    

