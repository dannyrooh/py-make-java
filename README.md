# py-make-java versão 3.0

Gerador de cruds para api com o design pattern **clean archtecture**.
Essa versão contempla a geração de códigos fontes para java com as seguintes caracteristicas:

* cruds em java 11 com spring boot
* documentação em OpenApi (swagger 2.0)
* testes unitário com Junit 5
* testes de integração com Mockito e WireMock
* integração para sonarqube
* integração para verscode
* collections para postman

## Como gerar fontes

1. se posicionar no diretorio **src\main ** do projeto
2. chamar o arquivo main.py do projeto e passar os seguintes parâmetros
     **-g:[nome do group]** ➝ cor. Caso esta parêmetro não seja informado, os fontes serão gerados a partir do diretório corrente
     **-a:[nome do artefato]**  ➝ nome do diretório de onde serão gerados os fontes, caso o diretório não exista ele será criado
     **-t:[nome da tabela]**  ➝ nome da tabela de onde serão procurados os campos
     **-p:[nome do perfil]**  ➝ deverá se informado **main** ou **test**, caso não seja informado o group, ou não esteja posicionado no diretório main ou test
     **-template:[nome do template]**  ➝ quando informado será gerado somente o arquivo do template


## Help

Execute o arquivo main.py da seguinte maneira, para saber sobre o help na linha de comando

```shell
py main.py help | -h | --help 
```

## Sintaxe

* py main.py [comandos]

### Comandos

#### unícos por linha

* help 
     help | -h | --help 

#### podem ser concatenados

* -t [nome da tabela] ➝ nome da tabela é obrigatório
* -p [nome da package] ➝ quando não informado pega o que estiver configurado no config.yaml 

## Release da versão

* Alterado a configuração das tabelas e colunas de um arquivos em json,, que configurava varias tabelas, para arquivos unicos por tabela no formato .yaml

>
> ./data/diretorio/[nome da tabela].yaml

* Substituido o arquivo de mapeamento dos datatypes com o nome do banco de dados .json, para o arquivo datatype.yaml, onde é identificado o datatype padrão do gerador, para o datatype da linguagem e do banco de dados

* Adicionado propriedade no arquivo **template.yaml** para indicar se ele gera arquivos de teste. Caso e ele gere, deverá haver um ou mais arquivos correspondentes, como o mesmo nome do template  num diretorio abaixo :file_folder:***/test***, com a sequinte regra de nomeclatura:
    > &nbsp;
    > **test-[nome do template]-[ IT | Test ]-{[1..n]}**
    >
    > **test**- ➝ prefixo fixo para indicar que é um template de test
    > **[nome do template]** ➝ igual ao nome do template que gera o fonte principal
    > **[IT | Test]** ➝ sufixo que será atribuido ao nome do arquivo gerado. 
    > &nbsp;&nbsp;&nbsp;  IT ➝ corresponde aos teste de integração
    > &nbsp;&nbsp;&nbsp;  Test ➝ Teste unitário
    > **{[1..n]}** ➝ opcional, quando houver mais de um arquivo para o mesmo teste, colocar uma numeração para indicar que há mais de um arquivo para arquele teste
    > &nbsp;

    A propriedade adicionada está em folder.test: [enable | disable | None]
  
    ```yaml
      - folder:
              name: mapper
              test: enable
    ```
