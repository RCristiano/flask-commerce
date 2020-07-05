# Flask-commerce

[![pipeline status](https://gitlab.com/rcristiano/flask-commerce/badges/master/pipeline.svg)](https://gitlab.com/rcristiano/flask-commerce/commits/master)  [![coverage report](https://gitlab.com/rcristiano/flask-commerce/badges/master/coverage.svg)](https://gitlab.com/rcristiano/flask-commerce/-/commits/master)


A simple REST API for e-commerce made with Flask

## Poetry

For the management of python packages, `poetry` was used

## Setup

Para que o pipeline rode completamente é necessário que se configure uma `token` de acesso a API no projeto. Nesse caso foi gerado uma `token` em minha conta pessoal, mas em projetos corporativos o ideal é que se crie uma *conta de serviço* e gere o `token` nela.

Adicione como variáveis do projeto (**Settings > CI/CD > Variables**), os valores:

- **NPA_USERNAME** - nome do usuário
- **NPA_PASSWORD** - token de acesso a api

Crie e adicione as seguintes `labels` no projeto (**Issues > Labels**):

- **bumb-major**
- **bump-minor**


Essas `labels` são utilizadas nos `merge requests` para definir qual será o tipo de atualização feito pelo versionamento. Caso não seja utilizada nenhuma `tag`, o script fará o `bump` na versão de **PATCH**, no caso de uma das `labels` ser definidas o `bump` acontece na versão **MAJOR** ou **MINOR** respectivamente.

## Pipeline

A criação do pipeline foi baseada no repositório: [gitlab-semantic-versioning (mrooding)](https://github.com/mrooding/gitlab-semantic-versioning)


O pipeline é composto dos `stages`:
  - env-vars
  - test
  - build
  - tag-version
  - registry


#### env-vars
Responsible for generating the variables used by the version and registration `jobs.

#### test
Job to execute Python tests.

#### build
Job que realiza o build da imagem Docker e verifica se não ocorrem erros antes que a `tag` seja criada.

#### tag-version
Execução do script de versionamento, para mais informações sobre como o script funciona ver o [repositório de origem](https://github.com/mrooding/gitlab-semantic-versioning).

#### registry
Build da imagem Docker final, `push` para o repositório com a `tag`gerada e atualização da imagem com `tag` *latest*.

# Run

## 

# TODO

- [ ] Doc
  - [ ] Flasgger ?
- [ ] Cart CRUD
