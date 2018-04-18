#!venv/bin/python3

def task_install_dependencies():
  """Install required python modules"""

  def install_dependencies(targets):
    from setuptools.command import easy_install
    import pip

    for target in targets:
      try:
        __import__(target)
        print('  found %s.' % (target))
      except ImportError:
        print('  installing %s...' % (target))
        pip.main(['install', target])

  return {
    'actions': [install_dependencies],
    'targets': ['myhdl'],
    'file_dep': ['venv/bin/python3'],
    'verbosity': 2
  }

if __name__ == '__main__':
    from subprocess import call

    dependencies_installed = False

    from pathlib import Path
    venv_dir = Path('venv')

    if not venv_dir.is_dir():
      print('\nInstalling Python 3 virtual environment...')
      call(['python3', '-m', 'venv', 'venv'])
      print('  Installing Python automation tools...\n')
      call(['venv/bin/pip3', 'install', 'doit', 'wheel', 'setuptools'])

    print('\nRunning build tools...\n')
    call(["venv/bin/doit"])
