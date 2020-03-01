from django.db import models
"""упрощенная можель, в которой я не буду работать со временкм
а только создам связь один ко многим класса ответ с классом вопрос
задача этого упражнения подготовить приложение в более простом виде
и потренировать с формированием шаблонов даженго на более простом примере
поэкспериментировать с формами и теми запросами,которые от меня треюуются
в оффициальной документациии"""

class Question(models.Model):
    question_text = models.TextField(max_length=300)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.TextField(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text