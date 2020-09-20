from django.test import TestCase


class TestViews(TestCase):
    def test_index_template_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index/index.html")