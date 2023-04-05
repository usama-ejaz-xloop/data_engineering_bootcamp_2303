An example application you will need to add metrics collection to.

The task will be to collect the number of uploaded files to Prometheus
so that it's visible in Grafana.

To run, use:

```
cd upload_app/

python3 -m venv venv
. venv/bin/activate

pip install Flask==2.2.2

python main.py
```
