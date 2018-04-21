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
    'targets': ['myhdl', 'pytest'],
    'file_dep': ['venv/bin/python3'],
    'verbosity': 2
  }

def task_run_tests():
  """Run pytest tests."""
  return {
    'actions': [lambda : print("  not implemented.")],
    'verbosity': 2
  }

def create_test_report():
  """Create HTML and PDF test reports from rst files."""
  return {
    'actions': [lambda : print("  not implemented.")],
    'verbosity': 2
  }

def task_create_docs():
  """"""
  from doit.action import CmdAction

  return {
    'actions': [CmdAction('sphinx-build -M latexpdf source build', cwd = 'docs')],
    'verbosity': 1
  }

if __name__ == '__main__':
    from subprocess import call

    dependencies_installed = False

    from pathlib import Path
    venv_dir = Path('venv')

    print('\nInstalling Python 3 virtual environment...')
    call(['python3', '-m', 'venv', 'venv'])
    print('  Installing Python automation tools...\n')

    # Install packages that are not simple code modules (i.e. that have executable files)
    call(['venv/bin/pip3', 'install', '-r', 'requirements.txt'])

    print('\nRunning build tools...\n')
    call(["venv/bin/doit"])
