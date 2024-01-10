#!/usr/bin/env python
# coding: utf-8

# In[6]:


def checkout_books(librarian_name, book_title_1, book_title_2, duration_time, special_conditions, **details):
    print("checkout processed by: " + librarian_name)
    print("books checkout: ")
    print("-" + book_title_1)
    print("-" + book_title_2)
    print("checkout duration: " + duration_time)
    print("additional checkout details: ")
    for detail, value in details.items():
        print("-" + detail.replace('-', '').title() + ": " + str(value))
    print("special conditions for checkout: ")
    print("-" + special_conditions)


# In[7]:


checkout_books('julie', 'love is unpredictable', 'after', '2 weeks', 'please be careful with the book', late_fee='$0.50', renewals_allowed = '3')


# In[ ]:




