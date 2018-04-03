from django.test import TestCase
from catalog.models import Author, Language, Genre, Book


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')


class LanguageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Language.objects.create()

    def test_name_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_name_help_text(self):
        language = Language.objects.get(id=1)
        help_text = language._meta.get_field('name').help_text
        self.assertEqual(help_text, "Enter a the book's natural language")

    def test_name_default(self):
        language = Language.objects.get(id=1)
        default = language._meta.get_field('name').default
        self.assertEqual(default, 'English')

    def test_object_name_is_name(self):
        language = Language.objects.get(id=1)
        expected_name = f'{language.name}'
        self.assertEqual(expected_name, str(language))


class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create()

    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_name_help_text(self):
        genre = Genre.objects.get(id=1)
        help_text = genre._meta.get_field('name').help_text
        self.assertEqual(help_text, "Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def test_object_name_is_name(self):
        genre = Genre.objects.get(id=1)
        expected_name = f'{genre.name}'
        self.assertEqual(expected_name, str(genre))


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create()

    def test_title_label(self):
        book = Book.objects.get(id=1)
        title_label = book._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

    def test_title_max_length(self):
        pass
