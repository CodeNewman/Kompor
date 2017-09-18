-- 建库 中国区
CREATE KEYSPACE cn_kavoutdata WITH replication = {'class': 'NetworkTopologyStrategy', 'dc1': '1', 'dc2': '1'}  AND durable_writes = true;


-- stock ratio value  股票指数信息
create table if not exists stock_ratio_from_10jqka(
	symbol               text    , -- 代码
	name                 text    , -- 名称
	date                 date    , -- 日期
	price                text    , -- 现价
	size_ratio           text    , -- 涨跌幅(%)
	rise_fall            text    , -- 涨跌
	pace_ratio           text    , -- 涨速(%)
	changed_hands_ratio  text    , -- 换手(%)
	than                 text    , -- 量比
	amplitude_ratio      text    , -- 振幅(%)
	turnover             text    , -- 成交额
	shares_outstanding   text    , -- 流通股
	current_market       text    , -- 流通市值
	pe_ratio             text    , -- 市盈率

	PRIMARY KEY(symbol, date)
) WITH CLUSTERING ORDER BY(date DESC);


-- stock detial value  股票基本信息
create table if not exists stock_basic_from_10jqka(
	symbol               text    , -- 代码
	name                 text    , -- 名称
	rt                   text    , -- 交易时间
	total                text    , -- 总交易日数量
	start                date    , -- 上市日期
	year                 text    , -- 每年度交易日数量

	PRIMARY KEY(symbol, name)
) WITH CLUSTERING ORDER BY(name ASC);

