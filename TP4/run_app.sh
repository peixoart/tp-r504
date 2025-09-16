#!/bin/bash

docker run --rm \
  --name tp4-app2 \
  -v $(pwd)/srv:/srv \
  --network net-tp4 \
  -p 5000:5000 \
  im-tp4
