Using Django_Alfajor
====================

Intended usage of Alfajor is for purely functional testing. People who
use a fair amount of unit testing might be tempted to touch the
database then reload a page to see if it worked. While this will get
you some tests, it doesn't prove your site is working. This is due to
the fact that you can poke and prod your data into the form you want
it for the page, when that may or may not reflect the reality of your
site creating and manipulating data through the real interfaces that
your customers and users will use.
