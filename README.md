# Vynilog: Especificação de Requisitos

## Sumário
1. [Resumo](#1-resumo)
2. [Detalhamento da Aplicação](#2-detalhamento-da-aplicacao)
   - [2.1. Definição do Escopo](#21-definicao-do-escopo)
   - [2.2. Requisitos Funcionais (MVP - Escopo Atual)](#22-requisitos-funcionais-mvp---escopo-atual)
   - [2.3. Integração de Inteligência Artificial e APIs](#23-integracao-de-inteligencia-artificial-e-apis)
   - [2.4. Requisitos Futuros (Pós-MVP)](#24-requisitos-futuros-pos-mvp)
3. [Levantamentos e Diferenciais de Mercado](#3-levantamentos-e-diferenciais-de-mercado)

---

## 1. Resumo

O projeto visa solucionar as dificuldades enfrentadas por colecionadores de mídias físicas (CDs e vinis) na organização, gestão e expansão de seus acervos. A solução proposta é uma plataforma dedicada à catalogação pessoal, permitindo que o usuário registre seus itens, avalie obras, crie listas de desejos e utilize Inteligência Artificial como assistente para dados faltantes, dúvidas e recomendações. Funcionalidades mais complexas de interação social e geolocalização compõem a visão de longo prazo do produto.

**1. Qual o problema que vocês querem resolver?**
A dificuldade de colecionadores de mídias físicas em organizar e gerenciar seus acervos. Com o crescimento da coleção, o usuário frequentemente esquece os itens que já possui (gerando compras duplicadas) e enfrenta dificuldades para encontrar informações rápidas ou lojas físicas específicas que vendam os discos que procura.

**2. Qual a solução de vocês?**
O desenvolvimento de uma plataforma (aplicativo/site) para a catalogação detalhada das coleções de mídias físicas, incluindo dados completos dos álbuns, faixas e avaliações pessoais. A solução integra a criação de listas de desejos e a utilização de uma Inteligência Artificial via API para automatizar cadastros faltantes e atuar como um chatbot interativo para tirar dúvidas e recomendar obras. No futuro, a plataforma também mapeará lojas físicas e permitirá interação entre usuários.

**3. Que outras soluções existem e por que a de vocês é melhor ou diferente?**
Atualmente existem plataformas como Discogs, RateYourMusic e Last.fm, além do uso de planilhas manuais. Essas ferramentas falham por não possuírem foco nacional, relegarem a avaliação pessoal a um plano secundário, apresentarem interfaces complexas e terem uso muito voltado para compra e venda direta. Nossa solução foca estritamente na organização pessoal e na introdução de uma interface inteligente (chatbot via IA) para auxiliar o colecionador, unificando as funcionalidades de forma intuitiva.

**4. Qual o escopo da solução de vocês?**
O escopo base compreende um catálogo focado exclusivamente em CDs e vinis, exibindo dados técnicos (capa, faixas, ano, gravadora, produtores, artistas) sem envolver precificação, estado de conservação ou transações de compra e venda. Contempla contas individuais com acervos, avaliações, listas de desejos (com redirecionamento para Amazon/Discogs) e assistência de IA para suporte de informações.

**5. Quais as features?**
* Criação de conta, login e logout.
* Cadastro e consulta detalhada de CDs e vinis.
* Avaliação de álbuns com nota (1 a 5 estrelas), resenha e seleção de faixas favoritas.
* Lista de desejos com redirecionamento externo.
* Automação de cadastro de itens fora da base utilizando IA.
* Chatbot com IA para tirar dúvidas sobre obras musicais e solicitar recomendações.
* *(Visão Futura)*: Registro de lojas físicas, busca de itens por loja, visualização de perfis públicos, seguidores e chat entre usuários.

**6. Como vocês vão incorporar IA via API na solução?**
A inteligência artificial (Gemini) atuará em duas frentes integradas à API do Discogs:
1. **Automação de Cadastro:** Se a API do Discogs não encontrar um álbum, a IA buscará e estruturará os dados de forma automatizada (se a IA falhar, o cadastro é manual).
2. **Chatbot (Q&A e Recomendações):** O usuário poderá abrir um chat para tirar dúvidas específicas (ex: "quem compôs essa faixa?") ou pedir recomendações diretas (ex: "quais discos são parecidos com este?"). O sistema enviará o contexto atual para o Gemini formular respostas dinâmicas.

**7. O que pode ou vai ficar para o futuro?**
Para garantir o aprendizado focado e a qualidade do código para alunos do primeiro ano, funcionalidades que exigem relacionamentos complexos de banco de dados, tempo real ou geolocalização ficarão para o futuro. Isso inclui:
* **Sistema social e de mensagens:** Seguir usuários, chat privado para trocas e comentários em perfis.
* **Mapeamento de lojas físicas:** Registrar locais de compra e pesquisar disponibilidade por loja em mapas.
* **Recomendações ativas (Background):** A recomendação proativa cruzando todos os dados da coleção de forma automática (o usuário deverá pedir via chatbot nesta primeira versão).
* **Estatísticas detalhadas:** Geração de gráficos complexos sobre a distribuição de estilos.

**8. Como vocês garantem que vão entregar esse projeto dentro de 2 meses?**
Garantiremos a entrega através da definição rigorosa de um Produto Mínimo Viável (MVP) focado exclusivamente no domínio principal: o CRUD (Criar, Ler, Atualizar, Deletar) da coleção de discos e as integrações essenciais. Como alunos do primeiro ano, limitaremos a complexidade técnica focando no que precisamos aprender e consolidar agora: modelagem de banco de dados, construção de interfaces funcionais e consumo de APIs REST externas (Discogs e Gemini). 

O desenvolvimento será dividido em etapas semanais claras:
1. Modelagem do banco de dados e autenticação básica.
2. Desenvolvimento do CRUD de álbuns (cadastro manual).
3. Integração com a API do Discogs para buscas de dados de catálogo.
4. Implementação do chatbot utilizando a API do Gemini, viabilizando dúvidas e recomendações interativas via requisições HTTP simples.

Caso haja qualquer atraso nas etapas iniciais, recursos secundários (como "Lista de Desejos" e "Avaliações") serão temporariamente suspensos para garantir que o catálogo principal e o chatbot sejam entregues funcionando perfeitamente.

---

## 2. Detalhamento da Aplicacao

### 2.1. Definição do Escopo
A aplicação atualiza o conceito de gerenciador de coleções, priorizando a robustez do banco de dados pessoal e o uso prático de IA. Para o MVP de 2 meses, o sistema atuará de forma isolada de transações financeiras e redes sociais complexas, garantindo a entrega de uma ferramenta estável de catalogação. O valor principal reside no registro minucioso dos itens (via API Discogs) e no assistente conversacional (Gemini).

### 2.2. Requisitos Funcionais (MVP - Escopo Atual)
* **RF01:** O sistema deve permitir a criação de conta, autenticação e logout de usuários.
* **RF02:** O sistema deve permitir realizar o CRUD (Cadastro, Consulta, Atualização e Exclusão) de CDs e vinis na coleção pessoal.
* **RF03:** O sistema deve exibir metadados completos de cada item (capa, faixas, ano, gravadora, produtores, artistas).
* **RF04:** O sistema deve permitir ao usuário avaliar os álbuns de sua coleção (nota de 1 a 5 estrelas e resenha opcional).
* **RF05:** O sistema deve manter uma "Lista de Desejos" com redirecionamento de links externos para aquisição (Discogs, Amazon).

### 2.3. Integração de Inteligência Artificial e APIs
* **RS01:** O sistema deve realizar a busca primária de metadados na API do Discogs.
* **RS02:** Caso a busca no Discogs retorne vazia, o sistema deve acionar a API do Gemini para estruturar os dados do álbum e sugerir o preenchimento.
* **RS03:** O sistema deve possuir uma interface de Chatbot vinculada à API do Gemini, permitindo ao usuário fazer perguntas de contexto e solicitar recomendações musicais via prompt.

### 2.4. Requisitos Futuros (Pós-MVP)
Para não perder a visão completa do produto, os seguintes requisitos compõem o backlog futuro do sistema:
* **RF-FUTURO 01:** Vincular álbuns cadastrados a lojas físicas locais e realizar buscas geolocalizadas.
* **RF-FUTURO 02:** Sistema de seguidores, perfis públicos e comentários mútuos.
* **RF-FUTURO 03:** Chat entre usuários para negociação de mídias marcadas como "disponíveis para troca".
* **RF-FUTURO 04:** Dashboards de estatísticas e recomendações geradas automaticamente no background.

---

## 3. Levantamentos e Diferenciais de Mercado

Em oposição aos sistemas concorrentes e métodos manuais, a presente aplicação unifica a robustez de um banco de dados global (Discogs) com uma experiência focada, limpa e moderna. O grande diferencial desta aplicação (MVP) frente ao mercado é a eliminação da poluição visual gerada por marketplaces integrados, oferecendo, em contrapartida, um assistente virtual conversacional. A inclusão do chatbot com IA preenche uma lacuna crítica, permitindo que o usuário explore o próprio acervo e tire dúvidas técnicas sobre as obras musicais de forma instantânea, promovendo uma cultura rica e interativa de colecionismo.
