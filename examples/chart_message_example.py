from aily_sdk.message.chart import LineChart, BarChart, CommonChart, PieChart

bar_chart_data = [
    {"x": 1, "y": 2, "type": "飞书"},
    {"x": 2, "y": 3, "type": "Lark"},
    {"x": 3, "y": 3, "type": "Lark"},
    {"x": 4, "y": 5, "type": "飞书"},
    {"x": 5, "y": 10, "type": "飞书"},
]
line_chart_data = [
    {"x": 1, "y": 5},
    {"x": 2, "y": 5},
    {"x": 3, "y": 2},
    {"x": 4, "y": 2},
    {"x": 5, "y": 3},
]

pie_chart_data = [
    {"x": 1, "y": 2, "type": "飞书"},
    {"x": 2, "y": 3, "type": "Lark"},
    {"x": 3, "y": 3, "type": "Lark"},
]
# 创建 BarChartSpec 和 LineChartSpec 实例
bar_chart = BarChart(data=bar_chart_data, x_field=['x', 'type'], y_field='y', series_field='type')
line_chart = LineChart(data=line_chart_data, x_field='x', y_field='y')
pie_chart = PieChart(data=pie_chart_data, value_field=['x', 'y'], category_field='type')
# 创建 CommonChartSpec 实例
common_chart = CommonChart(charts=[bar_chart, line_chart])

# 打印出配置
print(common_chart.to_message())
print(bar_chart.to_message())
print(pie_chart.to_message())
