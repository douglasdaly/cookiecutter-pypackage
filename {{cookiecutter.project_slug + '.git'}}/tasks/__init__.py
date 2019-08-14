# -*- coding: utf-8 -*-
"""
Invoke commands for common tasks.
"""
import dotenv
import invoke

from . import docs
from . import generate
from . import release

dotenv.load_dotenv()

namespace = invoke.Collection(docs, generate, release)
