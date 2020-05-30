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
   package_dir = {'pySPH_Shocktube': 'pySPH_Shocktube'},
   ext_modules=[Extension("pySPH_Shocktube.pyParticle",
                             ["pySPH_Shocktube/pyParticle.pyx",
                              "pySPH_Shocktube/Particle.cpp"], language="c++"),
                Extension("pySPH_Shocktube.pykernelhGauss",
                             ["pySPH_Shocktube/pykernelhGauss.pyx",
                              "pySPH_Shocktube/kernelhGauss.cpp"], language="c++")],
   cmdclass = {'build_ext': build_ext}
)
