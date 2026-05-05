# devops-2026

Repositório voltado para armazenar os projetos de estudo de devops 
![CI](https://img.shields.io/github/actions/workflow/status/SEU_USUARIO/devops-2026/ci.yml?label=CI&style=flat-square)
![Security Scan](https://img.shields.io/github/actions/workflow/status/SEU_USUARIO/devops-2026/ci.yml?label=security%20scan&style=flat-square)
![Docker](https://img.shields.io/badge/docker-ready-blue?style=flat-square)
![IaC](https://img.shields.io/badge/IaC-terraform-purple?style=flat-square)

---

## O que este projeto faz

Aplicação Python containerizada com pipeline de entrega contínua do commit ao deploy, incluindo scan de segurança automático e monitoramento em tempo real.

```
push → lint → testes → build imagem → scan Trivy → push Docker Hub → deploy EC2
```

---

## Stack

| Camada | Tecnologia |
|---|---|
| App | Python + Flask |
| Container | Docker (multi-stage build) |
| Orquestração local | Docker Compose |
| CI/CD | GitHub Actions |
| Segurança | Trivy (scan de vulnerabilidades) |
| Infra (IaC) | Terraform |
| Cloud | AWS (EC2, S3, VPC, IAM) |
| Observabilidade | Prometheus + Grafana |
| Logs | Logs estruturados em JSON |

---

## Arquitetura

```
┌─────────────┐     push      ┌──────────────────────────────┐
│  Local dev  │ ────────────► │       GitHub Actions          │
└─────────────┘               │  lint → test → build → scan  │
                              └──────────────┬───────────────┘
                                             │ deploy
                                             ▼
                              ┌──────────────────────────────┐
                              │          AWS (EC2)            │
                              │  ┌────────┐  ┌───────────┐   │
                              │  │  App   │  │ Prometheus│   │
                              │  │(Docker)│  │  Grafana  │   │
                              │  └────────┘  └───────────┘   │
                              └──────────────────────────────┘
                                        infra via Terraform
```

---

## Como rodar localmente

**Pré-requisitos:** Docker e Docker Compose instalados.

```bash
git clone https://github.com/JoaoVitorMVBR/Devops-2026
cd devops-2026
docker compose up -d
```

App disponível em `http://localhost:8000`
Grafana disponível em `http://localhost:3000` (admin / admin)

---

## Pipeline CI/CD

Cada push na branch `main` dispara automaticamente:

1. **Lint** — verifica qualidade do código (flake8 + hadolint)
2. **Testes** — roda a suite de testes unitários
3. **Build** — constrói imagem Docker multi-stage
4. **Scan** — Trivy verifica vulnerabilidades (bloqueia se CRITICAL)
5. **Push** — envia imagem para Docker Hub
6. **Deploy** — SSH na EC2 e restart do container

PR só pode ser mergeado se todos os steps passarem.

---

## Infraestrutura como código

Toda a infra AWS é provisionada via Terraform — sem clique no console.

```bash
cd terraform/
terraform init
terraform plan
terraform apply
```

Recursos criados: VPC, subnet pública, security group, EC2 t2.micro, S3 bucket, IAM role com least privilege.

---

## Observabilidade

A aplicação expõe métricas via `/metrics` (formato Prometheus).

O stack de monitoramento sobe junto com `docker compose up`:
- **Prometheus** coleta métricas a cada 15s
- **Grafana** exibe dashboard com taxa de requisições, latência e erros
- **Alerta** configurado para erro rate > 5% por 5 minutos

---

## Segurança

- Imagem não roda como root (`USER` definido no Dockerfile)
- Secrets via variáveis de ambiente — nenhuma credencial no código
- IAM Role com permissões mínimas necessárias
- Scan automático de vulnerabilidades no pipeline (Trivy)
- Dependabot ativo para alertas de dependências

---

## Aprendizados

Projeto construído como parte de um plano de estudos. Documentei a jornada semana a semana no [LinkedIn](www.linkedin.com/in/joao-vilas-565b422a9).

---

## Contato

[LinkedIn](www.linkedin.com/in/joao-vilas-565b422a9) · [GitHub](https://github.com/JoaoVitorMVBR/Devops-2026)
