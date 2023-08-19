#!user/bin/python3
"""Console test cases"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
import uuid


class ConsolePromptTest(unittest.TestCase):
    """Console class test cases."""
    def test_Console_prompt(self):
        """Check the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_Console_prompt_empty_line(self):
        """Check empty line."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue())

    def test_Console_prompt_new_line(self):
        """Check new line."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("\n"))
            self.assertEqual("", output.getvalue())

    def test_Console_quit(self):
        """Check quit exists."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_Console_eof(self):
        """Check eof exists."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class ConsoleHelpTest(unittest.TestCase):
    """help testing."""
    def test_Console_help(self):
        """Check help exists."""
        _help = ("Documented commands (type help <topic>):\n" +
                 "========================================\n" +
                 "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(_help, output.getvalue().strip())

    def test_Console_help_EOF(self):
        """help eof"""
        text = "EOF command to EOF the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_all(self):
        """help all"""
        text = ("Print string representation of all instances.\n" +
                "\n        If a class name is provided, " +
                "will print only instances of that class." +
                "\n        Usage: all" +
                "\n        or   : all <class_name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_count(self):
        """help all"""
        text = ("Return the number of count.\n" +
                "\n        Usage: <class name>.count()." +
                "\n        Example: User.count().")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_create(self):
        """help create"""
        text = ("Create a new instance of BaseModel, " +
                "saves it (to the JSON file).\n" +
                "\n        Usage: create <class_name>" +
                "\n        Example: create Basemodel")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_destroy(self):
        """help destroy"""
        text = ("Delete an instance based on the class name and id.\n" +
                "\n        Usage: destroy <class_name> <id>" +
                "\n        Example: destroy BaseModel 1234-1234-1234")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_quit(self):
        """help quit"""
        text = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_show(self):
        """help show"""
        text = ("Print the string representation of an instance" +
                " based on the class name.\n" +
                "\n        Usage: show <class_name> <id>" +
                "\n        Example: show BaseModel 1234-1234-1234")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_update(self):
        """help update"""
        text = ("Update an instance based on its class name and id.\n" +
                "\n        Usage: update <class name> <id> <attribute name>" +
                " '<attribute value>'")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(text, output.getvalue().strip())


class ConsoleCreateTest(unittest.TestCase):
    """Create command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Console_create_no_class(self):
        """Test create with no class"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("create")
            expected = "** class name missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_create_no_existing_class(self):
        """Test create with class doesn't exist"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("create Cake")
            expected = "** class doesn't exist **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_create_BaseModel_instance(self):
        """Test create BaseModel"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_User_instance(self):
        """Test create User"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_Amenity_instance(self):
        """Test create Amenity"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_City_instance(self):
        """Test create City"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_Place_instance(self):
        """Test create Place"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_Review_instance(self):
        """Test create Review"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_State_instance(self):
        """Test create State"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_doted_BaseModel(self):
        """Test BaseModel.create()"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.create()")
            err = "*** Unknown command: BaseModel.create()"
            self.assertEqual(err, output.getvalue().strip())

    def test_Console_create_doted_Amenity(self):
        """Test Amenity.create()"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Amenity.create()")
            err = "*** Unknown command: Amenity.create()"
            self.assertEqual(err, output.getvalue().strip())

    def test_Console_create_doted_City(self):
        """Test City.create()"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("City.create()")
            err = "*** Unknown command: City.create()"
            self.assertEqual(err, output.getvalue().strip())

    def test_Console_create_doted_Place(self):
        """Test Place.create()"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Place.create()")
            err = "*** Unknown command: Place.create()"
            self.assertEqual(err, output.getvalue().strip())

    def test_Console_create_doted_Review(self):
        """Test Review.create()"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Review.create()")
            err = "*** Unknown command: Review.create()"
            self.assertEqual(err, output.getvalue().strip())

    def test_Console_create_doted_State(self):
        """Test State.create()"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("State.create()")
            err = "*** Unknown command: State.create()"
            self.assertEqual(err, output.getvalue().strip())

    def test_Console_create_doted_User(self):
        """Test User.create()"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("User.create()")
            err = "*** Unknown command: User.create()"
            self.assertEqual(err, output.getvalue().strip())


class ConsoleShowTest(unittest.TestCase):
    """Test show command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Console_show_no_class(self):
        """Test show no class"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", op.getvalue().strip())

    def test_Console_show_no_existing_class(self):
        """Test show class doesn't exist"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show Cake")
            expected = "** class doesn't exist **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_show_no_id(self):
        """Test show class no id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show BaseModel")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_show_no_existing_id(self):
        """Test show class no existing id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show BaseModel no-id-123")
            expected = "** no instance found **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_show_no_existing_class_doted(self):
        """Test show class doesn't exist"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Cake.show()")
            expected = "** class doesn't exist **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_show_no_id_doted(self):
        """Test class.show() no id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("BaseModel.show()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("User.show()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("City.show()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Amenity.show()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Place.show()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Review.show()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("State.show()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_show_no_existing_id_doted(self):
        """Test class.show() no existing id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("BaseModel.show(no-id-123)")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("User.show(no-id-123)")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Amenity.show(no-id-123)")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("City.show(no-id-123)")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Place.show(no-id-123)")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Review.show(no-id-123)")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("State.show(no-id-123)")
            self.assertEqual("** no instance found **", op.getvalue().strip())

    def test_Console_show_instance(self):
        """Test show class id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(_id)]
            command = "show BaseModel {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(_id)]
            command = "show User {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(_id)]
            command = "show Amenity {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(_id)]
            command = "show City {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(_id)]
            command = "show Place {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(_id)]
            command = "show Review {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(_id)]
            command = "show State {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_Console_show_instance_doted(self):
        """Test class.show(id)"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(_id)]
            command = "BaseModel.show({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(_id)]
            command = "User.show({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(_id)]
            command = "Amenity.show({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(_id)]
            command = "City.show({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(_id)]
            command = "Place.show({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(_id)]
            command = "Review.show({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(_id)]
            command = "State.show({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())


class ConsoleDestroyTest(unittest.TestCase):
    """Test destroy command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Console_destroy_no_class(self):
        """Test destroy no class"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **", op.getvalue().strip())

    def test_Console_destroy_no_existing_class(self):
        """Test destroy class doesn't exist"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("destroy Cake")
            expected = "** class doesn't exist **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_destroy_no_id(self):
        """Test destroy class no id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("destroy BaseModel")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_destroy_no_existing_id(self):
        """Test destroy class no existing id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("destroy BaseModel no-id-123")
            self.assertEqual("** no instance found **", op.getvalue().strip())

    def test_Console_destroy_no_id_doted(self):
        """Test class.destroy() no id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("BaseModel.destroy()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("User.destroy()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Amenity.destroy()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("City.destroy()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Place.destroy()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Review.destroy()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("State.destroy()")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_destroy_no_existing_id_doted(self):
        """Test class.destroy() no existing id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("BaseModel.destroy('no-id-123')")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("User.destroy('no-id-123')")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Amenity.destroy('no-id-123')")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("City.destroy('no-id-123')")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Place.destroy('no-id-123')")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("Review.destroy('no-id-123')")
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("State.destroy('no-id-123')")
            self.assertEqual("** no instance found **", op.getvalue().strip())

    def test_Console_destroy_instance(self):
        """destroy class id"""
        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy BaseModel {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show BaseModel {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy User {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show User {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy Amenity {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show Amenity {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy City {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show City {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy Place {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show Place {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy Review {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show Review {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy State {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show State {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

    def test_Console_destroy_instance_doted(self):
        """ class.destroy(id)"""
        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "BaseModel.destroy({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show BaseModel {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "User.destroy({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show User {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "Amenity.destroy({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show Amenity {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "City.destroy({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show City {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "Place.destroy({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show Place {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "Review.destroy({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show Review {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "State.destroy({})".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show State {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())


class ConsoleAllTest(unittest.TestCase):
    """Test all command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Console_all_non_existing_calss(self):
        """Test all with a non existing class"""
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("all Cake"))
            expected = "** class doesn't exist **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_all_with_calss(self):
        """Test all with a class"""
        bm_id = ""
        usr_id = ""
        expected = ""
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            bm_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            usr_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel " + bm_id))
            expected = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn(expected, op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            bm_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            usr_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("show Amenity " + bm_id))
            expected = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn(expected, op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            bm_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            usr_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("show City " + bm_id))
            expected = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn(expected, op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            bm_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            usr_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("show Place " + bm_id))
            expected = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn(expected, op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            bm_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            usr_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("show Review " + bm_id))
            expected = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn(expected, op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            bm_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            usr_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("show State " + bm_id))
            expected = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn(expected, op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            bm_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            usr_id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("show User " + bm_id))
            expected = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn(expected, op.getvalue().strip())


class ConsoleUpdateTest(unittest.TestCase):
    """Test cases for update command"""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Console_update_no_class(self):
        """update without args"""
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual("** class name missing **", op.getvalue().strip())

    def test_Console_update_non_existing_class(self):
        """update non existing class"""
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update Cake"))
            expected = "** class doesn't exist **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_update_no_id(self):
        """update without id"""
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_update_no_id_doted(self):
        """update without id"""
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("City.update()"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("Place.update()"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("Review.update()"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("State.update()"))
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_update_wrong_id(self):
        """update wrong id"""
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1234"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update User 1234"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1234"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update City 1234"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update Place 1234"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update Review 1234"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("update State 1234"))
            self.assertEqual("** no instance found **", op.getvalue().strip())

    def test_Console_update_wrong_id_doted(self):
        """update wrong id"""
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update(1234)"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("User.update(1234)"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update(1234)"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("City.update(1234)"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("Place.update(1234)"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("Review.update(1234)"))
            self.assertEqual("** no instance found **", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            self.assertFalse(HBNBCommand().onecmd("State.update(1234)"))
            self.assertEqual("** no instance found **", op.getvalue().strip())

    def test_Console_update_attribute_missing(self):
        """update a missing attribute"""
        expected = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = output.getvalue().strip()
            testCmd = "update BaseModel {}".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = output.getvalue().strip()
            testCmd = "update User {}".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = output.getvalue().strip()
            testCmd = "update Amenity {}".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = output.getvalue().strip()
            testCmd = "update City {}".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
            testCmd = "update Place {}".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = output.getvalue().strip()
            testCmd = "update Review {}".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = output.getvalue().strip()
            testCmd = "update State {}".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

    def test_Console_update_attribute_missing_doted(self):
        """update a missing attribute"""
        expected = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = output.getvalue().strip()
            testCmd = "BaseModel.update({})".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = output.getvalue().strip()
            testCmd = "User.update({})".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = output.getvalue().strip()
            testCmd = "Amenity.update({})".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = output.getvalue().strip()
            testCmd = "City.update({})".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
            testCmd = "Place.update({})".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = output.getvalue().strip()
            testCmd = "Review.update({})".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = output.getvalue().strip()
            testCmd = "State.update({})".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

    def test_Console_update_value_missing(self):
        """update a missing value"""
        expected = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = output.getvalue().strip()
            testCmd = "update BaseModel {} created_at".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = output.getvalue().strip()
            testCmd = "update User {} created_at".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = output.getvalue().strip()
            testCmd = "update Amenity {} created_at".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = output.getvalue().strip()
            testCmd = "update City {} created_at".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
            testCmd = "update Place {} created_at".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = output.getvalue().strip()
            testCmd = "update Review {} created_at".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = output.getvalue().strip()
            testCmd = "update State {} created_at".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

    def test_Console_update_value_missing_doted(self):
        """update a missing value"""
        expected = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = output.getvalue().strip()
            testCmd = "BaseModel.update({}, 'created_at')".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = output.getvalue().strip()
            testCmd = "User.update({}, 'created_at')".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = output.getvalue().strip()
            testCmd = "Amenity.update({}, 'created_at')".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = output.getvalue().strip()
            testCmd = "City.update({}, 'created_at')".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
            testCmd = "Place.update({}, 'created_at')".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = output.getvalue().strip()
            testCmd = "Review.update({}, 'created_at')".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = output.getvalue().strip()
            testCmd = "State.update({}, 'created_at')".format(_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(expected, output.getvalue().strip())

    def test_Console_update_basemodel(self):
        """update a basemodel instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update BaseModel {} name Opla'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["BaseModel.{}".format(_id)].__dict__
            self.assertEqual("Opla", _dict["name"])

    def test_Console_update_basemodel_doted(self):
        """update a basemodel instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'BaseModel.update({}, name, Nicole)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["BaseModel.{}".format(_id)].__dict__
            self.assertEqual("Nicole", _dict["name"])

    def test_Console_update_user(self):
        """update a user instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update User {} first_name upla'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["User.{}".format(_id)].__dict__
            self.assertEqual("upla", _dict["first_name"])

    def test_Console_update_user_doted(self):
        """update a user instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'User.update({}, first_name, Nicola)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["User.{}".format(_id)].__dict__
            self.assertEqual("Nicola", _dict["first_name"])

    def test_Console_update_amenity(self):
        """update a amenity instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update Amenity {} name Moon'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Amenity.{}".format(_id)].__dict__
            self.assertEqual("Moon", _dict["name"])

    def test_Console_update_amenity_doted(self):
        """update a amenity instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'Amenity.update({}, name, camp)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Amenity.{}".format(_id)].__dict__
            self.assertEqual("camp", _dict["name"])

    def test_Console_update_city(self):
        """update a city instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update City {} state_id OHIO'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["City.{}".format(_id)].__dict__
            self.assertEqual("OHIO", _dict["state_id"])

    def test_Console_update_city_doted(self):
        """update a city instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'City.update({}, state_id, OHIO)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            res = output.getvalue().strip()
            _dict = storage.all()["City.{}".format(_id)].__dict__
            self.assertEqual("OHIO", _dict["state_id"])

    def test_Console_update_place_str(self):
        """update a place instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update Place {} name Tokyo'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual("Tokyo", _dict["name"])

    def test_Console_update_place_str_doted(self):
        """update a place instance's str"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'Place.update({}, state_id, Casablanca)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual("Casablanca", _dict["state_id"])

    def test_Console_update_place_int_guests(self):
        """update a place instance int"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update Place {} max_guest 3'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(3, _dict["max_guest"])

    def test_Console_update_place_int_guests_doted(self):
        """update a place instance's str"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'Place.update({}, max_guest, 2)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(2, _dict["max_guest"])

    def test_Console_update_place_int_rooms(self):
        """update a place instance int"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update Place {} number_rooms 3'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(3, _dict["number_rooms"])

    def test_Console_update_place_int_rooms_doted(self):
        """update a place instance's str"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'Place.update({}, number_rooms, 2)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(2, _dict["number_rooms"])

    def test_Console_update_place_int_bathrooms(self):
        """update a place instance int"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update Place {} number_bathrooms 3'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(3, _dict["number_bathrooms"])

    def test_Console_update_place_int_bathrooms_doted(self):
        """update a place instance's str"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'Place.update({}, number_bathrooms, 2)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(2, _dict["number_bathrooms"])

    def test_Console_update_place_int(self):
        """update a place instance int"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update Place {} price_by_night 30'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(30, _dict["price_by_night"])

    def test_Console_update_place_int_doted(self):
        """update a place instance's str"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'Place.update({}, price_by_night, 20)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(20, _dict["price_by_night"])

    def test_Console_update_place_float_latitude(self):
        """update a place instance float"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update Place {} latitude 10.55'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(10.55, _dict["latitude"])

    def test_Console_update_place_float_latitude_doted(self):
        """update a place instance's float"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'Place.update({}, latitude, 10.66)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(10.66, _dict["latitude"])

    def test_Console_update_place_float_longitude(self):
        """update a place instance float"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update Place {} longitude 10.55'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(10.55, _dict["longitude"])

    def test_Console_update_place_float_longitude_doted(self):
        """update a place instance's float"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'Place.update({}, longitude, 10.66)'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual(10.66, _dict["longitude"])

    def test_Console_update_place_list_amenity_ids(self):
        """update a place instance list"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'update Place {} amenity_ids ""'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual([], _dict["amenity_ids"])

    def test_Console_update_place_float_amenity_ids_doted(self):
        """update a place instance's float."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'Place.update({}, amenity_ids, "")'.format(_id)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            _dict = storage.all()["Place.{}".format(_id)].__dict__
            self.assertEqual([], _dict["amenity_ids"])


class ConsoleCountTest(unittest.TestCase):
    """Test cases for count command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_Console_count_invalid_class(self):
        """Test with an invalid class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Unknown.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_Console_count_valid_classes(self):
        """Count valid classes."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual('2', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual('3', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual('3', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual('4', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual('4', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual('1', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual('3', output.getvalue().strip())
