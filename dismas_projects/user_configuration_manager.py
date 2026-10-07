#function to add new settings 
def add_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = str(value).lower()
    if key in settings:
        return f"The '{key}'  and '{value}' you want to add already exist. You cannot add a setting that exist in settings."
    settings[key] = value
    return f"New setting '{key}' and '{value}' added successfully."
#Function to update the existing user settings
def update_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = str(value).lower()
    if key in settings:
        settings[key] = value
        return f"The '{key}' and '{value}' updated successfully in settings."
    return f"you cannot update '{key}' and '{value}' that does not exist in settings."
#function to delete an existing setting
def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"The '{key}' deleted successfully from settings"
    return f"You cannot delete '{key}' that is not in settings."
#function to view existing settings
def view_settings(settings):
    if not settings:
        return f"NO settings to view"
    result = f"These are the user settings: \n"
    for key, value in settings.items():
        result += f"{key.capitalize()} : {value}\n"
    return result
test_settings = {'theme': 'dark', 'language': 'english', 'country': 'Kenya'}
if __name__ == "__main__":
    print(add_setting(test_settings, ('theme', 'black')))
    print(add_setting(test_settings, ('color', 'blue')))
    print(update_setting(test_settings, ('sound', 'medium')))
    print(update_setting(test_settings, ('language', 'kiswahile')))
    print(delete_setting(test_settings, 'background'))
    print(delete_setting(test_settings, 'theme'))
    print(add_setting(test_settings, ("sound", 50)))
    print(view_settings(test_settings))
