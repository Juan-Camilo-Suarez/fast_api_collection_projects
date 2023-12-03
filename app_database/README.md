# App Database 

### 1. This will create an environment using the “generic” template. "migrations" is the name of the package. 
<code> alembic init migrations </code>

#### commentary: alembic.init is de file to config migrations with DB.

### 2. We need configurate path to save migrations in file alembic.init
<code> [alembic]
script_location = app_database/migrations </code>