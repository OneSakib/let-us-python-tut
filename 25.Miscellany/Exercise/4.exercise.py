def require_role(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') == role:
                return func(user, *args, **kwargs)
            else:
                print("Access Denied")
        return wrapper
    return decorator


@require_role(role="admin")
def delete_user(user, user_id):
    print(f"User {user_id} delete by {user['name']}")


admin_user = {"name": "Sakib", "role": "admin"}
guest_user = {"name": "John", "role": "guest"}
delete_user(admin_user, 123)
delete_user(guest_user, 456)
