from aily.message.field import NumberField, BooleanField, DateField, OptionsField, StringField
from aily.message.table import Table


class TableDemo(Table):
    name = StringField(display_name='姓名')
    age = NumberField(display_name='年龄')
    isAlive = BooleanField(display_name='是否存活')
    birthday = DateField(display_name='出生日期')
    mainRaces = OptionsField(display_name='主要胜出赛事', options=[
        {
            'label': '选项1',
            'value': 'opt1',
        },
        {
            'label': '选项2',
            'value': 'opt2',
        },
        {
            'label': '选项3',
            'value': 'opt3',
        },
    ])
    prizes = NumberField(display_name='奖金')


# Example usage
if __name__ == "__main__":
    td = TableDemo([{
        'name': '东海帝皇',
        'age': 25,
        'isAlive': False,
        'birthday': 577465200000,
        'mainRaces': ['opt2'],
        'prizes': 625633500,
    }, {
        'name': '东海帝皇',
        'age': 25,
        'isAlive': False,
        'birthday': 577465200000,
        'mainRaces': ['opt2'],
        'prizes': 625633500,
    }])
    print(td.to_message())
