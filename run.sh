#!/bin/bash
docker run --rm -v "$(pwd)/pdfs:/app/pdfs" rpa-boletos python main.py pdfs
