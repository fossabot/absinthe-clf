#!venv/bin/python3

def task_install_dependencies():
  """Install required python modules"""

  def inst_deps(targets):
    from setuptools.command import easy_install
    import pip

    for target in targets:
      try:
        __import__(target)
      except ImportError:
        pip.main(['install', target])

  return {
    'actions': [inst_deps],
    'targets': ['myhdl'],
    'file_dep': ['venv/bin/python3']
  }

if __name__ == '__main__':
    from subprocess import call

    dependencies_installed = False

    from pathlib import Path
    venv_dir = Path('venv')

    if not venv_dir.is_dir():
      call(['python3', '-m', 'venv', 'venv'])
      call(['venv/bin/pip3', 'install', 'doit', 'wheel', 'setuptools'])

    call(["venv/bin/doit"])
