# App Database 

### 1. This will create an environment using the “generic” template. "migrations" is the name of the package. 
<code> alembic init migrations </code>

#### commentary: alembic.init is de file to config migrations with DB.

### 2. Configurate path to save migrations in file alembic.init
<code> [alembic]
script_location = app_database/migrations </code>

### 3. In file migrations/env.py need define variable target_metadata in Our case we define class base in file database.py, we need import class Base from there
<code> from database import Base
target_metadata = Base.metadata
</code>