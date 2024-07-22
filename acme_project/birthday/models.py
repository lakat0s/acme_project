from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Импортируется функция-валидатор.
from .validators import real_age

User = get_user_model()

class Tag(models.Model):
    tag = models.CharField('Тег', max_length=20)


    # Переопределяем метод:
    def __str__(self):
        return self.tag



class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
     )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте Ctrl для выбора нескольких вариантов'
    )


    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})


class Congratulation(models.Model):
    text = models.TextField('Текст поздравления')
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)

#class BirthdayListView(ListView):
    #model = Birthday
    # По умолчанию этот класс
    # выполняет запрос queryset = Birthday.objects.all(),
    # но мы его переопределим:
    #queryset = Birthday.objects.prefetch_related('tags')
    #ordering = 'id'
    #paginate_by = 10

#class BirthdayListView(ListView):
    #model = Birthday
    #queryset = Birthday.objects.prefetch_related(
    #    'tags'
    #).select_related('author')
    #ordering = 'id'
    #paginate_by = 10