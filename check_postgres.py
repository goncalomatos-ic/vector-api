import time

# Wait for postgres to be up and running
#
# Improvement: try to connect to postgres
#
# Note: pinging the container is not enough because
#       it doesn't ensure that postgres is running
time.sleep(10)