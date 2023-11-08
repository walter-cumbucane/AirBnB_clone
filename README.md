Markdown
## Description of the project

This project involves simulating an Airbnb application by creating a control system for the modules used on our web page. We achieve this by implementing a JSON-format database and leveraging object-oriented programming, Python data translation, and command interpretation. The result is a local database that can be easily modified using specific commands, providing a flexible and efficient way to manage data.

## Prerequisites

Python3.4+ has to be installed if you desire to use the console:

```bash
sudo apt-get install python3
Installation
To have access to the console use the following command:

Bash
git clone https://github.com/walter-cumbucane/AirBnB_clone.git; cd AirBnB_clone

Run
If you want to execute the console use:

Bash
python3 console.py
or

Bash
./console.py


## Testing

If you want to personalize the classes and execute unit tests to confirm that your changes haven't modified the functionality use:

bash
python3 -m unittest discover tests


## Use

### Available commands

| Command | Explanation |
|---|---|
| `create` | Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel` |
| `show` | Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234` |
| `all` | Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseMode` |
| `update` | Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"` |

### Normal command input

| Command | Example |
|---|---|
| `create` | `create [class name]` |
| `show` | `show [class name] [id]` |
| `all` | `all [class name]` |
| `update` | `update [class name] [id] [arg_name] [arg_value]` |

### Alternative command input

| Command | Example |
|---|---|
| `[class name].all()` | `User.all()` |
| `[class name].count()` | `User.count()` |
| `[class name].show()` | `User.show()` |
| `[class name].destroy()` | `User.destroy()` |
| `[class name].update([id], [attribute name], [attribute value])` | `User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")` |
| `[class name].update([id], [dictionary representation])` | `User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})` |

### Available classes

| Class name | Attributes |
|---|---|
| `BaseModel` | `id`, `created_at`, `updated_at` |
| `User` | `email`, `password`, `first_name`, `last_name` |
| `State` | `name`, `state_id` |
| `City` | `name` |
| `Amenity` | `name` |
| `Place` | `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, `amenity_ids` |
| `Review` | `place_id`, `user_id`, `text` |

Every model inherits attributes from `BaseModel`.

## How to start it

### Interactive Mode

bash
./console.py
Now you are on interactive mode and you will see the prompt (hbnb) input a command:

(hbnb) create User
The id of the created model will be visible in the standard output, if you do:

(hbnb) show User [id]
Sources
Coded with ❤️ and 🔨 by: [Akuak Akuak](https://github.com/Akuak-Mayen) & [Walter Cumbucane](https://github.com/
walter-cumbucane
