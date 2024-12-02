# Release Notes

## Version 0.1.0

### New Features

- **User Registration:** Implemented automatic user registration based on OIDC tokens.
- **Role Assignment:** Added functionality to assign roles to users based on their OIDC groups.
- **Admin Status:** Introduced the ability to update user admin status in specific projects if they belong to the designated admin group.
- **Customizable:** Made the plugin easily configurable to work with different OIDC providers and group structures.

### Improvements

- **Code Refactoring:** Improved code readability and maintainability by refactoring repetitive code into separate functions.
- **Logging:** Enhanced logging to provide better insights into user registration and role assignment processes.

### Bug Fixes

- **Role Assignment:** Fixed an issue where users were not being assigned roles correctly based on their OIDC groups.
- **Admin Status:** Resolved a bug where the admin status was not being updated correctly for existing users.

### Known Issues

- **Performance:** The plugin may experience performance issues with a large number of users and groups. This will be addressed in future releases.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
