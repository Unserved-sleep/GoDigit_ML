class UserManager:
    def __init__(self):
        self.users = {
            "customers": [],
            "employees": [],
            "admins": []
        }
    def create_user(self, user_type, name, email, extra_info):
        table_name = f"{user_type}s"
        extra_column = self._get_extra_column(user_type)

        user = {
            "name": name,
            "email": email,
            extra_column: extra_info
        }
        self.users[table_name].append(user)
        print(f"{user_type.capitalize()} {name} created successfully")

    def show_users(self):
        for user_type, user_list in self.users.items():
            print(f"\n{user_type.upper()}:")
            for user in user_list:
                print(user)

    def _get_extra_column(self, user_type):
        return {
            'customer': 'phone',
            'employee': 'department',
            'admin': 'access_level'
        }.get(user_type, 'extra')

user_manager = UserManager()

user_manager.create_user("customer", "John Doe", "john@example.com", "1234567890")
user_manager.create_user("employee", "Jane Smith", "jane@company.com", "HR")
user_manager.create_user("admin", "Admin User", "admin@company.com", "Full")

user_manager.show_users()