## Lightweight and optimized Airflow setup for local development

## What is it and why you should care
Airflow has slow and bloated official docker compose file.

You can use this setup for learning process and local development in work.

### How to use
0. add needed providers to `requirements.txt`
0. add needed connections to `airflow-init` command
0. add dags to `dags` folder

### Test on Linux
First run
```bash
. up.sh --init
```

Future runs:
```bash
. up.sh
```

Turn down:
```bash
. down.sh
```

### TODO
. Test on Win and update instructions how to run .sh (maybe with WSL)

### Curator
[@LexxaRRioo ](https://github.com/LexxaRRioo)
[@razvodov_de_mentor](https://t.me/razvodov_de_mentor)