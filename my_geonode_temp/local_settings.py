DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'geonode',
         'USER': 'geonode',
         'PASSWORD': 'geonode',
     }
}

# GeoNode vector data backend configuration.

# Uploader backend (rest or importer)

UPLOADER_BACKEND_URL = 'rest'

# Import uploaded shapefiles into a GeoGit repository
GEOGIT_DATASTORE = False
GEOGIT_DATASTORE_NAME = 'geogit-repo'

UPLOADER_SHOW_TIME_STEP=False

#Import uploaded shapefiles into a database such as PostGIS?
DB_DATASTORE = True

#Database datastore connection settings
DB_DATASTORE_DATABASE = 'geonode_imports'
DB_DATASTORE_USER = 'geonode'
DB_DATASTORE_PASSWORD = 'geonode'
DB_DATASTORE_HOST = 'localhost'
DB_DATASTORE_PORT = '5432'
DB_DATASTORE_TYPE = 'postgis'
DB_DATASTORE_NAME = 'geonode_imports'

# Use the printNG geoserver lib
PRINTNG_ENABLED=True
