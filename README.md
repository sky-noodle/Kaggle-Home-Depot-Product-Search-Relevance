# Kaggle-Home-Depot-Product-Search-Relevance
As an NLP practice
项目描述：
这是Home Depot在Kaggle平台发起的竞赛。
Home Depot是家装产品销售商，提供了用户只需搜索物品描述，即可找到所需产品的服务。
在本次竞赛中，Home Depot提供用户对商品的描述以及对匹配程度的评分，要求开发一个可以准确预测用户所需产品的模型，
提交对训练集的商品描述的匹配程度评分。

1.特征工程：
主要进行了
#1.文本预处理
对原始文本信息进行三点预处理

（1）将单词小写并分为tokens

（2）去除停止词和数字

（3）使用SnowballStemmer提取词干

#2.提取特征
提取三项特征

（1）文本距离

（2）基于TF-IDF算法计算文本余弦相似度

（3）基于Word2Ver计算向量的余弦相似度

2.建立模型
选用3种模型
（1）RandomForestRegressor

（2）XGBRegressor

（3）Ridge

3.模型融合
采用stacking方式进行模型融合

