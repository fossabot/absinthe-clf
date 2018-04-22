#!venv/bin/python3

def task_run_tests():
  """Run pytest tests."""
  return {
    'actions': [lambda : print("  not implemented.")],
    'verbosity': 2
  }

def task_create_test_report():
  """Create HTML and PDF test reports from rst files."""
  from doit.action import CmdAction
  return {
    'actions': [CmdAction('../../venv/bin/sphinx-build -M html source build', cwd = 'tests/docs'), CmdAction('../../venv/bin/sphinx-build -M latexpdf source build', cwd = 'tests/docs')],
    'verbosity': 2
  }

def task_create_docs():
  """"""
  from doit.action import CmdAction

  return {
    'actions': [CmdAction('../venv/bin/sphinx-build -M latexpdf source build', cwd = 'docs')],
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
