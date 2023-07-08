#!/usr/bin/python3
"""
Unittest for the console
"""
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """ Tests for the console """

    def setUp(self) -> None:
        self.cmd = HBNBCommand()

    def test_quit(self):
        """ test quit function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.assertTrue(self.cmd.onecmd("quit"))

    def test_create(self):
        """ test create function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("create")
            self.assertAlmostEqual(
                "** class name missing **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("create MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())

    def test_show(self):
        """ test show function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show")
            self.assertAlmostEqual(
                "** class name missing **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show BaseModel")
            self.assertAlmostEqual(
                "** instance id missing **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show BaseModel 1234")
            self.assertAlmostEqual(
                "** no instance found **\n", screen.getvalue())

    def test_destroy(self):
        """ test destroy function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("destroy")
            self.assertAlmostEqual(
                "** class name missing **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("destroy MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("destroy BaseModel")
            self.assertAlmostEqual(
                "** instance id missing **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("destroy BaseModel 1234")
            self.assertAlmostEqual(
                "** no instance found **\n", screen.getvalue())

    def test_all(self):
        """ test all function"""
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("all")
            self.assertAlmostEqual(
                "[]\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("all BaseModel")
            self.assertAlmostEqual(
                "[]\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())

    def test_update(self):
        """ test update function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("update")
            self.assertAlmostEqual(
                "** class name missing **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("update MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("update BaseModel")
            self.assertAlmostEqual(
                "** instance id missing **\n", screen.getvalue())
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("update BaseModel 1234")
            self.assertAlmostEqual(
                "** no instance found **\n", screen.getvalue())


if __name__ == "__main__":
    unittest.main()
