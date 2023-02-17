## Low-level Vis Analytic Tasks

### 1. 表征分布 Characterize Distribution

在数据集中的定量属性中，描述属性值的分布（主要关注数值及其出现的频率）

Given a dataset and a quantitative attribute, characterize the distribution of the attributes' value

+ Vis Type/ Recommendation：直方图 Bar Chart，箱型图 Box Plot

+ Vega-Lite Chart：

  + [Simple Bar Chart](https://vega.github.io/vega-lite/examples/bar.html) & [Grouped Bar Chart](https://vega.github.io/vega-lite/examples/bar_grouped.html)：

    ![1](.asset\1.png)

  + [Grouped Bar Chart (Multiple Measure with Repeat)](https://vega.github.io/vega-lite/examples/bar_grouped_repeated.html)

    

    ![2](.asset\2.png)

  + 较少数据的分布 也可以用 [1D Strip Plot](https://vega.github.io/vega-lite/examples/tick_dot.html) 或者 凸显数据的Outlier 使用[Tukey Box Plot (1.5 IQR)](https://vega.github.io/vega-lite/examples/boxplot_2D_vertical.html)

    ![5](.asset\5.png)

    ![11](.asset\11.png)

  + 或者直方图  <font color="red">表示起来可能比较复杂</font>[Histogram](https://vega.github.io/vega-lite/examples/histogram.html)

    ![6](.asset\6.png)
    
  + 单个值的描述 使用Heatmap：正好是二维的

    ![24](.asset\24.png)

+ Design Space

  Bar Chart 的设计空间：

  + 图表的长度依据 顶部的表头种类
  + 数值的编码可以在 宽度方向上 进行压缩

  实际上不需要拘泥于设计空间，可以作为Bar Chart 的填充，设计空间是图表的长度

### 2. Correlation 相关性

在数据集中两个属性中，确定属性值的有用关系。

Given a dataset and two attributes, determine useful relationships between the attributes of datasets.

+ Vis Type/ Recommendation：散点图 Scatterplot，折线图 Line chart

+ Vega-Lite Chart

  + [Scatterplot](https://vega.github.io/vega-lite/examples/point_2d.html) & [Connected Scatterplot (Lines with Custom Paths)](https://vega.github.io/vega-lite/examples/connected_scatterplot.html)

    ![4](.asset\4.png)

    ![8](.asset\8.png)

  + [Strip Plot ](https://vega.github.io/vega-lite/examples/tick_strip.html)

    ![7](.asset\7.png)

  + [Bubble Plot](https://vega.github.io/vega-lite/examples/point_bubble.html) 存在第三个变量的时候

    ![9](.asset\9.png)

  + [Line Chart](https://vega.github.io/vega-lite/examples/line.html) / [Line Chart with Point Markers](https://vega.github.io/vega-lite/examples/line_overlay.html)

    ![10](.asset\10.png)

+ Design Space

  + 需要一些比较方正的设计空间，长宽比例要适当，尤其是图形的高度，往往需要体现其中的相关性的信息，不然会过于密集

    图形宽度仍然需要根据表头个数来确定。

### 3. Sort and Ranking 排序

给定一个数据集，根据一些序数度量对其进行排序 

Given a dataset, rank them according to some ordinal metric

**可能需要对表头进行重新排序**

+ Vis Type/ Recommendation：折线图 Line chart / 条形图 Bar Chart

重点在于对表头的重新排序

### 4. Deviation 离差 

给定一个数据集和一个数据属性，判断值相对于一个参考值的变化 

Given a dataset and a quantitative attribute, the change of judgment value relative to a reference value

+ Vis Type: Diverging Bar Chart / Bi-Direction Bar Chart with a line

+ Vega-Lite Chart：

  + [Bar Chart with Negative Values and a Zero-Baseline](https://vega.github.io/vega-lite/examples/bar_negative.html) 相对于0值的参考变化

    ![12](.asset\12.png)

  + [Horizontal Bar Chart with Negative Values and Labels](https://vega.github.io/vega-lite/examples/bar_negative_horizontal_label.html)

    ![13](.asset\13.png)

  + [Interactive Average](https://vega.github.io/vega-lite/examples/selection_layer_bar_month.html)

    ![14](.asset\14.png)

  + [Mean overlay over precipitation chart](https://vega.github.io/vega-lite/examples/layer_precipitation_mean.html)

    ![15](.asset\15.png)

+ Design Space：

> Bar Chart 的设计空间：
>
>- 图表的长度依据 顶部的表头种类
>- 数值的编码可以在 宽度方向上 进行压缩
>
>实际上不需要拘泥于设计空间，可以作为Bar Chart 的填充，设计空间是图表的长度

### 5. Compare 对比

给定一个数据集，对比一些数据的差异

+ Vis Type/Recommendation ：表征单个数据的，Dot plot 、Bar Chart  

+ Vega-Lite Chart:

  + Dot Plot：
  + Bar Chart
  + 如果是一块数据区域的对比：Heatmap

+ Design Space：

  Dot Plot 需要大小相同，分割一致的背景板。

### 6. Find Anomalies 查找异常值

识别给定关系或期望的给定数据案例集合中的异常 

Identify any anomalies within a given set of data cases with respect to a given relationship or expectation

+ Vis Type/Recommendation :  箱型图 Box plot / 1D Strip Plot

+ Vega-Lite Chart: 

  + [Tukey Box Plot (1.5 IQR)](https://vega.github.io/vega-lite/examples/boxplot_2D_vertical.html)
  + 1D Strip Plot

+ Design Space:

  1D Strip Plot & Box Plot

### 7. Compute Derived Value 派生值任务

给定一个数据集，计算数据的聚合表示，比如Sum, Average, Max, Min, Mean 等

Given a dataset, compute an aggregate numeric representation of the data.

对于不同的数据聚合类型，应该采用不同的可视化图表类型来表示。

Max/Min：建议使用Bar Chart

Sum : 建议使用 Pie Chart

  + [Interactive Average](https://vega.github.io/vega-lite/examples/selection_layer_bar_month.html)

    ![14](.asset\14.png)

  + [Mean overlay over precipitation chart](https://vega.github.io/vega-lite/examples/layer_precipitation_mean.html)

    ![15](.asset\15.png)
    
+ 还有一个有可能的有用的[Top-K Plot with “Others”](https://vega.github.io/vega-lite/examples/window_top_k_others.html)

  ![16](.asset\16.png)

**Design Space：**

所有的Bar Chart 都 不受设计空间大小的约束

但是 Pie Chart 需要方形的，纵横比合适的设计空间

### -. Cluster 聚类 这类任务删除

### 8. Magnitude 规模:

  用来比较数据的规模，有可能是比较相对规模（显示哪一个比较大），有可能是（显示精确的差异）

Vis Type/Recommendation :  条形图 雷达图 饼形图 比例堆叠条形图

Vega-Lite Chart: 

+ Simple Bar Chart
+ 雷达图 Vega-Lite好像不支持
+ 相对规模也可以采用Dot plot
+ 平行坐标图 Parallel Coordinates：[Parallel Coordinate Plot](https://vega.github.io/vega-lite/examples/parallel_coordinate.html)

![17](.asset\17.png)

+ [Mosaic Chart with Labels](https://vega.github.io/vega-lite/examples/rect_mosaic_labelled_with_offset.html)

![18](.asset\18.png)

+ Design Space：
  + 后两者都需要较大的设计空间，并且需要合适的纵横比
  + Dot Plot 的设计空间不限
  + 雷达图 没有Vega-Lite的支持，但是也需要方形的设计空间

### 9. Part-to-whole 表征部分和整体的关系

能显示出一个整体如何被拆解成不同组成。（如果读者只是想了解个别组成部分的大小，不妨改用规模类的图表）

+ Vis Type / Recommendation : Stacked Column 堆叠条形图， 或者Pie Chart / Donut， Radio Chart

+ Vega-Lite Chart:

  + [Pie Chart](https://vega.github.io/vega-lite/examples/arc_pie.html) : 

    ![19](.asset\19.png)

  + [Stacked Bar Chart](https://vega.github.io/vega-lite/examples/stacked_bar_weather.html)

    ![20](.asset\20.png)

  + [Mosaic Chart with Labels](https://vega.github.io/vega-lite/examples/rect_mosaic_labelled_with_offset.html)

+ Design Space

  + 都需要纵横比合适的设计空间
  + Stacked Bar Chart 如果 Stacked 量比较多，可能也需要较长的空间。

### 10. Trend

强调趋势的变化。有可能是短期的波动，或较长时间空间内的改变。

  + [Line Chart](https://vega.github.io/vega-lite/examples/line.html) / [Line Chart with Point Markers](https://vega.github.io/vega-lite/examples/line_overlay.html)

    ![10](.asset\10.png)

+ [Horizon Graph](https://vega.github.io/vega-lite/examples/area_horizon.html)

  ![21](.asset\21.png)

+ Design Space:
  + Line Chart : 不能太扁，需要纵横比合适
  + Horizon Graph ： 可以较Line Chart 更扁一些

### 11. Range 求一个数据集的范围

+ Vega-Lite Chart:

  + [Ranged Dot Plot](https://vega.github.io/vega-lite/examples/layer_ranged_dot.html)

    ![22](.asset\22.png)

  + [Box Plot with Min/Max Whiskers](https://vega.github.io/vega-lite/examples/boxplot_minmax_2D_vertical.html)

    ![23](.asset\23.png)

+ Design Space:
  
  + Ranged Dot 和 Box Plot 都需要一定长宽比的图，Ranged Dot 需要长>宽，Box Plot需要宽>长。