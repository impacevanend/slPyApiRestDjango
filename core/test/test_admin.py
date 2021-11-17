from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@datadosis.com',
            password = 'password123'
        )
        #Que el usuario administrado siempre haga login
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@datadosis.com',
            password = 'pass123',
            name = 'Test user nombre completo'
        )

    def test_users_listed(self):
        """ Testear que los usuarios han sido enlistados en la página de usuario """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)


    def test_user_change_page(self):
        """ Prueba que la página  editada por el usuario funciona """
        url = reverse('admin:core_user_change', args=[self.user.id])
         #/admin/core/user/id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
    

    def test_create_user_page(self):
        """ Prueba que la página de creación de usuario funciona """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
