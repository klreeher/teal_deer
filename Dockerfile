FROM python:3.6-alpine

# File Author / Maintainer
MAINTAINER K. L. Reeher

COPY . /output

EXPOSE PORT=8000
