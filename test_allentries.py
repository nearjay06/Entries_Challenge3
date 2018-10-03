import json
import unittest

from .all_entries import app

class FlaskTest(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()


  def test_all_entries_to_return_list_of_entries(self):
        response = self.app.get('/api/v1/entries/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')

  def test_all_entries_to_get_entry_with_specific_id(self):
    response = self.app.get('/api/v1/entries/<id>')
    self.assertEqual(response.status_code,200)


  def test_all_entries_to_add_entry(self):
    response = self.app.post('/api/v1/entries/',
               data=json.dumps( {'id': 3,
                                 'name': 'texting'
                                  }
                              ),
                    content_type='application/json')

    self.assertEqual(response.status_code,201)
    
    content= response.get_json()
    print(content)
    self.assertEqual(content,{'entry': {'id': 3, 'name': 'texting'}})

  def test_all_entries_to_modify_entry(self):
    response = self.app.put('/api/v1/entries/1')
    self.assertEqual(response.status_code,200)

  def test_post_endpoint_errors_that_returns_400(self):
      response = self.app.post ('/api/v1/entries/',
                 data=json.dumps( {'id': 3
                                    }
                              ),
                    content_type='application/json')
                  
      self.assertEqual(response.status_code,400)

if __name__== '__main__':
  pass