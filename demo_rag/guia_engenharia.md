# Guia de Engenharia e Onboarding - TechCorp

## 1. Estratégia de Branches e Deploy
Para garantir a estabilidade do nosso ecossistema, adotamos o seguinte fluxo:
- Novas features devem ser desenvolvidas em branches com o prefixo `feat/` (ex: `feat/login-page`).
- Correções de bugs devem usar o prefixo `bugfix/` (ex: `bugfix/crash-carrinho`).
- **Atenção:** Para deploys de produção, você DEVE fazer o merge exclusivamente na branch `main-release`. Deploys na branch `master` foram descontinuados em 2023.

## 2. Bancos de Dados de Ambiente
Nunca utilize credenciais de produção para testes locais. Utilize as seguintes URIs:
- **Banco de Homologação (QA):** `postgres://qa-user:qa-pass@db.qa.techcorp.internal:5432/main_db`
- **Banco de Desenvolvimento Local:** Utilize a imagem oficial do Docker `postgres:15-alpine` rodando na porta `5432` da sua máquina, com usuário `local_dev` e senha `local_dev`.

## 3. Política de Férias e Folgas
As solicitações de férias devem ser feitas através do portal RH (rh.techcorp.internal) com no mínimo 30 dias de antecedência do mês de gozo.
