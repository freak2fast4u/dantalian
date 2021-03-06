# Copyright (C) 2015  Allen Li
#
# This file is part of Dantalian.
#
# Dantalian is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Dantalian is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Dantalian.  If not, see <http://www.gnu.org/licenses/>.

"""
This module contains unit tests for dantalian.library
"""

import os
import posixpath

from dantalian import library

from . import testlib

# pylint: disable=missing-docstring


class TestLibraryRoot(testlib.FSMixin):

    def setUp(self):
        super().setUp()
        os.makedirs('A/.dantalian')
        os.mknod('A/.dantalian/foo')
        os.makedirs('A/foo/bar')
        os.makedirs('B/foo/bar')

    def test_is_library(self):
        self.assertTrue(library.is_library('A'))
        self.assertFalse(library.is_library('B'))

    def test_find_library(self):
        self.assertEqual(library.find_library('A/foo/bar'),
                         posixpath.abspath('A'))

    def test_init_library(self):
        library.init_library('B')
        self.assertTrue(library.is_library('B'))

    def test_get_resource(self):
        self.assertEqual(library.get_resource('A', 'foo'), 'A/.dantalian/foo')
