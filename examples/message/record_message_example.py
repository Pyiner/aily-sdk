from aily.message.field import NumberField, BooleanField, DateField, OptionsField, StringField
from aily.message.record import Record


class PersonRecord(Record):
    name = StringField(display_name='姓名')
    age = NumberField(display_name='年龄')
    isAlive = BooleanField(display_name='是否存活')
    birthday = DateField(display_name='出生日期', date_format='YYYY/MM/DD')
    mainRaces = OptionsField(display_name='主要胜出赛事')
    prizes = NumberField(display_name='奖金')


# Example usage
if __name__ == "__main__":
    person = PersonRecord(
        name='东海帝皇',
        age=25,
        isAlive=False,
        birthday=577465200000,  # Unix timestamp in milliseconds
        mainRaces=['皋月赏', '东京优骏', '日本杯', '有马纪念', '产经大阪杯'],
        prizes=625633500
    )

    # Printing the instance using to_string() method
    print(person.to_message())
