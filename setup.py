from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
name='pySPH-ChockTube',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='m.c.juandeanda@gmail.com',
   packages=[ 'pySPH_chocktube'],
   package_dir = {'pySPH_chocktube': 'pySPH_chocktube'},
   ext_modules=[Extension("pySPH_chocktube.pyParticle",
                             ["pySPH_chocktube/pyParticle.pyx",
                              "pySPH_chocktube/Particle.cpp"], language="c++")],
   cmdclass = {'build_ext': build_ext}
)
