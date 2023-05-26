# Curso Digital: Conteinerização com Docker
## Ada Tech | Santander Coders 2023

### Comandos Docker:

**docker run -ti -p 8081:8081 nginx** -> Cria e roda um container na porta 8081 com a imagem nginx.

**docker ps -a** -> Lista todos os containers criados e seus status.

### Instruções Dockerfile

**FROM** -> Base de sistema operacional que pode ser customizado, mas que servirá de base para as demais configurações.

**WORKDIR** -> Acessa um diretório.

**ENV** -> Adiciona variáveis de ambiente.

**RUN** -> Roda comandos em tempo de execução.

**CMD** -> Roda comandos após o início do container, permitindo que o processo seja prioritário (Caso se usa a instrução **ENTRYPOINT**, a prioridade é dele e o CMD será utilizado como argumento).
