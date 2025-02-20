from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        """
        Test that a regular user can be created with the proper fields
        and that the password is hashed.
        """
        user = User.objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="securepassword"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertTrue(user.check_password("securepassword"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_user_str_representation(self):
        """
        Test the string representation of the user.
        Adjust this test if your __str__ method returns something different.
        """
        user = User.objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="securepassword"
        )
        self.assertEqual(str(user), "testuser")

    def test_create_superuser(self):
        """
        Test that a superuser can be created and has is_staff and is_superuser True.
        """
        admin = User.objects.create_superuser(
            username="admin",
            email="admin@gmail.com",
            password="adminpassword"
        )
        self.assertEqual(admin.username, "admin")
        self.assertEqual(admin.email, "admin@gmail.com")
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
