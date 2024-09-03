# These libraries are pre-installed in SN Labs. If running in another environment please uncomment lines below to install them:
# !pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
# !pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
# !pip install ipython-sql

cuando ejecuto ese codigo eliminando las # que hay antes de !pip install me da error.

Connection info needed in SQLAlchemy format, example:
               postgresql://username:password@hostname/dbname
               or an existing connection: dict_keys([])
cannot import name 'processors' from 'sqlalchemy' (/home/jupyterlab/conda/envs/python/lib/python3.7/site-packages/sqlalchemy/__init__.py)
Connection info needed in SQLAlchemy format, example:
               postgresql://username:password@hostname/dbname
               or an existing connection: dict_keys([])

cuando meto mis credenciales para iniciar una conexioncon mi db2 me sale este error.
