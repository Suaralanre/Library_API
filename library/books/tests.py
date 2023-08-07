from django.test import TestCase
from django.urls import reverse
from .models import Book
# Create your tests here.

class Book_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "A nice title",
            subtitle = "A nice subtitle",
            author = "Kimi Raiko",
            isbn = "1234567899876",
        )
    
    def test_book_content(self):
        self.assertEqual(self.book.title, "A nice title")
        self.assertEqual(self.book.subtitle, "A nice subtitle")
        self.assertEqual(self.book.author, "Kimi Raiko")
        self.assertEqual(self.book.isbn, "1234567899876")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1234567899876")
        self.assertTemplateUsed(response, "book_list.html")