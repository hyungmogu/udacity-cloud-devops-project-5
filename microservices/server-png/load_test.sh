#!/bin/bash
locust -f tests_load/locustfile.py -P 8089 &
python app.py