from django.test import TestCase, Client
from django.urls import resolve


class Test_Member_Related_API(TestCase):

    client = Client()
    
    # def test_reachable_admin(self):
    #     response = self.client.get('admin/')
    #     self.assertEqual(response.status_code, 200)

    # # task (1) (2) (3)
    # def test_reachable_bookstore(self):
    #     response = self.client.get("bookstore")
    #     self.assertEqual(response.status_code, 200)
    #
    # # task (4)
    # def test_reachable_book(self):
    #     response = self.client.get("book")
    #     self.assertEqual(response.status_code, 200)

        
"""
(1) List all book stores that are open at a certain datetime
(2) List all book stores that are open on a day of the week, at a certain time
(3) List all book stores that are open for more or less than x hours per day or week

(4) List all books that are within a price range, sorted by price or alphabetically
(5) List all book stores that have more or less than x number of books
(6) List all book stores that have more or less than x number of books within a price range
(7) Search for book stores or books by name, ranked by relevance to search term
(8) The top x users by total transaction amount within a date range
(9) The total number and dollar value of transactions that happened within a date range
(10) Edit book store name, book name, book price and user name
(11) The most popular book stores by transaction volume, either by number of transactions or transaction dollar value
(12) Total number of users who made transactions above or below $v within a date range
(13) Process a user purchasing a book from a book store, handling all relevant data changes in an atomic transaction
"""