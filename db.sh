#!/bin/bash

flask db init
flask db migrate -m "products table"
flask db upgrade
