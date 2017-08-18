# Kaggle-Home-Depot-Product-Search-Relevance
As an NLP practice
项目描述：
这是Home Depot在Kaggle平台发起的竞赛。
Home Depot是家装产品销售商，提供了用户只需搜索物品描述，即可找到所需产品的服务。
在本次竞赛中，Home Depot要求开发一个可以准确预测用户所需产品的模型，用于提高用户体验。

特征工程：
详见feature_engineering.ipynb
主要进行了
#1.文本预处理
对原始文本信息进行三点预处理

（1）将单词小写并分为tokens

（2）去除停止词和数字

（3）使用SnowballStemmer对文本进行归一化处理

#2.提取特征
提取三项特征

（1）基于文本距离

（2）基于TF-IDF的文本相似度余弦

（3）基于Word2Ver的向量相似度余弦

