# Vinylog – Catálogo de Mídias Físicas

O Vinylog é uma plataforma criada para colecionadores organizarem os seus acervos de CDs e vinis, facilitando a gestão da coleção e a descoberta de informações através de um assistente de Inteligência Artificial.

## O Desafio do Colecionador

Com o crescimento de uma coleção de mídias físicas, manter o controle do acervo torna-se complexo. É comum esquecer os itens que já possui, o que acaba gerando compras duplicadas. Além disso, a busca por informações técnicas sobre as obras, metadados de álbuns ou a localização de lojas físicas específicas para adquirir novos discos costuma ser fragmentada e trabalhosa.

## A Proposta do Vinylog

O sistema atua como um gerenciador de coleções detalhado e inteligente. A plataforma permite registrar discos, avaliar obras e criar listas de desejos. Em paralelo, a Inteligência Artificial integrada atua nos bastidores para preencher dados faltantes e funciona como um assistente interativo, pronto para tirar dúvidas e recomendar novos álbuns baseados no contexto do usuário.

## Por Que o Vinylog é Diferente?

Ao contrário de plataformas tradicionais como Discogs, RateYourMusic ou o uso de planilhas manuais, o Vinylog foca na experiência individual do usuário:

* **Foco na organização pessoal:** Interface limpa e livre da poluição visual e da complexidade de marketplaces focados em compra, venda e precificação.
* **Valorização da experiência:** A avaliação pessoal, as resenhas e a marcação de faixas favoritas assumem o papel principal, em vez de ficarem em segundo plano.
* **Exploração inteligente:** Em vez de bancos de dados estáticos que exigem pesquisa manual exaustiva, o sistema oferece um assistente conversacional para explorar o próprio acervo, tirar dúvidas técnicas e descobrir novas músicas.

## Escopo do Projeto (MVP)

A primeira versão (MVP) tem o objetivo de entregar a base sólida da plataforma, focada estritamente na organização:

* **Catálogo Especializado:** Foco exclusivo em CDs e vinis, exibindo dados técnicos (capa, faixas, ano, gravadora) sem o envolvimento de transações financeiras.
* **Gestão Pessoal:** Contas individuais com controle total sobre o acervo, sistema de avaliações e lista de desejos.
* **Integração Inteligente:** Automação de cadastros e suporte via chatbot utilizando API REST.

*(Recursos de maior complexidade, como redes sociais, chat direto entre usuários e mapeamento de lojas físicas locais, estão mapeados para as próximas versões do produto).*

## Funcionalidades Principais

* **Autenticação:** Registro, login e logout individual para proteção do acervo.
* **Gestão de Catálogo:** CRUD (Cadastro, Consulta, Atualização e Exclusão) de itens na coleção com metadados completos.
* **Reviews e Avaliações:** Sistema para dar notas (1 a 5 estrelas), escrever resenhas em texto e marcar faixas favoritas.
* **Lista de Desejos:** Área dedicada para discos procurados, com redirecionamento de links externos para aquisição (Amazon, Discogs).
* **Preenchimento Automático:** Uso de IA para estruturar e preencher metadados de itens que não forem encontrados na base de dados primária.
* **Assistente Musical:** Chatbot integrado para responder perguntas de contexto sobre as obras e sugerir recomendações.

## Como a IA se Integra ao Acervo

A inteligência artificial atua em duas frentes integradas ao catálogo (utilizando a API do Gemini):

1. **Automação de Cadastro:** Se a API primária (Discogs) não encontrar um álbum, a IA busca e estrutura os metadados automaticamente para viabilizar o registro pelo usuário.
2. **Assistente Especializado:** O usuário pode abrir um chat para tirar dúvidas técnicas pontuais (ex: "quem compôs e produziu essa faixa?") ou pedir recomendações dinâmicas (ex: "quais discos da minha lista de desejos têm uma sonoridade parecida com este?").
