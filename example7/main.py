
import logging

import com.bar
import com.foo.tar


print("without basicConfig")
com.bar.run()
com.foo.run()
com.foo.tar.run()
print("\n\n")
print("with basicConfig(level=logging.DEBUG)")
logging.basicConfig(level=logging.DEBUG)
com.bar.run()
com.foo.run()
com.foo.tar.run()
print("\n\n")
print("setting level on com.foo logger")
foo_logger = logging.getLogger("com.foo")
foo_logger.setLevel(logging.WARNING)
com.bar.run()
com.foo.run()
com.foo.tar.run()
